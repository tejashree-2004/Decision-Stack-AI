from pydantic import BaseModel, Field
from typing import List
class DecisionInput(BaseModel):
    problem: str
    pros: List[str] = []
    cons: List[str] = []
    constraints: List[str] = []
class DecisionOutput(BaseModel):
    recommendation: str = Field(description="Final decision suggestion")
    reasoning_stack: List[str] = Field(description="Step-by-step stack reasoning")
    risk_level: str = Field(description="Low / Medium / High")
    confidence: float = Field(ge=0, le=1)

