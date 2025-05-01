from smolagents import CodeAgent, HfApiModel
from smolagents import tool
from huggingface_hub import list_models

from dotenv import load_dotenv

load_dotenv()

@tool
def model_download_tool(task: str) -> str:
  """
  This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
  It returns the name of the checkpoint.

  Args:
      task: The task for which to get the download count.
  """

 # TODO: 1 - Search for the most downloaded model for the given task / 2 - Sort the models by downloads, in descending order / 3 - Return the most downloaded model
  most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
  
  return most_downloaded_model.id

agent = CodeAgent(tools=[model_download_tool], model=HfApiModel())

model_id = agent.run(
  "Give me the most downloaded model for text-generation on the Hugging Face Hub." # ? Given task, text generation
)

print(model_id) # | Possible output: "TheBloke/phi-2-GGUF"