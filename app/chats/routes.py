from flask import Blueprint, jsonify
from app.chats.model import Chats

# Define a blueprint for the routes
chats = Blueprint('chats', __name__)

@chats.route('/chats', methods=['GET'])
def get_sessions():
    chats = Chats.query.all()
    return jsonify([chat.to_dict() for chat in chats])