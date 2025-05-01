from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(
  tools=[DuckDuckGoSearchTool()],
  model=HfApiModel() # by default: Qwen/Qwen2.5-Coder-32B-Instruct 
)

agent.run("How long would it take for an elephant to cross the United States from Florida to California?")
# ? Out - Final answer: It would take approximately 30.87 days for an elephant to cross the United States from Florida to California.
