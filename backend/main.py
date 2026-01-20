from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import DecisionInput, DecisionOutput
from service import make_decision

app = FastAPI(
    title="Decision Stack AI API",
    description="Backend API for stack-based AI decision making",
    version="1.0.0"
)

# ✅ CORS CONFIGURATION (THIS FIXES 405 OPTIONS ERROR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow frontend
    allow_credentials=True,
    allow_methods=["*"],        # allow OPTIONS, POST, GET
    allow_headers=["*"],        # allow all headers
)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Decision Stack AI backend is running"
    }

@app.post("/decide", response_model=DecisionOutput)
async def decide(data: DecisionInput):
    print("📥 Received data:", data)
    return await make_decision(data)
