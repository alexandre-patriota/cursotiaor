import math

# Vetores para armazenamento dos dados
culturas = []
tipos_geometricos = []
areas = []
insumos = []
quantidades_insumo_litros = []


def exibir_menu():
  print("\n========================================")
  print("   SISTEMA DE GESTÃO AGRÍCOLA SUSTENTÁVEL ")
  print("========================================")
  print("1. Entrada de dados (Cadastrar plantio)")
  print("2. Saída de dados (Visualizar registros)")
  print("3. Atualizar dados")
  print("4. Deletar dados")
  print("5. Sair do programa")


def obter_dados_plantio():
  """Função auxiliar que padroniza o fluxo de entrada e cálculo dos dados."""
  print("\nCulturas sustentáveis disponíveis:")
  print("1. Mandioca (Forma geométrica: Retângulo)")
  print("2. Feijão-caupi (Forma geométrica: Círculo)")

  escolha_cultura = input("Selecione a cultura (1 ou 2): ")

  if escolha_cultura == "1":
    cultura = "Mandioca"
    figura = "Retângulo"
    base = float(input("Digite a base do retângulo de plantio (metros): "))
    altura = float(input("Digite a altura do retângulo de plantio (metros): "))
    area = base * altura
    print(f"-> Área calculada do Retângulo: {area:.2f} m²")

  elif escolha_cultura == "2":
    cultura = "Feijão-caupi"
    figura = "Círculo"
    raio = float(input("Digite o raio da área circular de plantio (metros): "))
    area = math.pi * (raio**2)
    print(f"-> Área calculada do Círculo: {area:.2f} m²")
  else:
    print("Opção de cultura inválida!")
    return None

  produto = input(
      "Digite o nome do insumo (ex: Fosfato Natural / Biofertilizante): "
  )
  qtd_por_m2 = float(input("Digite a quantidade do insumo por metro quadrado: "))

  print("Escolha a unidade da quantidade informada:")
  print("1. Mililitros por metro quadrado (mL/m²)")
  print("2. Litros por metro quadrado (L/m²)")
  unidade_opcao = input("Digite 1 ou 2: ")

  # Cálculo da quantidade total em litros
  if unidade_opcao == "1":
    total_litros = (area * qtd_por_m2) / 1000  # Converte mL para Litros
  else:
    total_litros = area * qtd_por_m2

  return cultura, figura, area, produto, total_litros


# Loop principal do programa
while True:
  exibir_menu()
  opcao = input("Escolha uma opção (1-5): ")

  if opcao == "1":
    print("\n--- ENTRADA DE DADOS ---")
    resultado = obter_dados_plantio()

    if resultado is not None:
      cultura, figura, area, produto, total_litros = resultado

      # Armazenando nos vetores
      culturas.append(cultura)
      tipos_geometricos.append(figura)
      areas.append(area)
      insumos.append(produto)
      quantidades_insumo_litros.append(total_litros)

      print(
          f"\n[Sucesso] Insumo cadastrado! Total necessário:"
          f" {total_litros:.2f} Litros."
      )

  elif opcao == "2":
    print("\n--- SAÍDA DE DADOS (RELATÓRIO) ---")
    if len(culturas) == 0:
      print("Nenhum dado cadastrado no sistema.")
    else:
      for i in range(len(culturas)):
        print(
            f"[{i}] Cultura: {culturas[i]} | Geometria: {tipos_geometricos[i]}"
            f" | Área: {areas[i]:.2f} m² | Insumo: {insumos[i]}"
            f" | Qtd Total: {quantidades_insumo_litros[i]:.2f} L"
        )

  elif opcao == "3":
    print("\n--- ATUALIZAÇÃO DE DADOS ---")
    if len(culturas) == 0:
      print("Nenhum dado cadastrado para atualizar.")
    else:
      for i in range(len(culturas)):
        print(f"[{i}] {culturas[i]} - Insumo: {insumos[i]}")

      pos = int(
          input("Digite o índice (posição) do registro que deseja atualizar: ")
      )
      if 0 <= pos < len(culturas):
        print(f"Atualizando registro {pos}:")
        resultado = obter_dados_plantio()

        if resultado is not None:
          cultura, figura, area, produto, total_litros = resultado

          # Atualizando os valores nas mesmas posições dos vetores
          culturas[pos] = cultura
          tipos_geometricos[pos] = figura
          areas[pos] = area
          insumos[pos] = produto
          quantidades_insumo_litros[pos] = total_litros

          print(
              f"\n[Sucesso] Registro {pos} atualizado com sucesso! Novo total:"
              f" {total_litros:.2f} Litros."
          )
      else:
        print("Posição inválida!")

  elif opcao == "4":
    print("\n--- DELEÇÃO DE DADOS ---")
    if len(culturas) == 0:
      print("Nenhum dado cadastrado para deletar.")
    else:
      for i in range(len(culturas)):
        print(f"[{i}] {culturas[i]} - Insumo: {insumos[i]}")

      pos = int(input("Digite o índice (posição) do registro que deseja deletar: "))
      if 0 <= pos < len(culturas):
        culturas.pop(pos)
        tipos_geometricos.pop(pos)
        areas.pop(pos)
        insumos.pop(pos)
        quantidades_insumo_litros.pop(pos)
        print("Registro deletado com sucesso!")
      else:
        print("Posição inválida!")

  elif opcao == "5":
    print("Encerrando o programa. Até logo!")
    break
  else:
    print("Opção inválida! Por favor, escolha um número de 1 a 5.")