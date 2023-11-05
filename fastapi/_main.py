from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import requests
#from sqlalchemy import create_engine

class GitInfo(BaseModel):
    owner: str
    payload: str
    status: bool

class TelegMessage(BaseModel):
    #user_id: Optional[int] = None
    payload: str

app = FastAPI(
    title = 'CI-CD'
)

@app.post('/git/', tags=['Git']) 
async def git_check(info: GitInfo, Autorization: str | None = Header(default=None)):
    if Autorization == "123": 
        send_telegram(info.payload);
        return {"info": "ну и что мы тут забыли -_-"}
    raise HTTPException(status_code = 401, detail="Unauthorized")

@app.post('/send_message/', tags=['Test']) 
async def send_message(info: TelegMessage, Autorization: str | None = Header(default=None)):
    if Autorization == "123": 
        send_telegram(info.payload);
        return {"info": "ну и что мы тут забыли -_-"}
    raise HTTPException(status_code = 401, detail="Unauthorized")

#@app.get('/git/history/', tags=['Git / Data'])
#async def git_history(date: str, Autorization: str | None = Header(default=None)):
#    if Autorization == "123":
#        answer = get_history(date)
#        send_telegram(answer)
#        return {"info": true, "Autorization": Autorization}
#    raise HTTPException(status_code = 401, detail="Unauthorized")
    

def send_telegram(payload: str): 
    user_id = 828170828
    url = "https://www.kunteynir.space/submitpayload?" + f"user_id={user_id}&payload={payload}"
    response = requests.get(url)
    return url

#def get_history(date: str):
#    db_params = {
#        "drivername": "postgresql",
#        "username": "user",
#        "password": "123",
#        "host": "localhost",
#        "port": 5432,
#        "database": "data"
#    }
#    conn_string = f'{db_params["drivername"]}://{db_params["username"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}'
#    engine = create_engine(conn_string)
#    conn = engine.connect()
#    selection = conn.execute("SELECT * FROM git_history")
#    conn.close()
#    return str(selection)
