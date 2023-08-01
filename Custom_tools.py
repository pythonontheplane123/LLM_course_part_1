import os

os.environ["LANGCHAIN_TRACING"] = "true"

from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

def multiplier(a, b):
    return a / b


def parsing_multiplier(string):
    a, b = string.split(",")
    return multiplier(int(a), int(b))

llm = OpenAI(temperature=0)
tools = [
    Tool(
        name="Multiplier",
        func=parsing_multiplier,
        description="useful for when you need to multiply two numbers together. The input to this tool should be a comma separated list of numbers of length two, representing the two numbers you want to multiply together. For example, `1,2` would be the input if you wanted to multiply 1 by 2.",
    )
]
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run("3 times four?")
