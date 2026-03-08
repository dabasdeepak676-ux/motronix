# ai_engine/component_detector.py

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
        "pad",
        "abs",
        "stopping"
    ]

    engine_words = [
        "engine",
        "misfire",
        "power loss",
        "stall",
        "knocking",
        "rpm",
        "engine shaking"
    ]

    electrical_words = [
        "battery",
        "starter",
        "alternator",
        "fuse",
        "not starting",
        "no start",
        "relay",
        "sensor"
    ]

    cooling_words = [
        "overheat",
        "overheating",
        "coolant",
        "radiator",
        "temperature",
        "fan",
        "water pump"
    ]

    steering_words = [
        "steering",
        "alignment",
        "pulling",
        "steering vibration",
        "hard steering"
    ]

    ac_words = [
        "ac",
        "cooling",
        "compressor",
        "air conditioning",
        "blower",
        "weak cooling"
    ]

    fuel_words = [
        "fuel",
        "injector",
        "fuel pump",
        "fuel smell",
        "fuel pressure"
    ]

    transmission_words = [
        "gear",
        "gearbox",
        "shifting",
        "gear slipping",
        "clutch"
    ]

    suspension_words = [
        "shock",
        "suspension",
        "bump",
        "clunk",
        "wheel bearing",
        "cv joint"
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

    # fuel
    for word in fuel_words:
        if word in text:
            components.append("fuel")

    # transmission
    for word in transmission_words:
        if word in text:
            components.append("transmission")

    # suspension
    for word in suspension_words:
        if word in text:
            components.append("suspension")

    # remove duplicates
    components = list(set(components))

    return components