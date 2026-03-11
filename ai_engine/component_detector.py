# ai_engine/component_detector.py

def detect_components(problem_text):

    text = problem_text.lower()

    COMPONENT_KEYWORDS = {

        "brake":[
            "brake","braking","pedal","disc","rotor","caliper",
            "pad","abs","stopping"
        ],

        "engine":[
            "engine","misfire","power loss","stall","knocking",
            "rpm","engine shaking","engine vibration"
        ],

        "electrical":[
            "battery","starter","alternator","fuse",
            "not starting","no start","relay","sensor"
        ],

        "cooling":[
            "overheat","overheating","coolant","radiator",
            "temperature","fan","water pump"
        ],

        "steering":[
"steering",
"alignment",
"pulling",
"car pulling",
"pulling to one side",
"vehicle pulling",
"steering vibration",
"hard steering"
],

        "ac":[
            "ac","cooling","compressor",
            "air conditioning","blower","weak cooling"
        ],

        "fuel":[
            "fuel","injector","fuel pump",
            "fuel smell","fuel pressure"
        ],

"transmission":[
    "gear",
    "gearbox",
    "shifting",
    "gear slipping",
    "clutch"
],
"suspension":[
    "shock",
    "suspension",
    "bump",
    "clunk",
    "wheel bearing",
    "cv joint",
    "car shaking",
    "shaking while driving",
    "vibration while driving",
    "vehicle vibration",
    "wheel vibration"
],

        "ev":[
            "ev","battery pack","charging",
            "range drop","electric motor"
        ],

        "hybrid":[
            "hybrid","regen braking","hybrid battery"
        ],

        "adas":[
            "lane assist","adaptive cruise",
            "collision warning","parking assist"
        ],

        "body":[
            "door","window","sunroof",
            "wiper","mirror","body noise"
        ]
    }

    detected = set()

    for component, keywords in COMPONENT_KEYWORDS.items():

        for word in keywords:

            if word in text:
                detected.add(component)
                break

    return list(detected)