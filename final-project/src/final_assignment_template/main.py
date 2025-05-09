from src.final_assignment_template.agent import MyAgent
from src.final_assignment_template.utils import get_questions
from src.final_assignment_template.utils import print_answers
from src.final_assignment_template import SUBMIT_URL
import requests


def submit_answers(questions, answers):
    """ 
    Send the answers to the benchmark evaluation API.
    """
    payload = [
        {
            "task_id": question.task_id,
            "answer": answer,
        }
        for question, answer in zip(questions, answers)
    ]
    response = requests.post(SUBMIT_URL, json=payload)

    if response.status_code == 200:
        print("🐱‍🐉 Answers submitted successfully.")
        print(response.json()) # This will show the evaluation result
    else:
        print(f"❌ Failed to submit answers {response.status_code}")
        print(response.text)

  
def main():
    """ 
    Main function to run the agent and submit answers.
    """
    print("🐱‍👤 Fetching questions...")
    questions = get_questions()

    print("🤖 Running agent on all questions...")
    agent = MyAgent()
    answers = agent.run_on_all_questions(questions)

    print_answers(questions, answers) # Only for testing purposes
    # print("📤 Submitting answers...")
    # submit_answers(questions, answers)
    # print("✅ Done!")

if __name__ == "__main__":
    main()

# Run the script -> /Documents/VSCode Projects/python/hugging-face-agents-course/final-project
# | PYTHONIOENCODING=utf-8 py -m src.final_assignment_template.main

# Public API
# | https://agents-course-unit4-scoring.hf.space/docs