# run file: python olofab_api_client.py
# pip install requests
import requests
import json

BASE_URL = "https://presqa.olofab.se/api"

# Part 1 - GET
def get_all_questions():
    print("\n Fetching all questions")
    url = f"{BASE_URL}/question"
    try:
        response = requests.get(url)
        response.raise_for_status()

        questions = response.json()
        print(f"Successfully fetched {len(questions)} questions.")
        
        if questions:
            print("First question details:")
            print(json.dump(questions[0], indent=2))
        return questions
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

all_questions = get_all_questions();

# Part 2 - POST
def create_question(question_text, answer_text):
    print(f"\n Creating a new question: '{question_text}'")
    url = f"{BASE_URL}/question"
    payload = {
        "question": question_text,
        "answer": answer_text
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        created_question = response.json()
        print("Successfully created question:")
        print(json.dumps(created_question, indent=2))
        return created_question
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

new_q_text = "Vad betyder dessa statuskoder? 100 – 199."
new_q_answer = ""
create_q_object = create_question(new_q_text, new_q_answer)

created_question_id = None
if create_q_object:
    created_question_id = create_q_object.get("id")
    print(f"ID of our new question: {created_question_id}")
    
# Part 3
def get_specific_question(question_id):
    if not question_id:
        print("No question ID provided to fetch.")
        return None
    print(f"\n Fetching question with ID: {question_id}")
    url = f"{BASE_URL}/question/{question_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        question = response.json()
        print("Successfully fecthed specific question:")
        print(json.dumps(question, indent=2))
        return question
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

if created_question_id:
    get_specific_question(created_question_id)
else:
    print("Skipping get_specific_question as no question was created successfylly")

# Part 4
def update_question(question_id, new_question_text=None, new_answer_text=None):
    if not question_id:
        print("No question ID provided to update.")
        return None
    
    print(f"\n Updating question ID {question_id} ")
    url = f"{BASE_URL}/question/{question_id}"

    payload = {}
    if new_question_text is not None:
        payload["question"] = new_question_text
        print(f"Setting new question text: '{new_question_text}'")
    if new_answer_text is not None:
        payload["answer"] = new_answer_text
        print(f"Setting new answer text: '{new_answer_text}")
    
    if not payload:
        print("No new data provided for update.")
        return None
    
    try:
        response = requests.put(url, json=payload)
        response.raise_for_status()

        updated_question = response.json()
        print("Successfully updated question:")
        print(json.dumps(updated_question, indent=2))
        return updated_question
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP erro occurred: {http_err} . {response.text}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None

if created_question_id:
    updated_q_text = "What is the main programming language used in FastAPI?"
    updated_q_answer = "Python"
    update_question(created_question_id, new_question_text=updated_q_text, new_answer_text=updated_q_answer)
    get_specific_question(created_question_id)
else:
    print("Skipping update_question as no question was created successfully")

# Part 5
def delete_question(question_id):
    if not question_id:
        print("No question ID provided to delete.")
        return None
    print(f"\n Deleting question with ID: {question_id}")
    url=f"{BASE_URL}/question/{question_id}"
    try:
        response = requests.delete(url)
        response.raise_for_status()

        if response.status_code == 200 and response.content:
            deleted_item_info = response.json()
            print("Successfully deleted question. API returned:")
            print(json.dumps(deleted_item_info, indent=2))
        else:
            print(f"Successfully initiated delete for question ID {question_id} (Status {response.status_code}).")
        return True
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.text}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return False

if created_question_id:
    delete_question(created_question_id)
    print("\nAttemptin to fetch the deleted question (should fail with 404):")
    get_specific_question(created_question_id)
else:
    print("Skipping delete_question as no question was created successfully.")
