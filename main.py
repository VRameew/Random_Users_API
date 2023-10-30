from generate_users import generate_user as gu
from SQL_ORM_API import save_users_data as save
from fastapi import FastAPI
import JSON

app = FastAPI()

@app.post('/api/{integer}')
async def response_question(integer: int):
    data = gu(integer)
    save(data)
    return json.dump(data)
