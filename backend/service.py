from agent import agent
from models import DecisionInput, DecisionOutput


def is_meaningful(text: str) -> bool:
    return len(text.split()) >= 3


async def make_decision(data: DecisionInput) -> DecisionOutput:
    # ✅ Backend semantic guard
    if not is_meaningful(data.problem):
        return DecisionOutput(
            recommendation="Please provide a clearer and more meaningful decision description.",
            reasoning_stack=[
                "Input validation failed",
                "Decision description too short or unclear"
            ],
            risk_level="High",
            confidence=0.0
        )

    try:
        response = await agent.run(
            f"""
Decision Problem:
{data.problem}

Pros:
{data.pros}

Cons:
{data.cons}

Constraints:
{data.constraints}
"""
        )
        return response.data

    except Exception as e:
        print("⚠️ AI error, using fallback:", e)

        return DecisionOutput(
            recommendation="Unable to analyze this decision meaningfully. Please add more context.",
            reasoning_stack=[
                "Fallback triggered",
                "Insufficient context detected"
            ],
            risk_level="High",
            confidence=0.2
        )
