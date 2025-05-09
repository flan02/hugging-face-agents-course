import io
from typing import List
from agno.tools.tavily import TavilyTools
import pandas as pd
from agno.agent import Agent
from agno.media import Image
from agno.models.openai import OpenAIChat
from agno.tools.arxiv import ArxivTools
from agno.tools.calculator import CalculatorTools
#from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools
from agno.tools.youtube import YouTubeTools
from openai import OpenAI
from src.final_assignment_template.datamodel import Question

from dotenv import load_dotenv
load_dotenv()




def transcribe_audio(audio_bytes: bytes) -> str:
    client = OpenAI()
    audio_file = io.BytesIO(audio_bytes)
    audio_file.name = "audio.mp3"  # Set a name attribute if needed by OpenAI

    transcription = client.audio.transcriptions.create(
        model="gpt-4o-transcribe", file=audio_file
    )
    return transcription.text


class MyAgent:
    def __init__(self, model_name: str = "gpt-4o"): # gpt-3.5-turbo | gpt-4o | gpt2 (huggingface)
        # text_generator = pipeline("text-generation", model=model_name)
        # self.model = text_generator.model 
        self.model = OpenAIChat(id=model_name)
        self._agent = Agent(
            model=self.model,
            instructions="""\
Perform all the necessary tool calls to answer the question.
Answer with ONLY the final ansewr, no other text or comment is needed as your results will be evaluated with an exact match.
""",
            tools=[
                WikipediaTools(),
                CalculatorTools(enable_all=True),
                YouTubeTools(),
                # DuckDuckGoTools(),
                TavilyTools(),
                ArxivTools(),
            ],
        )

    def _run_with_image(self, question: Question) -> str:
        image = Image(content=question.get_file())
        result = self._agent.run(question.question, images=[image])
        return result if isinstance(result, str) else "No output generated"

    def _run_with_audio(self, question: Question) -> str:
        audio_bytes = question.get_file()
        if audio_bytes is None:
            return "Error: No audio file provided."
        transcription = transcribe_audio(audio_bytes)
        updated_question = (question.question + f"\n\nComplete Audio Transcription: {transcription}")
        result = self._agent.run(updated_question)
        return result if isinstance(result, str) else "No output generated"

    def _run_with_excel(self, question: Question) -> str:
        excel_data = pd.read_excel(question.get_file())
        # add the excel data to the question as a table
        updated_question = (
            question.question + f"\n\nExcel Data: {excel_data.to_markdown()}"
        )
        result = self._agent.run(updated_question)
        return result if isinstance(result, str) else "No output generated"
    
    def _run_with_code(self, question: Question) -> str:
        code = question.get_file()
        updated_question = question.question + f"\n\nComplete Code: {code}"
        result = self._agent.run(updated_question)
        return result if isinstance(result, str) else "No output generated"

    def __call__(self, question: Question) -> str:
        if not question.file_name:
            result = self._agent.run(question.question)
            return result if isinstance(result, str) else "No output generated"
        else:
            # check if the file is an image
            if (
                question.file_name.endswith(".png")
                or question.file_name.endswith(".jpg")
                or question.file_name.endswith(".jpeg")
            ):
                return self._run_with_image(question)
            elif question.file_name.endswith(".mp3") or question.file_name.endswith(
                ".wav"
            ):
                return self._run_with_audio(question)
            elif question.file_name.endswith(".py"):
                return self._run_with_code(question)
            elif question.file_name.endswith(".xlsx"):
                return self._run_with_excel(question)
            else:
                raise ValueError(f"Unsupported file type: {question.file_name}")

    def __str__(self) -> str:
        result = self._agent.instructions
        return result if isinstance(result, str) else "No output generated"

    def run_on_all_questions(self, questions: List[Question]) -> List[str]:
        return [self(question) for question in questions]