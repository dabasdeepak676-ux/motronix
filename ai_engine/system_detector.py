def detect_system(problem_text):

    text = problem_text.lower()

    systems = {
        "brake": ["brake","braking","pedal","disc","rotor","caliper","abs"],
        "engine": ["engine","misfire","stall","power loss","smoke","knocking"],
        "electrical": ["battery","starter","alternator","fuse","not starting","no start"],
        "cooling": ["overheat","coolant","radiator","temperature","fan"],
        "steering": ["steering","alignment","pulling","vibration","suspension"],
        "ac": ["ac","cooling","compressor","air conditioning","blower"]
    }

    for system, words in systems.items():

        for word in words:

            if word in text:
                return system

    return None