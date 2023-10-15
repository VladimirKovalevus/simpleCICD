from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import requests

class GitInfo(BaseModel):
    owner: str
    payload: str
    status: bool

app = FastAPI(
    title = 'CI-CD'
)

@app.post('/git/', tags=['Git']) 
async def create_workspace(info: GitInfo, Autorization: str | None = Header(default=None)):
    if Autorization == "123": 
        send_telegram(str(info));
        return {"info": info, "Autorization": Autorization}
    raise HTTPException(status_code = 401, detail="Unauthorized")

def send_telegram(payload: str):
    url = "https://www.kunteynir.space/submitpayload"
    user_id = 828170828
    response = requests.get(url + "user_id={user_id}&payload={payload}")
