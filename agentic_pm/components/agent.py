from agno.agent import Agent
from agentic_pm.components.config import *
from agno.models.groq import Groq
from agentic_pm.components.prompt import *


planning_agent = Agent(
    name="planning_agent",
    description= prompt_for_planing_agents,
    model=groq_client,
    role="Investment Policy statement generator",
    instructions=dedent("""
1. You have to ask the User there Investment requirements and other things which are need to generate the IPS
""")
)

