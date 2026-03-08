# ai_engine/symptom_weight_engine.py

SYMPTOM_WEIGHTS = {

    "misfire": {
        "spark plug": 22,
        "ignition coil": 20,
        "fuel injector": 16
    },

    "engine shaking": {
        "spark plug": 20,
        "ignition coil": 18,
        "fuel injector": 15,
        "engine mount": 5
    },

    "power loss": {
        "fuel injector": 15,
        "fuel pump": 12,
        "air filter": 8,
        "turbocharger": 10
    },

    "vibration while braking": {
        "brake disc": 30,
        "brake pad": 5
    },

    "brake vibration": {
        "brake disc": 30,
        "brake pad": 5
    },

    "squeaking brake": {
        "brake pad": 18
    },

    "hard steering": {
        "power steering": 20
    },

    "car not starting": {
        "battery": 20,
        "starter motor": 18,
        "alternator": 12
    }

}


def symptom_weight_score(problem_words):

    scores = {}

    # convert words list → sentence
    text = " ".join(problem_words)

    for symptom, components in SYMPTOM_WEIGHTS.items():

        if symptom in text:

            for comp, weight in components.items():

                scores[comp] = scores.get(comp, 0) + weight

    return scores