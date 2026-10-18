from datetime import datetime
import json

# ==========================================
# 1. ESTRUTURAS DE DADOS E CONSTANTES
# ==========================================

# Tupla: Limites aceitáveis de perda (%) (Manual, Mecânica)
LIMITES_PERDA = (5.0, 15.0)

# Constante de mercado: Valor médio da tonelada de cana em R$
VALOR_TONELADA_CANA = 150.0

# Tabela de memória (Lista estruturada contendo Dicionários)
tabela_memoria = []


# ==========================================
# 2. SUBALGORITMOS: FUNÇÃO E PROCEDIMENTO
# ==========================================


def calcular_prejuizo(toneladas_colhidas, percentual_perda):
  """Função: Calcula o valor financeiro do prejuízo com base nas perdas.

  Retorna o valor calculado (float).
  """
  toneladas_perdidas = toneladas_colhidas * (percentual_perda / 100.0)
  prejuizo_total = toneladas_perdidas * VALOR_TONELADA_CANA
  return round(prejuizo_total, 2)


def gerar_relatorio_memoria(registros):
  """Procedimento: Exibe na tela a tabela de memória formatada de forma

  tabular, sem retornar valor (executa uma ação visual).
  """
  print("\n" + "=" * 70)
  print(f"{'RELATÓRIO DE MONITORAMENTO DE PERDAS NA COLHEITA':^70}")
  print("=" * 70)
  print(
      f"{'ID':<5} | {'Talhão':<8} | {'Método':<10} | {'Perda (%)':<10} |"
      f" {'Prejuízo (R$)':<15}"
  )
  print("-" * 70)

  for reg in registros:
    print(
        f"{reg['id']:<5} | {reg['talhao']:<8} | {reg['metodo']:<10} |"
        f" {reg['perda_perc']:<10.2f} | {reg['prejuizo_rs']:<15.2f}"
    )
  print("=" * 70)


# ==========================================
# 3. MANIPULAÇÃO DE ARQUIVOS (TEXTO E JSON)
# ==========================================


def salvar_dados_json(registros, nome_arquivo="dados_colheita.json"):
  """Manipulação de Arquivo JSON: Salva o backup da tabela de memória."""
  try:
    with open(nome_arquivo, "w", encoding="utf-8") as f:
      json.dump(registros, f, ensure_ascii=False, indent=4)
    print(
        f"[Arquivo JSON] Dados salvos com sucesso no arquivo '{nome_arquivo}'."
    )
  except Exception as e:
    print(f"[Erro JSON] Falha ao salvar arquivo: {e}")


def registrar_auditoria_txt(mensagem, nome_arquivo="auditoria_colheita.txt"):
  """Manipulação de Arquivo de Texto: Insere logs de auditoria do sistema."""
  try:
    with open(nome_arquivo, "a", encoding="utf-8") as f:
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      f.write(f"[{timestamp}] {mensagem}\n")
    print(f"[Arquivo TXT] Log de auditoria registrado em '{nome_arquivo}'.")
  except Exception as e:
    print(f"[Erro TXT] Falha ao gravar log: {e}")


# ==========================================
# 4. CONEXÃO COM BANCO DE DADOS ORACLE
# ==========================================


def sincronizar_com_oracle(registros):
  """Conexão com Banco de Dados Oracle utilizando o driver oficial 'oracledb'."""
  # Nota: Certifique-se de ter a biblioteca instalada (`pip install oracledb`)
  import oracledb

  dsn_tns = oracledb.makedsn(
      host="localhost", port="1521", service_name="XE"
  )  # Exemplo de DSN
  usuario = "sistema_agricola"
  senha = "sua_senha_segura"

  print("\n[Oracle DB] Tentando estabelecer conexão com o banco de dados...")

  try:
    # Conectando ao Oracle Database no modo Thin (não requer Oracle Client instalado)
    connection = oracledb.connect(
        user=usuario, password=senha, dsn=dsn_tns
    )
    cursor = connection.cursor()

    print("[Oracle DB] Conexão bem-sucedida! Sincronizando registros...")

    for reg in registros:
      # Exemplo de comando SQL preparado para inserção
      sql = """
                INSERT INTO TB_COLHEITA_PERDAS (ID, TALHAO, METODO, TONELADAS, PERDA_PERC, PREJUIZO_RS)
                VALUES (:1, :2, :3, :4, :5, :6)
            """
      cursor.execute(
          sql,
          (
              reg["id"],
              reg["talhao"],
              reg["metodo"],
              reg["toneladas"],
              reg["perda_perc"],
              reg["prejuizo_rs"],
          ),
      )

    connection.commit()
    print("[Oracle DB] Todos os registros foram sincronizados com sucesso!")

    cursor.close()
    connection.close()

  except Exception as e:
    # Caso o banco não esteja ativo localmente, tratamos a exceção de forma amigável
    print(
        f"[Oracle DB] Aviso de Conexão: Não foi possível conectar ao banco de"
        f" dados ({e})."
    )
    print(
        "[Oracle DB] Os dados foram mantidos seguros na tabela de memória e no"
        " arquivo JSON."
    )


# ==========================================
# 5. FLUXO PRINCIPAL DA APLICAÇÃO
# ==========================================


def main():
  print("Iniciando Sistema de Monitoramento de Perdas na Colheita de Cana...")

  # Simulação de inserção de dados capturados no campo (Dicionários adicionados à Lista / Tabela de Memória)
  reg1 = {
      "id": 1,
      "talhao": "Talhao-A",
      "metodo": "Mecânica",
      "toneladas": 600.0,
      "perda_perc": 14.0,
      "prejuizo_rs": calcular_prejuizo(600.0, 14.0),
  }

  reg2 = {
      "id": 2,
      "talhao": "Talhao-B",
      "metodo": "Manual",
      "toneladas": 350.0,
      "perda_perc": 3.5,
      "prejuizo_rs": calcular_prejuizo(350.0, 3.5),
  }

  tabela_memoria.append(reg1)
  tabela_memoria.append(reg2)

  # Utilizando o Procedimento para exibir a tabela de memória
  gerar_relatorio_memoria(tabela_memoria)

  # Manipulação de arquivos
  salvar_dados_json(tabela_memoria)
  registrar_auditoria_txt(
      "Relatório de perdas processado com 2 talhões monitorados."
  )

  # Conexão com Oracle Database
  sincronizar_com_oracle(tabela_memoria)


if __name__ == "__main__":
  main()
