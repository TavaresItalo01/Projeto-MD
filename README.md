
# 📊 API de Classificação de Clientes - Cartão de Crédito

Esta API foi desenvolvida com **FastAPI** e utiliza um modelo treinado de **Gradient Boosting** para prever se um cliente de cartão de crédito poderá se tornar inadimplente no próximo mês com base em dados demográficos e financeiros.

---

## 📦 Requisitos

- Python 3.8 ou superior
- `pip` (gerenciador de pacotes)

---

## ⚙️ Instalação e Execução

### 1. Clone o projeto ou copie os arquivos
```bash
git clone https://github.com/seu-usuario/projeto-classificacao-clientes.git
cd projeto-classificacao-clientes
```

### 2. Crie e ative um ambiente virtual

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a API
```bash
uvicorn main:app --reload
```

---

## 🚀 Acessar a API

Depois de executada, acesse:

```
http://127.0.0.1:8000/docs
```

Você verá uma interface interativa gerada automaticamente com Swagger.

---

## 🧪 Como Testar a API

### ✅ Via Swagger UI (recomendado)
1. Acesse `http://127.0.0.1:8000/docs`
2. Clique em `POST /prever`
3. Clique em "Try it out"
4. Cole um dos exemplos abaixo no corpo da requisição e clique em **Execute**:

```json
{
  "LIMIT_BAL": 30000,
  "SEX": 1,
  "EDUCATION": 2,
  "MARRIAGE": 1,
  "AGE": 25,
  "PAY_1": 0,
  "PAY_2": 0,
  "PAY_3": 0,
  "PAY_4": 0,
  "PAY_5": 0,
  "PAY_6": 0,
  "BILL_AMT1": 3913,
  "BILL_AMT2": 3102,
  "BILL_AMT3": 689,
  "BILL_AMT4": 0,
  "BILL_AMT5": 0,
  "BILL_AMT6": 0,
  "PAY_AMT1": 0,
  "PAY_AMT2": 689,
  "PAY_AMT3": 0,
  "PAY_AMT4": 0,
  "PAY_AMT5": 0,
  "PAY_AMT6": 0
}
```

## 🧾 Resposta esperada

```json
{
  "classe_predita": 0
}
```

```json
{
  "LIMIT_BAL": 150000,
  "SEX": 2,
  "EDUCATION": 1,
  "MARRIAGE": 2,
  "AGE": 45,
  "PAY_1": -1,
  "PAY_2": -1,
  "PAY_3": -1,
  "PAY_4": 0,
  "PAY_5": 0,
  "PAY_6": 0,
  "BILL_AMT1": 50000,
  "BILL_AMT2": 48000,
  "BILL_AMT3": 46000,
  "BILL_AMT4": 45000,
  "BILL_AMT5": 44000,
  "BILL_AMT6": 43000,
  "PAY_AMT1": 20000,
  "PAY_AMT2": 25000,
  "PAY_AMT3": 23000,
  "PAY_AMT4": 24000,
  "PAY_AMT5": 20000,
  "PAY_AMT6": 22000
}

```
## 🧾 Resposta esperada

```json
{
  "classe_predita": 0
}
```

- `0`: cliente **não inadimplente**
- `1`: cliente **inadimplente**

---

## 📁 Estrutura do Projeto

```
meu_projeto_api/
├── modelo/
│   └── gradient_boosting.joblib
├── main.py
├── requirements.txt
└── README.md
```

---

## 📄 Licença

Este projeto é apenas para fins educacionais.
