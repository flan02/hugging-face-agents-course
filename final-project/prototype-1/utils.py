import requests

from src.final_assignment_template import DEFAULT_API_URL, SUBMIT_URL, QUESTIONS_URL
from src.final_assignment_template.datamodel import Question


def get_questions() -> list[Question]:
    """
    Fetches questions from the API.
    """
    response = requests.get(QUESTIONS_URL)
    return [Question(**question) for question in response.json()]


def get_file_by_task_id(task_id: str) -> bytes:
    """
    Fetches an image file from the API and returns its binary content.

    Args:
        task_id: The ID of the task to fetch the image for

    Returns:
        bytes: The binary content of the image
    """
    file_url = f"{DEFAULT_API_URL}/files/{task_id}"
    response = requests.get(file_url)
    return response.content


def view_image(image_bytes: bytes):
    """
    Displays an image in a Jupyter notebook.
    """
    from IPython.display import Image

    return Image(image_bytes)