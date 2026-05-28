import time
from fastapi import FastAPI, HTTPException
from schemas import DNSRecordCreate, DNSRecordResponse

app = FastAPI(title="Servicio DNS RESTful")
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
    if time.time() > registro["expiracion"]:
        del db[nombre]
        raise HTTPException(status_code=404, detail="Not Found (Expired)")
    
    ttl_restante = int(registro["expiracion"] - time.time())
    return {"ip": registro["ip"], "ttl_restante": ttl_restante}
@app.patch("/dns/{nombre}", summary="Actualizar TTL")
def update_ttl(nombre: str, nuevo_ttl: int):
    if nombre not in db:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    db[nombre]["expiracion"] = time.time() + nuevo_ttl
    return {"message": "TTL actualizado"}

@app.delete("/dns/{nombre}", status_code=204, summary="Eliminar registro")
def delete_record(nombre: str):
    if nombre not in db:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    del db[nombre]
    return None
