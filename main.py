from generate_users import generate_user as gu
from SQL_ORM_API import save_users_data as save
from fastapi import FastAPI
import json

app = FastAPI()

@app.post('/api/{integer}')
async def response_question(integer: int):
    """  POST method takes integer for function.
    Function generate dictionary, then this dictionary saved in SQL,
    and return to user like JSON  """
    data = gu(integer)
    save(data)
    return json.dump(data)
