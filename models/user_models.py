from pydantic import BaseModel

class UserIn(BaseModel):
    ID_empleado: str
    Password: str

class UserOut(BaseModel):
    ID_empleado: str
    Correo_electronico: str
    Password: str
