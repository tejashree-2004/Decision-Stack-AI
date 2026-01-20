from pydantic import BaseModel
from typing import List

class DecisionInput(BaseModel):
    problem: str
    pros: List[str] = []
    cons: List[str] = []
    constraints: List[str] = []

class DecisionOutput(BaseModel):
    recommendation: str
    reasoning_stack: List[str]
    risk_level: str
    confidence: float


