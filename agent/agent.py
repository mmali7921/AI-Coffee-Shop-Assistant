from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from tools.menu_tool import show_menu


# Load environment variables
load_dotenv()

# Create the Groq model instance
groq_model = Groq(
    id="llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

# Create the agent with tools
agent = Agent(
    model=groq_model,
    tools=[show_menu]
)

# Call the agent
if __name__ == "__main__":
    agent.print_response("What coffees do you have?")
