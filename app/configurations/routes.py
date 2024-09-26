from flask import Blueprint, jsonify
from app.configurations.model import Configurations

# Define a blueprint for the routes
configurations = Blueprint('configurations', __name__)

@configurations.route('/configurations', methods=['GET'])
def get_sessions():
    configurations = Configurations.query.all()
    return jsonify([configuration.to_dict() for configuration in configurations])