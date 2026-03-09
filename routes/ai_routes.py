from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from datetime import datetime
from models.models import db
from google import genai
import os

# ================= BLUEPRINT =================

ai_bp = Blueprint("ai", __name__)


# ================= GEMINI CLIENT =================

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


# ================= AI ROUTE =================

@ai_bp.route("/ask-ai", methods=["POST"])
@login_required
def ask_ai():

    data = request.get_json()

    if not data:
        return jsonify({"reply": "Invalid request."})

    user_message = data.get("message")

    if not user_message:
        return jsonify({"reply": "Please explain your issue clearly."})

    today = datetime.utcnow().date()

    if not current_user.ai_last_reset or current_user.ai_last_reset.date() != today:
        current_user.ai_uses_today = 0
        current_user.ai_last_reset = datetime.utcnow()
        db.session.commit()

    if current_user.role != "premium" and current_user.ai_uses_today >= 5:
        return jsonify({"reply": "Free AI limit reached (5 per day)."})

    prompt = f"""
You are Motronix AI automotive expert.

User issue:
{user_message}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        reply = str(response.text).strip()

        current_user.ai_uses_today += 1
        db.session.commit()

        return jsonify({"reply": reply})

    except Exception as e:

        print("AI ERROR:", e)

        return jsonify({"reply": "AI temporarily unavailable."})