from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {
        "matricula": "2024118ISINF0052",
        "nome": "CATARINA ALEXANDRA DE MOURA DANTAS"
    }