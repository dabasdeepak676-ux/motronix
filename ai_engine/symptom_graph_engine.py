def expand_words(problem_text):

    text = problem_text.lower()

    synonyms = {

        "noise": [
            "sound",
            "squeak",
            "squeaking",
            "grinding",
            "rubbing"
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
            "cranking",
            "ignition"
        ],

        "overheat": [
            "temperature",
            "hot",
            "heating"
        ],

        "engine": [
            "motor",
            "power"
        ]

    }

    expanded_words = text.split()

    for word in text.split():

        if word in synonyms:

            expanded_words.extend(synonyms[word])

    return expanded_words