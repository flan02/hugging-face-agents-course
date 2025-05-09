from pydantic import BaseModel, Field


class Question(BaseModel):
    task_id: str = Field(description="The ID of the task")
    question: str = Field(description="The question to be answered")
    file_name: str = Field(description="The name of the file to be uploaded")
    Level: int = Field(description="The level of the question")

    def get_file(self):
        if self.file_name:
            from src.final_assignment_template.utils import get_file_by_task_id

            return get_file_by_task_id(self.task_id)
        else:
            return None