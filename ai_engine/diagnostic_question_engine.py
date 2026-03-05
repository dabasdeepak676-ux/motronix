# ai_engine/diagnostic_question_engine.py


def generate_questions(top_issue):

    questions = []

    issue = top_issue.lower()

    # brake related
    if "brake" in issue:

        questions.append({
            "question": "Does the noise happen only when braking?",
            "key": "brake_noise"
        })

        questions.append({
            "question": "Does the car vibrate when braking?",
            "key": "brake_vibration"
        })

    # starting related
    if "battery" in issue or "starter" in issue:

        questions.append({
            "question": "Do dashboard lights turn on when starting?",
            "key": "dashboard_lights"
        })

        questions.append({
            "question": "Do you hear a clicking sound while starting?",
            "key": "click_sound"
        })

    # overheating
    if "overheat" in issue or "coolant" in issue:

        questions.append({
            "question": "Does temperature rise in traffic?",
            "key": "traffic_overheat"
        })

        questions.append({
            "question": "Do you see coolant leakage?",
            "key": "coolant_leak"
        })

    return questions