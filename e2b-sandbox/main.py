
# $ This file allow you to start a E2B sandbox, remember to create a .env file with your E2B_API_KEY
from e2b_code_interpreter import Sandbox
from dotenv import load_dotenv
load_dotenv()

sbx = Sandbox() # By default the sandbox is alive for 5 minutes
execution = sbx.run_code("print('hello world')") # Execute Python inside the sandbox
print(execution.logs)

files = sbx.files.list("/")
print(files)
