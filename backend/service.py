from agent import agent
from models import DecisionInput, DecisionOutput

def is_meaningful(text: str) -> bool:
    return len(text.split()) >= 3

async def make_decision(data: DecisionInput) -> DecisionOutput:
    if not is_meaningful(data.problem):
        return DecisionOutput(
            recommendation="Please provide a clearer decision description.",
            reasoning_stack=["Input validation failed"],
            risk_level="High",
            confidence=0.0
        )

    try:
        result = await agent.run(f"""
Decision:
{data.problem}

Pros:
{data.pros}

Cons:
{data.cons}

Constraints:
{data.constraints}
""")
        return result.data

    except Exception:
        return DecisionOutput(
            recommendation="Unable to analyze. Please add more context.",
            reasoning_stack=["Fallback triggered"],
            risk_level="High",
            confidence=0.2
        )
