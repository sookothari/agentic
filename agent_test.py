import openai
import os
"""
from langchain_community.llms import OpenAI
from langchain_community import LLMMath, ZeroShotReactDescriptionAgent
from langchain_community.utilities import GoogleSerperAPIWrapper
"""
from langchain.agents import initialize_agent
from langchain import hub
from langchain_openai import OpenAI
#from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
from dotenv import load_dotenv
load_dotenv(dotenv_path="../config/.env")
 
# loaded from .env file
#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
#os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

llm = OpenAI(temperature=0)
""""
math_tool = LLMMath(llm=llm)
search = GoogleSerperAPIWrapper()
agent = ZeroShotReactDescriptionAgent(
            tools=[google_search, math_tool], llm=llm, verbose=True
        )
"""
tools = load_tools(["google-serper", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
agent.run("Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?")
"""
prompt=hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt=prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
executor.invoke({"Input": "Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?"})
"""