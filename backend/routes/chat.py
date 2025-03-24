from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import Message
from extensions import db
import openai
import os
from dotenv import load_dotenv

load_dotenv()

bp = Blueprint('chat', __name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

@bp.route('/send', methods=['POST'])
@login_required
def send_message():
    data = request.get_json()
    user_message = data['message']
    
    # Save user message
    user_msg = Message(
        user_id=current_user.id,
        text=user_message,
        is_user=True
    )
    db.session.add(user_msg)
    
    # Generate AI response (for now, just echo the message)
    ai_response = f"Echo: {user_message}"
    
    # Save AI response
    ai_msg = Message(
        user_id=current_user.id,
        text=ai_response,
        is_user=False
    )
    db.session.add(ai_msg)
    db.session.commit()
    
    return jsonify({
        'user_message': user_message,
        'ai_response': ai_response
    })

@bp.route('/history')
@login_required
def get_history():
    messages = Message.query.filter_by(user_id=current_user.id).order_by(Message.timestamp).all()
    return jsonify([{
        'id': msg.id,
        'text': msg.text,
        'is_user': msg.is_user,
        'timestamp': msg.timestamp.isoformat()
    } for msg in messages]) 