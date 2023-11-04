from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import requests

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
        send_telegram(str(info));
        return {"info": info, "Autorization": Autorization}
    raise HTTPException(status_code = 401, detail="Unauthorized")

@app.post('/send_message/', tags=['Test']) 
async def send_message(info: TelegMessage, Autorization: str | None = Header(default=None)):
    if Autorization == "123": 
        answer = send_telegram(info.payload);
        return {"info": answer, "Autorization": Autorization}
    raise HTTPException(status_code = 401, detail="Unauthorized")

def send_telegram(payload: str): 
    user_id = 828170828
    url = "https://www.kunteynir.space/submitpayload?" + f"user_id={user_id}&payload={payload}"
    response = requests.get(url)
    return url
