def detect_system(problem_text):

    text = problem_text.lower()

    systems = {

        "brake":[
            "brake","braking","pedal","disc","rotor","caliper","abs","stopping"
        ],

        "engine":[
            "engine","misfire","stall","power loss","smoke","knocking","rpm","engine shaking"
        ],

        "electrical":[
            "battery","starter","alternator","fuse","relay","sensor","not starting","no start"
        ],

        "cooling":[
            "overheat","overheating","coolant","radiator","temperature","fan","water pump"
        ],

        "steering":[
            "steering","alignment","pulling","hard steering"
        ],

        "suspension":[
            "suspension","shock","bump","clunk","wheel bearing"
        ],

        "fuel":[
            "fuel","injector","fuel pump","fuel smell","fuel pressure"
        ],

        "transmission":[
            "gear","gearbox","shifting","clutch","gear slipping"
        ],

        "ac":[
            "ac","air conditioning","compressor","blower","weak cooling"
        ],

        "exhaust":[
            "exhaust","smoke","catalytic","dpf"
        ],

        "body":[
            "door","window","sunroof","lock","horn","wiper"
        ]

    }

    for system, words in systems.items():

        for word in words:

            if word in text:
                return system

    return None