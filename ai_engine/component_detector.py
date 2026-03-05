# component_detector.py

def detect_components(problem_text):

    text = problem_text.lower()

    components = []

    brake_words = [
        "brake",
        "braking",
        "pedal",
        "disc",
        "rotor",
        "caliper",
        "pad"
    ]

    engine_words = [
        "engine",
        "misfire",
        "power loss",
        "stall",
        "knocking"
    ]

    electrical_words = [
        "battery",
        "starter",
        "alternator",
        "fuse",
        "not starting",
        "no start"
    ]

    cooling_words = [
        "overheat",
        "coolant",
        "radiator",
        "temperature",
        "fan"
    ]

    steering_words = [
        "steering",
        "alignment",
        "pulling",
        "vibration"
    ]

    ac_words = [
        "ac",
        "cooling",
        "compressor",
        "air conditioning",
        "blower"
    ]

    # brake
    for word in brake_words:
        if word in text:
            components.append("brake")

    # engine
    for word in engine_words:
        if word in text:
            components.append("engine")

    # electrical
    for word in electrical_words:
        if word in text:
            components.append("electrical")

    # cooling
    for word in cooling_words:
        if word in text:
            components.append("cooling")

    # steering
    for word in steering_words:
        if word in text:
            components.append("steering")

    # AC
    for word in ac_words:
        if word in text:
            components.append("ac")

    return components