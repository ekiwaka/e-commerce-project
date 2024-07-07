from flask import Blueprint, request, jsonify
from utils.database import load_csv_to_db

data_bp = Blueprint('data', __name__)

@data_bp.route('/upload', methods=['POST'])
def upload_data():
    file = request.files.get('file')
    if file:
        file_path = f"./data/{file.filename}"
        file.save(file_path)
        load_csv_to_db(file_path)
        return jsonify({"message": "Data uploaded successfully"}), 200
    return jsonify({"error": "No file provided"}), 400
