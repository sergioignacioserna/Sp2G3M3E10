from db.user_db import UserInDB
from db.user_db import update_user, get_user
from db.transaction_db import TransactionInDB
from db.transaction_db import save_transaction
from models.user_models import UserIn, UserOut
from models.transaction_models import TransactionIn, TransactionOut
import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):

    user_in_db = get_user(user_in.ID_empleado)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.Password != user_in.Password:
        return  {"Autenticado": False}

    return  {"Autenticado": True}


@api.get("/user/balance/{ID_empleado}")
async def get_balance(ID_empleado: str):

    user_in_db = get_user(ID_empleado)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out


@api.put("/user/transaction/")
async def make_transaction(transaction_in: TransactionIn):

    user_in_db = get_user(transaction_in.ID_empleado)

    if user_in_db != None:
        raise HTTPException(status_code=404, detail="El usuario ya existe")

    
    #update_user(user_in_db)

    transaction_in_db = TransactionInDB(**transaction_in.dict())
    transaction_in_db = save_transaction(transaction_in_db)

    transaction_out = TransactionOut(**transaction_in_db.dict())

    return  transaction_out
