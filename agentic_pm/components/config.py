import os, sys
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.memory.v2.memory import Memory
from agno.storage.mongodb import MongoDbStorage


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY", None)

# if GROQ_API_KEY is None:
#     raise ValueError("GROQ_API_KEY environment variable not set.")

# Initialize the Groq client with the provided API key
groq_client = Groq(
    id="llama-3.1-8b-instant",
    api_key="",
    )

## Memory configuration:
db_url = os.getenv("DB_URL", "mongodb://localhost:27017")
if db_url is None:
    raise ValueError("DB_URL environment variable not set.")

STORAGE = MongoDbStorage(
    db_url=db_url,
    collection_name="agentic_pm_collection",
)

MEMORY = Memory(
    db= STORAGE,
    debug_mode= True,
    model= groq_client,   
)


