from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Carrega o modelo já treinado
modelo = joblib.load("modelo/gradient_boosting.joblib")

# Instancia a aplicação
app = FastAPI(title="API - Classificação de Clientes de Cartão de Crédito")

# Classe com os campos de entrada
class ClienteInput(BaseModel):
    LIMIT_BAL: float
    SEX: int
    EDUCATION: int
    MARRIAGE: int
    AGE: int
    PAY_1: float
    PAY_2: int
    PAY_3: int
    PAY_4: int
    PAY_5: int
    PAY_6: int
    BILL_AMT1: float
    BILL_AMT2: float
    BILL_AMT3: float
    BILL_AMT4: float
    BILL_AMT5: float
    BILL_AMT6: float
    PAY_AMT1: float
    PAY_AMT2: float
    PAY_AMT3: float
    PAY_AMT4: float
    PAY_AMT5: float
    PAY_AMT6: float

@app.post("/prever")
def prever_cliente(dados: ClienteInput):
    entrada = np.array([[ 
        dados.LIMIT_BAL, dados.SEX, dados.EDUCATION, dados.MARRIAGE, dados.AGE,
        dados.PAY_1, dados.PAY_2, dados.PAY_3, dados.PAY_4, dados.PAY_5, dados.PAY_6,
        dados.BILL_AMT1, dados.BILL_AMT2, dados.BILL_AMT3, dados.BILL_AMT4, dados.BILL_AMT5, dados.BILL_AMT6,
        dados.PAY_AMT1, dados.PAY_AMT2, dados.PAY_AMT3, dados.PAY_AMT4, dados.PAY_AMT5, dados.PAY_AMT6
    ]])

    predicao = modelo.predict(entrada)
    return {"classe_predita": int(predicao[0])}
