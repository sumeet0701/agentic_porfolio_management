import os, sys
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
load_dotenv()
GOROQ_API_KEY = os.getenv("GROQ_API_KEY")
if GOROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY environment variable not set.")

# Initialize the Groq client with the provided API key
groq_client = Groq(
    id="llama-3.1-8b-instant",
    api_key=GOROQ_API_KEY,
)
