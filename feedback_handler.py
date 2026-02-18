import json
import os

FEEDBACK_FILE = 'feedback_data.json'

def save_feedback(data):
    feedback = {'name': data.get('name'), 'message': data.get('message')}
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, 'r') as f:
            all_feedback = json.load(f)
    else:
        all_feedback = []
    all_feedback.append(feedback)
    with open(FEEDBACK_FILE, 'w') as f:
        json.dump(all_feedback, f)

def get_all_feedback():
    if os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, 'r') as f:
            return json.load(f)
    return []
