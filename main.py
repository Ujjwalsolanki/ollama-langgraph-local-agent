from langchain_ollama import OllamaLLM
from langchain.agents import AgentExecutor
from langchain.agents import create_react_agent
from langchain_core.prompts import PromptTemplate
from tools import get_current_time, calculate


# 1. Define the LLM and the tools
llm = OllamaLLM(model="llama3.1")
tools = [get_current_time, calculate]

# 2. Create the Prompt Template for the agent
# This prompt guides the LLM on how to reason and use the tools.
prompt_template = """
You are a helpful assistant. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(prompt_template)

# 3. Create the ReAct agent
# This combines the LLM, tools, and prompt to create a runnable agent.
agent = create_react_agent(llm, tools, prompt)

# 4. Create the Agent Executor
# This is the main runnable object that will execute the agent's decisions.
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 5. Run the agent with a sample query
# You can replace this with a user input loop.
if __name__ == "__main__":
    result = agent_executor.invoke({"input": "What is 50 multiplied by 5?"})
    print(f"\nFinal Result: {result['output']}")

    result = agent_executor.invoke({"input": "What is the current time in New York?"})
    print(f"\nFinal Result: {result['output']}")