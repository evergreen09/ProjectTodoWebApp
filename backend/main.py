from flask import request, jsonify
from config import app, db
from models import NoteData
import requests
from sqlalchemy import inspect, func
from datetime import datetime

@app.route('/save_note', methods=['POST'])
def save_note():
    note = request.json.get("noteData")

    if note is None:
        return jsonify({"Error": "Note is empty"}), 401

    note_data = NoteData(note=note)
    try:
        db.session.add(note_data)
        db.session.commit()
    except Exception as e:
        return jsonify({"Error": str(e)}), 400
    
    return jsonify({"message": "Note Saved"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)