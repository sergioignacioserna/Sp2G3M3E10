from typing import  Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    ID_empleado: str
    Nombre: str
    Apellido: str
    Correo_electronico: str
    Cargo: str
    Nivel_de_acceso: int
    Password: str

database_users = Dict[str, UserInDB]

database_users = {
    "98269478": UserInDB(**{"ID_empleado":"98269478",
                          "Nombre":"Jhonatan",
                          "Apellido":"Mora",
                          "Correo_electronico":"jh.mo@myfact.com",
                          "Cargo":"Operario",
                          "Nivel_de_acceso":0,
                          "Password":"MyPassJM8"}),
    
    "1018369421": UserInDB(**{"ID_empleado":"1018369421",
                          "Nombre":"Martha",
                          "Apellido":"Mendoza",
                          "Correo_electronico":"ma.me@myfact.com",
                          "Cargo":"Secretaria",
                          "Nivel_de_acceso":1,
                          "Password":"MyPassMM1"}),
    
    "43698527": UserInDB(**{"ID_empleado":"43698527",
                          "Nombre":"Catalina",
                          "Apellido":"Berrio",
                          "Correo_electronico":"ca.be@myfact.com",
                          "Cargo":"Gerente Oficina",
                          "Nivel_de_acceso":2,
                          "Password":"MyPassCB7"}),
    
    "71529641": UserInDB(**{"ID_empleado":"71529641",
                          "Nombre":"Carlos",
                          "Apellido":"Posada",
                          "Correo_electronico":"ca.po@myfact.com",
                          "Cargo":"Gerente General",
                          "Nivel_de_acceso":3,
                          "Password":"MyPassCP1"}),
    
    "1012369854": UserInDB(**{"ID_empleado":"1012369854",
                          "Nombre":"Carolina",
                          "Apellido":"Zapata",
                          "Correo_electronico":"ca.za@myfact.com",
                          "Cargo":"Directora Personal",
                          "Nivel_de_acceso":2,
                          "Password":"MyPassCZ4"}),
    
    "98200360": UserInDB(**{"ID_empleado":"98200360",
                          "Nombre":"Mario",
                          "Apellido":"Escobar",
                          "Correo_electronico":"ma.es@myfact.com",
                          "Cargo":"Analista",
                          "Nivel_de_acceso":1,
                          "Password":"MyPassME0"}),

}

def get_user(ID_empleado: str):
    if ID_empleado in database_users.keys():
        return database_users[ID_empleado]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.ID_empleado] = user_in_db
    return user_in_db
