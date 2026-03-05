def detect_system(problem_text):

    text = problem_text.lower()

    braking_words = [
        "brake","braking","pedal","disc","rotor","caliper","abs"
    ]

    engine_words = [
        "engine","misfire","power loss","stall","smoke","knocking"
    ]

    electrical_words = [
        "battery","starter","alternator","fuse","not starting","no start"
    ]

    cooling_words = [
        "overheat","coolant","radiator","temperature","fan"
    ]

    steering_words = [
        "steering","alignment","pulling","vibration","suspension"
    ]

    ac_words = [
        "ac","cooling","compressor","air conditioning","blower"
    ]

    fuel_words = [
        "fuel","pump","injector"
    ]

    transmission_words = [
        "gear","clutch","transmission"
    ]

    for word in braking_words:
        if word in text:
            return "brake"

    for word in engine_words:
        if word in text:
            return "engine"

    for word in electrical_words:
        if word in text:
            return "electrical"

    for word in cooling_words:
        if word in text:
            return "cooling"

    for word in steering_words:
        if word in text:
            return "steering"

    for word in ac_words:
        if word in text:
            return "ac"

    for word in fuel_words:
        if word in text:
            return "fuel"

    for word in transmission_words:
        if word in text:
            return "transmission"

    return None