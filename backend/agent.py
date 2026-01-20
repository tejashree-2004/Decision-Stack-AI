import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from models import DecisionOutput

load_dotenv()

model = OpenAIModel(
    model_name="meta-llama/llama-3-8b-instruct",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

agent = Agent(
    model=model,
    output_type=DecisionOutput,
    system_prompt="""
You are a decision-making AI agent.

Follow a STACK-BASED reasoning approach:
1. Push pros
2. Push cons
3. Push constraints
4. Analyze by popping items
5. Return a structured recommendation

Reject meaningless input.
Always return valid structured output.
"""
)


