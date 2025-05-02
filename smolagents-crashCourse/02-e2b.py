from smolagents import CodeAgent, VisitWebpageTool, HfApiModel, E2BExecutor
from dotenv import load_dotenv

load_dotenv()

class DummyLogger:
    def log(self, message):
        print(f"[Agent Log] {message}")

agent = CodeAgent(
  tools=[VisitWebpageTool()],
  model=HfApiModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct"), # by default without params: Qwen/Qwen2.5-Coder-32B-Instruct 
  executor=E2BExecutor(logger=DummyLogger(), additional_imports=["requests", "markdownify"]),
  additional_authorized_imports=["requests", "markdownify"]
)

agent.run('What was Abraham Lincoln\'s preferred pet?')

# with open("agent_output.log", "w", encoding="utf-8") as f:
#     f.write(str(response))
