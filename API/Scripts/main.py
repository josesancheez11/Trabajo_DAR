import time
from fastapi import FastAPI, HTTPException
from schemas import DNSRecordCreate, DNSRecordResponse

app = FastAPI(title="Servicio DNS RESTful")

# Persistencia en memoria
db = {}

@app.post("/dns", status_code=201, summary="Añadir registro")
def add_record(record: DNSRecordCreate):
    expiracion = time.time() + record.ttl
    db[record.nombre] = {"ip": record.ip, "expiracion": expiracion}
    return {"message": "Registro añadido"}

@app.get("/dns/{nombre}", response_model=DNSRecordResponse, summary="Resolver nombre")
def query_record(nombre: str):
    if nombre not in db:
        raise HTTPException(status_code=404, detail="Not Found")
    
    registro = db[nombre]
    # Lógica de expiración heredada de la Práctica 2
    if time.time() > registro["expiracion"]:
        del db[nombre]
        raise HTTPException(status_code=404, detail="Not Found (Expired)")
    
    ttl_restante = int(registro["expiracion"] - time.time())
    return {"ip": registro["ip"], "ttl_restante": ttl_restante}