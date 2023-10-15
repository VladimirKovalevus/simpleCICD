from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

class GitInfo(BaseModel):
    owner: str
    payplan: str
    status: bool

app = FastAPI(
    title = 'CI-CD'
)

@app.post('/git/', tags=['Git']) 
async def create_workspace(info: GitInfo, Autorization: str | None = Header(default=None)):
    if Autorization == "123": 
        return {"info": info, "Autorization": Autorization}
    raise HTTPException(status_code = 401, detail="Unauthorized")
