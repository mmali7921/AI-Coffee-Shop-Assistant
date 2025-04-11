from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

groq_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are a cooffee shop assistant who know well about both customers' tastes and about the menu",
    markdown=True
)

groq_agent.print_response("HIi, Suggest me a drink for the moment")