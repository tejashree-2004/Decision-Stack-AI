from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import DecisionInput, DecisionOutput
from service import make_decision

app = FastAPI(
    title="Decision Stack AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/decide", response_model=DecisionOutput)
async def decide(data: DecisionInput):
    return await make_decision(data)

