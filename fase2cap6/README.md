# Sistema de Monitoramento e Controle de Perdas na Colheita de Cana-de-Açúcar

## 1. Descrição do Problema

O agronegócio é um dos setores mais relevantes e complexos da economia brasileira, respondendo por uma fatia expressiva do Produto Interno Bruto (PIB). O Brasil mantém a liderança mundial na produção de cana-de-açúcar, alcançando marcas superiores a 600 milhões de toneladas por safra.

Apesar da alta capacidade produtiva e da crescente adoção da mecanização do campo, as perdas operacionais durante o processo de colheita continuam sendo um dos principais gargalos operacionais e financeiros do setor.

### Principais Indicadores e Impactos
- **Colheita Manual:** Apresenta índices de perda historicamente baixos, raramente ultrapassando 5% da produção total.
- **Colheita Mecanizada:** Apresenta índices de perda que chegam a até 15% do volume colhido, decorrentes de regulagens inadequadas de máquinas, velocidade inadequada de deslocamento, desníveis no solo e falta de alinhamento com a linha de plantio.
- **Impacto Financeiro:** No estado de São Paulo, que conta com cerca de 3 milhões de hectares cultivados e produtividade média de 100 toneladas por hectare, as perdas decorrentes da colheita mecanizada geram um prejuízo anual estimado em dezenas de milhões de reais para o setor produtivo e reduzem a arrecadação tributária governamental.

---

## 2. Arquitetura da Solução

Para responder a esse desafio, o projeto disponibiliza uma aplicação em Python desenvolvida com o objetivo de registrar, consolidar, auditá-las e persistir as métricas de perda coletadas nos talhões agrícolas.

### Funcionalidades do Sistema
1. **Cálculo de Prejuízo Financeiro:** Determina o impacto financeiro em Reais (R$) com base na metragem de tonelagem colhida e na porcentagem de perda registrada.
2. **Visualização em Memória:** Organiza os dados coletados em estruturas de dados nativas para exibição consolidada em formato tabular no terminal.
3. **Persistência de Dados (Arquivos):**
   - Exportação do relatório estruturado no formato **JSON** (`dados_colheita.json`).
   - Registro contínuo de logs de auditoria e execuções no formato **TXT** (`auditoria_colheita.txt`).
4. **Integração com Banco de Dados:** Sincronização automatizada dos registros operacionais com um banco de dados relacional **Oracle Database**.

---

## 3. Requisitos Técnicos e Estrutura do Código

A aplicação atende rigorosamente às seguintes diretrizes do desenvolvimento em Python:

- **Subalgoritmos:**
  - **Funções com passagem de parâmetros e retorno de valor:** `calcular_prejuizo(toneladas_colhidas, percentual_perda)` para o cálculo do dano financeiro.
  - **Procedimentos com passagem de parâmetros:** `gerar_relatorio_memoria(registros)` para exibição formatada e procedimentos para persistência de arquivos e banco de dados.
- **Estruturas de Dados:**
  - **Tupla:** Definida para limites operacionais imutáveis (ex.: `LIMITES_PERDA`).
  - **Dicionário:** Utilizado para representar a estrutura individual de cada talhão.
  - **Lista / Tabela de Memória:** Coleção encadeada dos dicionários de talhões para processamento em memória RAM.
- **Manipulação de Arquivos:**
  - Leitura e escrita de arquivos estruturados **JSON**.
  - Apêndice contínuo em arquivos de texto plano **TXT** com carimbo de data e hora.
- **Conexão Oracle Database:**
  - Utilização da biblioteca `oracledb` operando no modo *Thin* para execução de comandos SQL parametrizados.

---

## 4. Pré-requisitos e Dependências

- Python 3.8 ou superior
- Biblioteca `oracledb` instalada

Para instalar as dependências necessárias, execute o comando:

```bash
pip install oracledb
```

---

## 5. Instruções de Execução

1. Certifique-se de ter o ambiente Python configurado e as dependências instaladas.
2. Clone ou faça o download deste repositório contendo o arquivo `main.py`.
3. Para executar o projeto, abra o terminal na pasta do projeto e digite:

```bash
python main.py
```

---

## 6. Estrutura do Arquivo de Saída JSON

Exemplo da estrutura do arquivo `dados_colheita.json` gerado pelo sistema:

```json
[
    {
        "id": 1,
        "talhao": "Talhao-A",
        "metodo": "Mecânica",
        "toneladas": 600.0,
        "perda_perc": 14.0,
        "prejuizo_rs": 12600.0
    },
    {
        "id": 2,
        "talhao": "Talhao-B",
        "metodo": "Manual",
        "toneladas": 350.0,
        "perda_perc": 3.5,
        "prejuizo_rs": 1837.5
    }
]
```

---

## 7. Estrutura do Log de Auditoria TXT

Exemplo dos registros gerados no arquivo `auditoria_colheita.txt`:

```text
[2026-10-17 23:00:00] Relatório de perdas processado com 2 talhões monitorados.
```
