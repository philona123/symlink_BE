from flask import Blueprint, jsonify
from app.messages.model import Messages

# Define a blueprint for the routes
messages = Blueprint('messages', __name__)

@messages.route('/messages', methods=['GET'])
def get_sessions():
    messages = Messages.query.all()
    return jsonify([message.to_dict() for message in messages])