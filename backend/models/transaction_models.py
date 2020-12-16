from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    ID_empleado: str
    Nombre: str
    Apellido: str
    Correo_electronico: str
    Cargo: str
    Nivel_de_acceso: int
    Password: str

class TransactionOut(BaseModel):
    ID_empleado: str
    date: datetime
