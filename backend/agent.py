from pydantic_ai import Agent
from models import DecisionOutput

agent = Agent(
    model="openai:meta-llama/llama-3-8b-instruct",
    output_type=DecisionOutput,
    system_prompt="""
You are a decision-making AI agent.

Follow a STACK-BASED reasoning approach:
1. Push pros
2. Push cons
3. Push constraints
4. Analyze items
5. Return a structured recommendation

Reject meaningless input.
Always return valid structured output.
"""
)



