from pydantic import BaseModel

class DNSRecordCreate(BaseModel):
    nombre: str
    ip: str
    ttl: int

class DNSRecordResponse(BaseModel):
    ip: str
    ttl_restante: int