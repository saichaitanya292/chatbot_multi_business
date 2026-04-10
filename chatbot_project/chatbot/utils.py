import pandas as pd
from sentence_transformers import SentenceTransformer, util
from .models import ChatbotData
import os

model = SentenceTransformer('all-MiniLM-L6-v2')


def load_latest_data():
    try:
        latest = ChatbotData.objects.last()

        if not latest:
            return [], []

        file_path = latest.file.path

        df = pd.read_excel(file_path)
        df.columns = df.columns.str.strip().str.lower()

        questions = df['question'].astype(str).tolist()
        answers = df['answer'].astype(str).tolist()

        return questions, answers

    except Exception as e:
        print("Error loading Excel:", e)
        return [], []


def get_bot_response(user_input):
    questions, answers = load_latest_data()

    if not questions:
        return "No data available. Please upload Excel in admin."

    question_embeddings = model.encode(questions, convert_to_tensor=True)
    user_embedding = model.encode(user_input, convert_to_tensor=True)

    similarities = util.cos_sim(user_embedding, question_embeddings)

    best_match_idx = similarities.argmax().item()
    best_score = similarities[0][best_match_idx].item()

    print("Score:", best_score)

    if best_score < 0.4:
        return "Sorry, I didn't understand."

    return answers[best_match_idx]