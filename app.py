from fastapi import FastAPI
from pydantic import BaseModel

from agent import run_agent

app = FastAPI()


class UserRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: UserRequest):

    result = run_agent(request.message)

    return result