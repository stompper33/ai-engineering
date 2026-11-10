from pydantic import BaseModel, Field
from agents import Agent
from dotenv import load_dotenv
import os

load_dotenv(override=True)
MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gpt-5.4-mini")
CLARIFICATION_QUESTIONS = int(os.getenv("CLARIFICATION_QUESTIONS", 3))

INSTRUCTIONS = f"""
You are a research assistant that helps with clarifying a user's query. 
Given a query analyze it and come up with {CLARIFICATION_QUESTIONS} additional clarification questions based on the query. 
These questions remove confusion, fill in missing gaps, and help get a better understanding of the original question. 
"""

class Clarifications(BaseModel):
    follow_up_questions: list[str] = Field(description="Clarifying questions to ask the user about their query")


clarification_agent = Agent(name="Clarification Agent", instructions=INSTRUCTIONS, model=MODEL_NAME, output_type=Clarifications)
