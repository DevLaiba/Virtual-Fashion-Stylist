from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils import detect_age_gender, estimate_measurements
from recommender import get_recommendations
from tryon import simulate_tryon

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    age_group, gender = detect_age_gender(filepath)
    measurements = estimate_measurements(filepath)
    outfits = get_recommendations(gender, age_group, measurements)

    return jsonify({
        'age': age_group,
        'gender': gender,
        'measurements': measurements,
        'outfits': outfits,
        'image_path': filepath
    })

@app.route('/tryon', methods=['POST'])
def tryon():
    data = request.get_json()
    user_img = data.get('image_path')
    outfit_id = data.get('outfit_id')

    result_path = simulate_tryon(user_img, outfit_id)
    return jsonify({'result_image': result_path})

if __name__ == '__main__':
    app.run(debug=True)
