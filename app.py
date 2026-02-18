from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from utils.crop_recommender import recommend_crop
from utils.crop_rotation import suggest_rotation
from utils.pest_disease_predictor import predict_pest_disease
from utils.feedback_handler import save_feedback, get_all_feedback
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure secret key
app.config['UPLOAD_FOLDER'] = 'static/uploads'

upload_folder = app.config['UPLOAD_FOLDER']
if os.path.exists(upload_folder) and os.path.isfile(upload_folder):
    os.remove(upload_folder)
os.makedirs(upload_folder, exist_ok=True)

# Simple in-memory user store: username -> password
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session['username'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('home'))
    error = 'Invalid username or password'
    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users:
        error = 'Username already exists'
        return render_template('signup.html', error=error)
    users[username] = password
    session['username'] = username
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

from utils.geo_tagging import recommend_crop_by_geotag

@app.route('/geo_tagging', methods=['GET', 'POST'])
def geo_tagging():
    if request.method == 'GET':
        return render_template('geo_tagging.html')
    try:
        latitude = float(request.form.get('latitude'))
        longitude = float(request.form.get('longitude'))
        terrain = request.form.get('terrain')
        result = recommend_crop_by_geotag(latitude, longitude, terrain)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Removed test_pest_disease_predictor route as per user request

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'GET':
        return render_template('crop_recommender.html')
    try:
        data = request.form
        result = recommend_crop(data)
        return jsonify({'recommended_crop': result['crop'], 'price_trend': result['price_trend']})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/rotate', methods=['GET', 'POST'])
def rotate():
    if request.method == 'GET':
        return render_template('crop_rotation.html')
    try:
        crop = request.form.get('current_crop')
        rotation = suggest_rotation(crop)
        return jsonify({'rotation': rotation})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict_pest', methods=['GET', 'POST'])
def predict_pest():
    if request.method == 'GET':
        return render_template('pest_disease_predictor.html')
    try:
        file = request.files['image']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)
        result = predict_pest_disease(path)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/test_dataset', methods=['GET'])
def test_dataset():
    from utils.pest_disease_predictor import load_dataset
    df = load_dataset()
    if df is not None:
        return jsonify({'dataset_loaded': True, 'num_records': len(df), 'columns': df.columns.tolist()})
    else:
        return jsonify({'dataset_loaded': False, 'message': 'Dataset not found'})

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'GET':
        return render_template('feedback.html')
    try:
        data = request.form
        save_feedback(data)
        return jsonify({'message': 'Feedback saved successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback_all', methods=['GET'])
def feedback_all():
    feedback = get_all_feedback()
    return jsonify(feedback)

@app.errorhandler(Exception)
def handle_exception(e):
    # Return JSON instead of HTML for unhandled exceptions
    response = {
        "error": str(e)
    }
    return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)
