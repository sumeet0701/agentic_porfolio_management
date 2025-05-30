from agno.agent import Agent
from agentic_pm.components.config import *
from agno.models.groq import Groq
from agentic_pm.components.prompt import *
from agentic_pm.components.tools import *
from agentic_pm.components.instruction import *



planning_agent = Agent(
    name="planning_agent",
    description= prompt_for_planing_agents,
    model=groq_client,
    # tools=[data_collection_tool],
    role="Investment Policy statement generator",
    instructions= policy_agent_instruction,
    memory=MEMORY,
    storage= STORAGE
)

