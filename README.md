# 🚗 Tabela FIPE Scraper - Automação com Python e Selenium

Projeto pessoal de automação com **Python + Selenium** que realiza scraping dos dados de veículos diretamente no site oficial da **Tabela FIPE**, salvando os resultados em um arquivo `.json` estruturado.

Este projeto foi desenvolvido com foco em **praticar automação de tarefas web**, **extração de dados estruturados** e **manipulação de arquivos JSON** — habilidades essenciais para back-end e data engineering.

----------------------------------------------------------------------------------------

## 🎯 Objetivos do Projeto:

- Aplicar conceitos de **web scraping com Selenium**
- Praticar espera dinâmica com `WebDriverWait` e `ExpectedConditions`
- Simular o comportamento do usuário para interagir com um site dinâmico
- Exportar os dados coletados em **formato JSON** organizado
- Consolidar conhecimento prático em **Python** com foco em automações e dados

-------------------------------------------------------------------------------------------


## 🛠️ Tecnologias e Bibliotecas utilizadas:

- **Python 3.10+**
- **Selenium** (com `WebDriverWait` e `By`)
- **Google Chrome + ChromeDriver**
- **JSON** (exportação estruturada de dados)
- `datetime`, `time` e tratamento de exceções

-------------------------------------------------------------------------------------------


## 📊 Dados extraídos

O script coleta automaticamente as seguintes informações de um veículo:

- **Mês de referência**
- **Código FIPE**
- **Marca**
- **Modelo**
- **Ano/Combustível**
- **Código de autenticação**
- **Data da consulta**

Exemplo da saída no arquivo **JSON**:

```json

  "0": {
    "M�s de refer�ncia:": "junho de 2025",
    "C�digo Fipe:": "038003-2",
    "Marca:": "Acura",
    "Modelo:": "Integra GS 1.8",
    "Ano Modelo:": "1992 Gasolina",
    "Autentica��o": "gjfv1zf914",
    "Data da consulta": "quarta-feira, 11 de junho de 2025 00:35",
    "Pre�o M�dio": "R$ 11.097,00"
  },
  "1": {
    "M�s de refer�ncia:": "junho de 2025",
    "C�digo Fipe:": "038003-2",
    "Marca:": "Acura",
    "Modelo:": "Integra GS 1.8",
    "Ano Modelo:": "1991 Gasolina",
    "Autentica��o": "f7v5gtq0h0",
    "Data da consulta": "quarta-feira, 11 de junho de 2025 00:35",
    "Pre�o M�dio": "R$ 10.366,00"
  },
  "2": {
    "M�s de refer�ncia:": "junho de 2025",
    "C�digo Fipe:": "038002-4",
    "Marca:": "Acura",
    "Modelo:": "Legend 3.2/3.5",
    "Ano Modelo:": "1998 Gasolina",
    "Autentica��o": "mx3g4v6wz0",
    "Data da consulta": "quarta-feira, 11 de junho de 2025 00:35",
    "Pre�o M�dio": "R$ 25.397,00"
  }