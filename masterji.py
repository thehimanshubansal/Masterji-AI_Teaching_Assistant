from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
import random
from google import genai


client = genai.Client(api_key="AIzaSyBpJg5IAB6iykrpg8di15wJ6tL8Bumvhtc")

app = FastAPI()

# Predefined examples and lessons for topics
EXAMPLES = {
    "math": "For example, 2 + 3 = 5.",
    "science": "For example, water boils at 100°C.",
    "history": "For example, World War II started in 1939."
}

SUMMARIES = {
    "math": "Math is the study of numbers, shapes, and patterns.",
    "science": "Science involves the study of the natural world, including physics, chemistry, and biology.",
    "history": "History is the study of past events, particularly in human affairs."
}

EXPLANATIONS = {
    "math": "Mathematics is an abstract science of number, quantity, and space, either as abstract concepts or as applied to other disciplines such as physics and engineering.",
    "science": "Science is the pursuit of knowledge and understanding of the natural and social world using systematic methods based on evidence.",
    "history": "History is the study of past events, particularly the human race's experiences, and it helps us understand how our past shapes the present."
}


# Predefined quiz questions and answers
QUIZ_QUESTIONS = [
    {"question": "Solve: 5x + 3 = 18. What is x?", "answer": "3"},
    {"question": "What is 15 divided by 3?", "answer": "5"},
    {"question": "What is the square root of 49?", "answer": "7"},
    {"question": "If a triangle has angles 60° and 60°, what is the third angle?", "answer": "60"},
    {"question": "What is 8 times 7?", "answer": "56"},
]

# Store the current quiz question and answer
current_quiz = {}


class DialogflowRequest(BaseModel):
    queryResult: Dict[str, Any]


@app.post("/webhook")
async def handle_dialogflow(request: DialogflowRequest):
    global current_quiz
    intent = request.queryResult["intent"]["displayName"]
    parameters = request.queryResult.get("parameters", {})
    topic = parameters.get("topic", "").lower()
    exinfo = parameters.get("extra_info", "").lower()
    person = parameters.get("person", None)
    
    if intent == "Generate_math_quiz":
        # Select a random quiz question
        quiz = random.choice(QUIZ_QUESTIONS)
        current_quiz["question"] = quiz["question"]
        current_quiz["answer"] = quiz["answer"]
        response_text = f"Here’s a math question for you: {quiz['question']}"

    elif intent == "Answer_Math_Quiz":
        user_answer = parameters.get("number", None)
        
        if not user_answer:
            response_text = "Please provide an answer."
        elif str(int(user_answer)).strip() == str(current_quiz.get("answer", "")).strip():
            response_text = "Correct! Well done! 🎉"
        else:
            response_text = f"Oops! The correct answer is {current_quiz.get('answer', 'unknown')}."
    
    elif intent == "Explain_Topic":
        response1 = client.models.generate_content(
            model="gemini-2.0-flash", contents=f"Explain the {topic} in 100-150 words. Also begin as Here's The explaination of {topic}"
        )
        response_text = response1.text
    
    elif intent == "Extra_info":
        response1 = client.models.generate_content(
            model="gemini-2.0-flash", contents=f"{exinfo}"
        )
        response_text = response1.text


    elif intent == "Identify_person":
        response1 = client.models.generate_content(
            model="gemini-2.0-flash", contents=f"Who is {person} in 100-150 words. Also begin as Here's the details about {person}"
        )
        response_text = response1.text

        # if topic and topic in EXPLANATIONS:
        #     response_text = f"Here's an explanation for {topic}: {EXPLANATIONS[topic]}"
        # else:
        #     response_text = f"Sorry, I don't have an explanation for {topic} right now."

    elif intent == "Give_Example":
        response1 = client.models.generate_content(
            model="gemini-2.0-flash", contents=f"Give two examples of {topic} in plain text. Also begin as Here’s an example of {topic}"
        )
        response_text = response1.text
        # if topic and topic in EXAMPLES:
        #     response_text = f"Here’s an example of {topic}: {EXAMPLES[topic]}"
        # else:
        #     response_text = f"Sorry, I don't have an example for {topic} right now."

    elif intent == "Summarize_Lesson":
        response1 = client.models.generate_content(
            model="gemini-2.0-flash", contents=f"Summarize the {topic} in 60-80 words. Also begin as Here’s a quick summary of {topic}"
        )
        response_text = response1.text
        # if topic and topic in SUMMARIES:
        #     response_text = f"Here’s a quick summary of {topic}: {SUMMARIES[topic]}"
        # else:
        #     response_text = f"Sorry, I don't have a summary for {topic} right now."

    else:
        response_text = "I'm still learning, ask me something else!"

    return {"fulfillmentText": response_text}
