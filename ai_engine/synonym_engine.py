# ai_engine/synonym_engine.py

def expand_words(problem_text):

    text = problem_text.lower()

    synonyms = {

        "noise": [
            "sound",
            "squeak",
            "squeaking",
            "grinding"
        ],

        "brake": [
            "braking",
            "pedal",
            "disc",
            "rotor"
        ],

        "start": [
            "starting",
            "crank",
            "cranking"
        ],

        "engine": [
            "motor",
            "power"
        ],

        "overheat": [
            "temperature",
            "hot"
        ]

    }

    expanded_words = text.split()

    for word in text.split():

        if word in synonyms:
            expanded_words.extend(synonyms[word])

    return expanded_words