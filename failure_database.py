# failure_database.py

FAILURE_DATABASE = [

# ================= ENGINE =================

{
"id":1,
"problem":"Spark Plug Worn",
"system":"engine",
"component":"spark plug",
"severity":"medium",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"engine misfire",
"engine vibration",
"poor fuel economy",
"difficulty starting"
],
"user_checks":[
"check if engine struggles to start"
],
"repair_cost":{"min":1000,"max":4000}
},

{
"id":2,
"problem":"Ignition Coil Failure",
"system":"engine",
"component":"ignition coil",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine misfire",
"loss of power",
"check engine light"
],
"user_checks":[
"check if engine shakes during acceleration"
],
"repair_cost":{"min":2000,"max":8000}
},

{
"id":3,
"problem":"Fuel Injector Clogged",
"system":"fuel",
"component":"fuel injector",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine misfire",
"loss of power",
"poor fuel economy"
],
"user_checks":[
"check if engine misfires during acceleration"
],
"repair_cost":{"min":2500,"max":7000}
},

{
"id":4,
"problem":"Clogged Air Filter",
"system":"engine",
"component":"air intake",
"severity":"low",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"poor acceleration",
"loss of power",
"reduced mileage"
],
"user_checks":[
"inspect air filter condition"
],
"repair_cost":{"min":300,"max":1500}
},

{
"id":5,
"problem":"Dirty Throttle Body",
"system":"engine",
"component":"throttle body",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"rough idle",
"engine hesitation",
"engine stalls"
],
"user_checks":[
"observe unstable idle RPM"
],
"repair_cost":{"min":1500,"max":4000}
},

{
"id":6,
"problem":"Engine Mount Worn",
"system":"engine",
"component":"engine mount",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine vibration",
"thud sound during acceleration"
],
"user_checks":[
"observe engine movement while revving"
],
"repair_cost":{"min":3000,"max":10000}
},

{
"id":7,
"problem":"Timing Chain Wear",
"system":"engine",
"component":"timing chain",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"rattling noise from engine",
"engine noise at startup"
],
"user_checks":[
"listen for rattling sound during cold start"
],
"repair_cost":{"min":8000,"max":25000}
},

{
"id":8,
"problem":"Engine Vacuum Leak",
"system":"engine",
"component":"vacuum system",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"rough idle",
"high idle RPM"
],
"user_checks":[
"listen for hissing sound"
],
"repair_cost":{"min":1500,"max":8000}
},

{
"id":9,
"problem":"MAF Sensor Fault",
"system":"engine",
"component":"maf sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine hesitation",
"poor acceleration"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":3000,"max":9000}
},

{
"id":10,
"problem":"Oxygen Sensor Fault",
"system":"engine",
"component":"oxygen sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"check engine light",
"poor fuel economy"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":3000,"max":9000}
},

# ================= COOLING =================

{
"id":11,
"problem":"Low Coolant Level",
"system":"cooling",
"component":"coolant system",
"severity":"medium",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"engine overheating",
"overheating",
"engine temperature high",
"coolant warning light"
],
"user_checks":[
"check coolant reservoir level"
],
"repair_cost":{"min":500,"max":3000}
},

{

"id":12,
"problem":"Radiator Fan Failure",
"system":"cooling",
"component":"radiator fan",
"severity":"high",
"urgency":"repair_immediately",
"probability":7,

"symptoms":[
"engine overheating",
"temperature high",
"fan not running"
],

"possible_causes":[
"fan motor failure",
"fan relay fault",
"wiring issue"
],

"estimated_cost":{
"min":2500,
"max":8000
},

"user_checks":[
"check if radiator fan turns on when engine is hot",
"listen for fan noise near radiator"
]
},

{
"id":13,
"problem":"Radiator Blocked",
"system":"cooling",
"component":"radiator",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine overheating",
"coolant temperature high"
],
"user_checks":[
"inspect radiator fins"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":14,
"problem":"Thermostat Stuck Closed",
"system":"cooling",
"component":"thermostat",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine overheating quickly"
],
"user_checks":[
"observe temperature rise"
],
"repair_cost":{"min":2000,"max":6000}
},

{
"id":15,
"problem":"Water Pump Failure",
"system":"cooling",
"component":"water pump",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"coolant leak",
"engine overheating"
],
"user_checks":[
"check coolant leak near pump"
],
"repair_cost":{"min":4000,"max":15000}
},

# ================= BRAKES =================

{
"id":16,
"problem":"Brake Pad Wear",
"system":"brake",
"component":"brake pads",
"severity":"medium",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"squeaking while braking",
"reduced braking power"
],
"user_checks":[
"listen for brake noise"
],
"repair_cost":{"min":2500,"max":7000}
},

{
"id":17,
"problem":"Brake Disc Warped",
"system":"brake",
"component":"brake disc",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"vibration while braking"
],
"user_checks":[
"check steering vibration"
],
"repair_cost":{"min":4000,"max":12000}
},

{
"id":18,
"problem":"Brake Fluid Low",
"system":"brake",
"component":"brake fluid",
"severity":"high",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"soft brake pedal",
"brake warning light"
],
"user_checks":[
"check brake fluid level"
],
"repair_cost":{"min":500,"max":3000}
},

{
"id":19,
"problem":"Brake Caliper Stuck",
"system":"brake",
"component":"brake caliper",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"car pulling to one side while braking"
],
"user_checks":[
"check wheel heat after driving"
],
"repair_cost":{"min":3000,"max":10000}
},

{
"id":20,
"problem":"ABS Sensor Fault",
"system":"brake",
"component":"abs sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"ABS warning light"
],
"user_checks":[
"scan ABS codes"
],
"repair_cost":{"min":2500,"max":9000}
},

# ================= SUSPENSION =================

{
"id":21,
"problem":"Wheel Bearing Failure",
"system":"suspension",
"component":"wheel bearing",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"humming noise while driving"
],
"user_checks":[
"listen for wheel noise"
],
"repair_cost":{"min":3000,"max":10000}
},

{
"id":22,
"problem":"Shock Absorber Worn",
"system":"suspension",
"component":"shock absorber",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"car bouncing after bumps"
],
"user_checks":[
"perform bounce test"
],
"repair_cost":{"min":4000,"max":15000}
},

{
"id":23,
"problem":"Suspension Bush Wear",
"system":"suspension",
"component":"suspension bush",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"clunk noise on bumps"
],
"user_checks":[
"inspect bushings"
],
"repair_cost":{"min":1500,"max":6000}
},

{
"id":24,
"problem":"Wheel Alignment Incorrect",
"system":"steering",
"component":"wheel alignment",
"severity":"low",
"urgency":"service_soon",
"probability":7,
"symptoms":[
"car pulling to one side",
"vehicle pulling left",
"vehicle pulling right",
"steering off center",
"uneven tire wear"
],
"user_checks":[
"observe straight road behavior"
],
"repair_cost":{"min":800,"max":2500}
},

{
"id":25,
"problem":"Tire Pressure Low",
"system":"suspension",
"component":"tire",
"severity":"low",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"vehicle pulling",
"tire pressure warning"
],
"user_checks":[
"check tire pressure"
],
"repair_cost":{"min":0,"max":500}
},

# ================= ELECTRICAL =================

{
"id":26,
"problem":"Battery Weak",
"system":"electrical",
"component":"battery",
"severity":"medium",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"slow engine cranking",
"dim headlights",
"battery warning light"
],
"user_checks":[
"check battery voltage"
],
"repair_cost":{"min":3000,"max":8000}
},

{
"id":27,
"problem":"Alternator Failure",
"system":"electrical",
"component":"alternator",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"battery warning light",
"battery draining quickly",
"electrical systems malfunction"
],
"user_checks":[
"check battery voltage while engine running"
],
"repair_cost":{"min":5000,"max":15000}
},

{
"id":28,
"problem":"Starter Motor Failure",
"system":"electrical",
"component":"starter motor",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine not cranking",
"clicking sound when starting"
],
"user_checks":[
"listen for clicking sound during ignition"
],
"repair_cost":{"min":4000,"max":12000}
},

{
"id":29,
"problem":"Loose Battery Terminal",
"system":"electrical",
"component":"battery terminal",
"severity":"low",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"car not starting",
"dashboard flickering"
],
"user_checks":[
"inspect battery terminals"
],
"repair_cost":{"min":200,"max":800}
},

{
"id":30,
"problem":"Fuse Blown",
"system":"electrical",
"component":"fuse",
"severity":"low",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"electrical component not working",
"power loss in system"
],
"user_checks":[
"inspect fuse box"
],
"repair_cost":{"min":100,"max":500}
},

# ================= TRANSMISSION =================

{
"id":31,
"problem":"Clutch Plate Worn",
"system":"transmission",
"component":"clutch plate",
"severity":"high",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"engine revs high but speed not increasing",
"burning smell from clutch"
"gear not shifting properly",
"hard gear shift"
],
"user_checks":[
"observe RPM increase without speed increase"
],
"repair_cost":{"min":6000,"max":20000}
},

{
"id":32,
"problem":"Clutch Cable Loose",
"system":"transmission",
"component":"clutch cable",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"clutch pedal feels loose",
"gear shifting difficult"
],
"user_checks":[
"check clutch pedal free play"
],
"repair_cost":{"min":800,"max":3000}
},

{
"id":33,
"problem":"Gearbox Oil Low",
"system":"transmission",
"component":"gearbox",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"gear hard to shift",
"gearbox noise"
"gear not shifting properly",
"hard gear shift"
],
"user_checks":[
"check gearbox oil level"
],
"repair_cost":{"min":800,"max":4000}
},

{
"id":34,
"problem":"Gear Synchronizer Wear",
"system":"transmission",
"component":"gear synchronizer",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"gear hard to shift",
"gearbox noise"
"gear not shifting properly",
"hard gear shift"
],
"user_checks":[
"check if grinding occurs while shifting"
],
"repair_cost":{"min":10000,"max":35000}
},

{
"id":35,
"problem":"Transmission Fluid Low",
"system":"transmission",
"component":"transmission fluid",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"gear slipping",
"delayed gear shifts"
],
"user_checks":[
"check transmission fluid level"
],
"repair_cost":{"min":1000,"max":5000}
},

# ================= AC SYSTEM =================

{
"id":36,
"problem":"AC Gas Low",
"system":"ac",
"component":"ac refrigerant",
"severity":"medium",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"ac not cooling properly",
"weak airflow from vents"
],
"user_checks":[
"check AC cooling performance"
],
"repair_cost":{"min":1500,"max":4000}
},

{
"id":37,
"problem":"AC Compressor Failure",
"system":"ac",
"component":"ac compressor",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"ac not cooling",
"loud noise from compressor"
],
"user_checks":[
"check compressor engagement"
],
"repair_cost":{"min":8000,"max":25000}
},

{
"id":38,
"problem":"Cabin Air Filter Clogged",
"system":"ac",
"component":"cabin air filter",
"severity":"low",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"weak airflow",
"bad smell in cabin"
],
"user_checks":[
"inspect cabin air filter"
],
"repair_cost":{"min":300,"max":1500}
},

{
"id":39,
"problem":"AC Condenser Blocked",
"system":"ac",
"component":"ac condenser",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"ac cooling weak",
"ac cooling drops in traffic"
],
"user_checks":[
"inspect condenser fins"
],
"repair_cost":{"min":2000,"max":8000}
},

{
"id":40,
"problem":"Blower Motor Failure",
"system":"ac",
"component":"blower motor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"no air from vents",
"blower not working"
],
"user_checks":[
"test blower fan speed"
],
"repair_cost":{"min":2000,"max":6000}
},

# ================= FUEL SYSTEM =================

{
"id":41,
"problem":"Fuel Pump Weak",
"system":"fuel",
"component":"fuel pump",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine hard to start",
"loss of power"
],
"user_checks":[
"listen for fuel pump sound"
],
"repair_cost":{"min":4000,"max":12000}
},

{
"id":42,
"problem":"Fuel Filter Clogged",
"system":"fuel",
"component":"fuel filter",
"severity":"medium",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"engine hesitation",
"loss of power"
],
"user_checks":[
"check fuel filter replacement history"
],
"repair_cost":{"min":800,"max":3000}
},

{
"id":43,
"problem":"Fuel Pressure Regulator Fault",
"system":"fuel",
"component":"fuel pressure regulator",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine hesitation",
"poor fuel economy"
],
"user_checks":[
"observe fuel pressure behavior"
],
"repair_cost":{"min":3000,"max":9000}
},

{
"id":44,
"problem":"EVAP Purge Valve Fault",
"system":"fuel",
"component":"evap purge valve",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"check engine light",
"rough idle"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":2500,"max":8000}
},

{
"id":45,
"problem":"Fuel Tank Vent Blocked",
"system":"fuel",
"component":"fuel tank vent",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"difficulty refueling",
"fuel smell near vehicle"
],
"user_checks":[
"observe fuel filling behavior"
],
"repair_cost":{"min":1500,"max":6000}
},

# ================= BODY / MISC =================

{
"id":46,
"problem":"Horn Not Working",
"system":"electrical",
"component":"horn system",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"horn not producing sound"
],
"user_checks":[
"check horn fuse"
],
"repair_cost":{"min":500,"max":3000}
},

{
"id":47,
"problem":"Wiper Motor Failure",
"system":"electrical",
"component":"wiper motor",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"wipers not moving"
],
"user_checks":[
"test wiper operation"
],
"repair_cost":{"min":2000,"max":7000}
},

{
"id":48,
"problem":"Headlight Bulb Burned",
"system":"electrical",
"component":"headlight bulb",
"severity":"low",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"headlight not working"
],
"user_checks":[
"inspect headlight bulb"
],
"repair_cost":{"min":300,"max":2000}
},

{
"id":49,
"problem":"Brake Light Switch Fault",
"system":"electrical",
"component":"brake light switch",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"brake lights not working"
],
"user_checks":[
"check brake lights when pedal pressed"
],
"repair_cost":{"min":800,"max":3000}
},

{
"id":50,
"problem":"Sunroof Drain Blocked",
"system":"body",
"component":"sunroof drain",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"water leakage inside cabin"
],
"user_checks":[
"inspect sunroof drain outlets"
],
"repair_cost":{"min":1000,"max":4000}
},

# ================= STEERING SYSTEM =================

{
"id":51,
"problem":"Power Steering Fluid Low",
"system":"steering",
"component":"power steering system",
"severity":"medium",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"hard steering",
"whining noise while turning"
],
"user_checks":[
"check power steering fluid level"
],
"repair_cost":{"min":500,"max":4000}
},

{
"id":52,
"problem":"Power Steering Pump Failure",
"system":"steering",
"component":"power steering pump",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"hard steering",
"whining noise from pump"
],
"user_checks":[
"observe steering effort during turns"
],
"repair_cost":{"min":4000,"max":15000}
},

{
"id":53,
"problem":"Steering Rack Wear",
"system":"steering",
"component":"steering rack",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"loose steering",
"steering knocking noise"
],
"user_checks":[
"check steering free play"
],
"repair_cost":{"min":8000,"max":35000}
},

{
"id":54,
"problem":"Tie Rod End Wear",
"system":"steering",
"component":"tie rod",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"car pulling to one side",
"steering loose",
"steering vibration",
"uneven tire wear"
],
"user_checks":[
"inspect steering play"
],
"repair_cost":{"min":2500,"max":8000}
},

{
"id":55,
"problem":"Steering Column Joint Wear",
"system":"steering",
"component":"steering column joint",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"steering vibration",
"knocking in steering"
],
"user_checks":[
"observe steering vibration while driving"
],
"repair_cost":{"min":3000,"max":12000}
},

# ================= EXHAUST SYSTEM =================

{
"id":56,
"problem":"Catalytic Converter Blocked",
"system":"exhaust",
"component":"catalytic converter",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine power loss",
"poor fuel efficiency"
],
"user_checks":[
"check exhaust flow"
],
"repair_cost":{"min":8000,"max":35000}
},

{
"id":57,
"problem":"Exhaust Leak",
"system":"exhaust",
"component":"exhaust pipe",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"loud exhaust noise",
"exhaust smell"
],
"user_checks":[
"inspect exhaust pipe for leak"
],
"repair_cost":{"min":1500,"max":8000}
},

{
"id":58,
"problem":"Muffler Damage",
"system":"exhaust",
"component":"muffler",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"loud exhaust sound",
"vibration from rear"
],
"user_checks":[
"inspect muffler condition"
],
"repair_cost":{"min":2000,"max":10000}
},

{
"id":59,
"problem":"DPF Filter Blocked",
"system":"exhaust",
"component":"diesel particulate filter",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"DPF warning light",
"engine power reduced"
],
"user_checks":[
"check DPF warning indicator"
],
"repair_cost":{"min":5000,"max":25000}
},

{
"id":60,
"problem":"EGR Valve Blocked",
"system":"engine",
"component":"EGR valve",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"rough idle",
"engine hesitation"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":2500,"max":7000}
},

# ================= SENSORS =================

{
"id":61,
"problem":"Crankshaft Position Sensor Fault",
"system":"engine",
"component":"crankshaft position sensor",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine not starting",
"engine stalling"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":2500,"max":8000}
},

{
"id":62,
"problem":"Camshaft Position Sensor Fault",
"system":"engine",
"component":"camshaft position sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine misfire",
"poor acceleration"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":2500,"max":9000}
},

{
"id":63,
"problem":"Throttle Position Sensor Fault",
"system":"engine",
"component":"throttle position sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine hesitation",
"irregular acceleration"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":3000,"max":8000}
},

{
"id":64,
"problem":"Knock Sensor Fault",
"system":"engine",
"component":"knock sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine knocking sound",
"reduced engine power"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":3000,"max":9000}
},

{
"id":65,
"problem":"Idle Air Control Valve Fault",
"system":"engine",
"component":"idle air control valve",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine idle unstable",
"RPM fluctuating"
],
"user_checks":[
"observe idle RPM"
],
"repair_cost":{"min":2000,"max":7000}
},

# ================= DRIVETRAIN =================

{
"id":66,
"problem":"Drive Belt Worn",
"system":"engine",
"component":"drive belt",
"severity":"medium",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"squealing noise from engine"
],
"user_checks":[
"inspect belt condition"
],
"repair_cost":{"min":800,"max":4000}
},

{
"id":67,
"problem":"Serpentine Belt Slipping",
"system":"engine",
"component":"serpentine belt",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"squealing noise during acceleration"
],
"user_checks":[
"check belt tension"
],
"repair_cost":{"min":1000,"max":5000}
},

{
"id":68,
"problem":"Transmission Mount Worn",
"system":"transmission",
"component":"transmission mount",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"vibration during gear shift"
],
"user_checks":[
"inspect drivetrain movement"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":69,
"problem":"Clutch Release Bearing Worn",
"system":"transmission",
"component":"clutch release bearing",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"whining noise when clutch pressed"
],
"user_checks":[
"listen for noise when clutch pedal pressed"
],
"repair_cost":{"min":5000,"max":15000}
},

{
"id":70,
"problem":"Wheel Balancing Incorrect",
"system":"suspension",
"component":"wheel balancing",
"severity":"low",
"urgency":"service_soon",
"probability":7,
"symptoms":[
"car shaking while driving",
"vibration while driving",
"steering vibration",
"wheel vibration"
],
"user_checks":[
"observe vibration around 80-100 km/h"
],
"repair_cost":{"min":500,"max":2000}
},

{
"id":71,
"problem":"Tire Sidewall Damage",
"system":"suspension",
"component":"tire",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"bulge on tire sidewall"
],
"user_checks":[
"inspect tire sidewall"
],
"repair_cost":{"min":3000,"max":10000}
},

{
"id":72,
"problem":"Wheel Rim Bent",
"system":"suspension",
"component":"wheel rim",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"steering vibration",
"air pressure loss"
],
"user_checks":[
"inspect wheel rim"
],
"repair_cost":{"min":2000,"max":8000}
},

{
"id":73,
"problem":"Parking Brake Stuck",
"system":"brake",
"component":"parking brake",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"car not moving freely"
],
"user_checks":[
"check parking brake release"
],
"repair_cost":{"min":1000,"max":5000}
},

{
"id":74,
"problem":"Door Lock Actuator Failure",
"system":"body",
"component":"door lock actuator",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"door not locking or unlocking"
],
"user_checks":[
"test central locking"
],
"repair_cost":{"min":1500,"max":6000}
},

{
"id":75,
"problem":"Window Regulator Failure",
"system":"body",
"component":"window regulator",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"window not moving"
],
"user_checks":[
"test window switch"
],
"repair_cost":{"min":2000,"max":7000}
},

# ================= ELECTRICAL & ELECTRONICS =================

{
"id":76,
"problem":"ECU Communication Error",
"system":"electrical",
"component":"ECU",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"multiple warning lights",
"engine performance irregular"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":3000,"max":20000}
},

{
"id":77,
"problem":"ABS Module Failure",
"system":"brake",
"component":"ABS module",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"ABS warning light",
"ABS not working"
],
"user_checks":[
"scan ABS system codes"
],
"repair_cost":{"min":6000,"max":25000}
},

{
"id":78,
"problem":"Instrument Cluster Fault",
"system":"electrical",
"component":"instrument cluster",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"speedometer not working",
"dashboard display flickering"
],
"user_checks":[
"observe dashboard display behavior"
],
"repair_cost":{"min":4000,"max":20000}
},

{
"id":79,
"problem":"Central Locking Module Failure",
"system":"electrical",
"component":"central locking system",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"central locking not responding",
"doors not locking simultaneously"
],
"user_checks":[
"test central locking using key"
],
"repair_cost":{"min":2000,"max":10000}
},

{
"id":80,
"problem":"Key Fob Battery Dead",
"system":"electrical",
"component":"key fob",
"severity":"low",
"urgency":"service_soon",
"probability":5,
"symptoms": [
"car not starting",
"no start",
"dashboard lights dim",
"clicking sound while starting"
],
"user_checks":[
"replace key fob battery"
],
"repair_cost":{"min":100,"max":500}
},

# ================= COOLING & HEATING =================

{
"id":81,
"problem":"Heater Core Blocked",
"system":"cooling",
"component":"heater core",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"heater not producing heat",
"fogging inside windshield"
],
"user_checks":[
"check heater performance"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":82,
"problem":"Cooling Fan Relay Failure",
"system":"cooling",
"component":"fan relay",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"radiator fan not working",
"engine overheating in traffic"
],
"user_checks":[
"inspect fan relay"
],
"repair_cost":{"min":1000,"max":5000}
},

{
"id":83,
"problem":"Coolant Temperature Sensor Fault",
"system":"cooling",
"component":"temperature sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"incorrect temperature reading",
"engine overheating warning"
],
"user_checks":[
"scan OBD temperature data"
],
"repair_cost":{"min":2000,"max":7000}
},

{
"id":84,
"problem":"Coolant Hose Leak",
"system":"cooling",
"component":"coolant hose",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"coolant leakage",
"engine overheating"
],
"user_checks":[
"inspect hoses for leaks"
],
"repair_cost":{"min":800,"max":5000}
},

{
"id":85,
"problem":"Radiator Cap Failure",
"system":"cooling",
"component":"radiator cap",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"coolant loss",
"engine overheating"
],
"user_checks":[
"inspect radiator cap seal"
],
"repair_cost":{"min":300,"max":1500}
},

# ================= BODY / INTERIOR =================

{
"id":86,
"problem":"Seat Belt Sensor Fault",
"system":"electrical",
"component":"seat belt sensor",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"seat belt warning stays on"
],
"user_checks":[
"check seat belt latch"
],
"repair_cost":{"min":1000,"max":4000}
},

{
"id":87,
"problem":"Reverse Camera Failure",
"system":"electrical",
"component":"reverse camera",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"no rear camera display"
],
"user_checks":[
"check infotainment display"
],
"repair_cost":{"min":2000,"max":10000}
},

{
"id":88,
"problem":"Infotainment System Freeze",
"system":"electrical",
"component":"infotainment system",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"screen freezing",
"touchscreen not responding"
],
"user_checks":[
"restart infotainment system"
],
"repair_cost":{"min":3000,"max":20000}
},

{
"id":89,
"problem":"Interior Cabin Water Leak",
"system":"body",
"component":"body seals",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"water inside cabin",
"wet floor carpet"
],
"user_checks":[
"inspect door seals"
],
"repair_cost":{"min":2000,"max":10000}
},

{
"id":90,
"problem":"Door Hinge Wear",
"system":"body",
"component":"door hinge",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"door sagging",
"door noise while opening"
],
"user_checks":[
"check door alignment"
],
"repair_cost":{"min":1000,"max":5000}
},

# ================= SAFETY =================

{
"id":91,
"problem":"Airbag Warning Light",
"system":"safety",
"component":"airbag system",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"airbag warning light on"
],
"user_checks":[
"scan airbag system codes"
],
"repair_cost":{"min":3000,"max":20000}
},

{
"id":92,
"problem":"Seat Occupancy Sensor Fault",
"system":"safety",
"component":"seat sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"airbag light on"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":93,
"problem":"Parking Sensor Failure",
"system":"safety",
"component":"parking sensor",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"parking sensor not beeping"
],
"user_checks":[
"check sensor obstruction"
],
"repair_cost":{"min":1500,"max":8000}
},

{
"id":94,
"problem":"ADAS Camera Misalignment",
"system":"safety",
"component":"ADAS camera",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"lane assist not working"
],
"user_checks":[
"clean windshield camera area"
],
"repair_cost":{"min":5000,"max":20000}
},

{
"id":95,
"problem":"Blind Spot Sensor Fault",
"system":"safety",
"component":"blind spot sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"blind spot warning not working"
],
"user_checks":[
"inspect sensor area"
],
"repair_cost":{"min":6000,"max":25000}
},

{
"id":96,
"problem":"Cruise Control Not Working",
"system":"electrical",
"component":"cruise control system",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"cruise control not activating"
],
"user_checks":[
"check cruise control switch"
],
"repair_cost":{"min":2000,"max":12000}
},

{
"id":97,
"problem":"Fuel Gauge Incorrect Reading",
"system":"electrical",
"component":"fuel gauge sensor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"fuel gauge inaccurate"
],
"user_checks":[
"observe fuel level changes"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":98,
"problem":"Speed Sensor Failure",
"system":"electrical",
"component":"speed sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"speedometer not working"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":2500,"max":8000}
},

{
"id":99,
"problem":"Alternator Belt Loose",
"system":"engine",
"component":"drive belt",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"squealing noise from engine"
],
"user_checks":[
"inspect belt tension"
],
"repair_cost":{"min":800,"max":4000}
},

{
"id":100,
"problem":"Engine Head Gasket Leak",
"system":"engine",
"component":"head gasket",
"severity":"critical",
"urgency":"stop_driving",
"probability":2,
"symptoms":[
"white smoke from exhaust",
"coolant loss",
"engine overheating"
],
"user_checks":[
"check coolant level frequently"
],
"repair_cost":{"min":20000,"max":60000}
},

# ================= TURBO & ADVANCED ENGINE =================

{
"id":101,
"problem":"Turbocharger Lag",
"system":"engine",
"component":"turbocharger",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"delayed acceleration",
"lack of power at low RPM"
],
"user_checks":[
"observe turbo boost response"
],
"repair_cost":{"min":5000,"max":20000}
},

{
"id":102,
"problem":"Turbocharger Failure",
"vehicle_type":[
"turbo"
],
"system":"engine",
"component":"turbocharger",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"loss of engine power",
"whistling noise from engine",
"black smoke from exhaust"
],
"user_checks":[
"listen for turbo whistle"
],
"repair_cost":{"min":15000,"max":60000}
},

{
"id":103,
"problem":"Intercooler Leak",
"system":"engine",
"component":"intercooler",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"loss of turbo boost",
"engine power loss"
],
"user_checks":[
"inspect intercooler pipes"
],
"repair_cost":{"min":3000,"max":15000}
},

{
"id":104,
"problem":"Turbo Boost Pressure Sensor Fault",
"system":"engine",
"component":"boost sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"check engine light",
"poor acceleration"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":3000,"max":9000}
},

{
"id":105,
"problem":"Wastegate Valve Stuck",
"system":"engine",
"component":"turbo wastegate",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"overboost condition",
"engine knocking under load"
],
"user_checks":[
"observe boost pressure behavior"
],
"repair_cost":{"min":5000,"max":20000}
},

# ================= DIESEL SYSTEM =================

{
"id":106,
"problem":"Common Rail Fuel Pump Failure",
"system":"fuel",
"component":"high pressure fuel pump",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine hard to start",
"engine stalling"
],
"user_checks":[
"scan OBD fuel pressure data"
],
"repair_cost":{"min":15000,"max":60000}
},

{
"id":107,
"problem":"Diesel Injector Failure",
"system":"fuel",
"component":"diesel injector",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine knocking",
"excessive smoke",
"poor fuel economy"
],
"user_checks":[
"observe exhaust smoke color"
],
"repair_cost":{"min":8000,"max":30000}
},

{
"id":108,
"problem":"Glow Plug Failure",
"system":"engine",
"component":"glow plug",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"difficulty starting in cold",
"engine rough startup"
],
"user_checks":[
"check glow plug warning light"
],
"repair_cost":{"min":2000,"max":8000}
},

{
"id":109,
"problem":"Diesel Fuel Contamination",
"system":"fuel",
"component":"fuel system",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine hesitation",
"poor acceleration"
],
"user_checks":[
"check fuel quality"
],
"repair_cost":{"min":3000,"max":20000}
},

{
"id":110,
"problem":"High Pressure Fuel Line Leak",
"system":"fuel",
"component":"fuel line",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"fuel smell",
"engine power loss"
],
"user_checks":[
"inspect fuel lines"
],
"repair_cost":{"min":3000,"max":15000}
},

# ================= TRANSMISSION ADVANCED =================

{
"id":111,
"problem":"Automatic Transmission Slipping",
"system":"transmission",
"component":"automatic gearbox",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"delayed acceleration",
"gear slipping"
],
"user_checks":[
"observe gear shifting behavior"
],
"repair_cost":{"min":15000,"max":80000}
},

{
"id":112,
"problem":"Torque Converter Failure",
"system":"transmission",
"component":"torque converter",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"transmission vibration",
"delayed gear engagement"
],
"user_checks":[
"observe vibration during acceleration"
],
"repair_cost":{"min":20000,"max":90000}
},

{
"id":113,
"problem":"CV Joint Wear",
"system":"drivetrain",
"component":"CV joint",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"clicking noise while turning"
],
"user_checks":[
"check noise during sharp turns"
],
"repair_cost":{"min":4000,"max":15000}
},

{
"id":114,
"problem":"Drive Shaft Imbalance",
"system":"drivetrain",
"component":"drive shaft",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"vibration during acceleration"
],
"user_checks":[
"observe vibration at highway speed"
],
"repair_cost":{"min":5000,"max":20000}
},

{
"id":115,
"problem":"Differential Gear Wear",
"system":"drivetrain",
"component":"differential",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"whining noise from rear axle"
],
"user_checks":[
"listen for noise during acceleration"
],
"repair_cost":{"min":15000,"max":60000}
},

# ================= ADVANCED ELECTRONICS =================

{
"id":116,
"problem":"ECU Software Corruption",
"system":"electrical",
"component":"ECU software",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"random warning lights",
"engine performance irregular"
],
"user_checks":[
"scan ECU codes"
],
"repair_cost":{"min":5000,"max":30000}
},

{
"id":117,
"problem":"CAN Bus Communication Error",
"system":"electrical",
"component":"CAN bus network",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"multiple systems malfunction"
],
"user_checks":[
"scan vehicle network errors"
],
"repair_cost":{"min":5000,"max":40000}
},

{
"id":118,
"problem":"Immobilizer System Fault",
"system":"security",
"component":"immobilizer",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"car not starting",
"security warning light"
],
"user_checks":[
"try spare key"
],
"repair_cost":{"min":4000,"max":20000}
},

{
"id":119,
"problem":"Keyless Entry Module Failure",
"system":"electrical",
"component":"keyless entry module",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"keyless entry not working"
],
"user_checks":[
"check key fob battery"
],
"repair_cost":{"min":3000,"max":15000}
},

{
"id":120,
"problem":"Starter Relay Failure",
"system":"electrical",
"component":"starter relay",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"car not starting",
"click sound while starting"
],
"user_checks":[
"inspect starter relay"
],
"repair_cost":{"min":1000,"max":5000}
},
{
"problem": "Battery Dead",
"component": "battery",
"system": "electrical",

"symptoms": [
"car not starting",
"clicking sound while starting",
"dashboard lights dim",
"engine does not crank"
],

"possible_causes": [
"old battery",
"battery discharged",
"charging system failure"
],

"severity": "medium",

"repair_cost": {
"min": 3000,
"max": 7000
},

"user_checks": [
"check dashboard lights brightness",
"try jump start",
"check battery voltage"
],

"probability": 5
},

# ================= AIR INTAKE =================

{
"id":121,
"problem":"Intake Manifold Leak",
"system":"engine",
"component":"intake manifold",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"rough idle",
"engine hesitation"
],
"user_checks":[
"listen for air leak noise"
],
"repair_cost":{"min":4000,"max":20000}
},

{
"id":122,
"problem":"PCV Valve Blocked",
"system":"engine",
"component":"pcv valve",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine oil consumption high",
"rough idle"
],
"user_checks":[
"inspect PCV valve"
],
"repair_cost":{"min":800,"max":3000}
},

{
"id":123,
"problem":"Air Intake Hose Crack",
"system":"engine",
"component":"air intake hose",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine hesitation",
"hissing noise"
],
"user_checks":[
"inspect intake hose"
],
"repair_cost":{"min":500,"max":3000}
},

{
"id":124,
"problem":"Throttle Cable Loose",
"system":"engine",
"component":"throttle cable",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"delayed acceleration"
],
"user_checks":[
"inspect throttle cable movement"
],
"repair_cost":{"min":500,"max":2500}
},

{
"id":125,
"problem":"Engine Oil Pump Failure",
"system":"engine",
"component":"oil pump",
"severity":"critical",
"urgency":"stop_driving",
"probability":2,
"symptoms":[
"low oil pressure warning",
"engine knocking"
],
"user_checks":[
"check oil pressure warning light"
],
"repair_cost":{"min":15000,"max":60000}
},

# ================= ENGINE LUBRICATION =================

{
"id":126,
"problem":"Engine Oil Leak",
"system":"engine",
"component":"engine seals",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"oil spots under car",
"low engine oil level"
],
"user_checks":[
"inspect engine area for oil leak"
],
"repair_cost":{"min":1500,"max":8000}
},

{
"id":127,
"problem":"Valve Cover Gasket Leak",
"system":"engine",
"component":"valve cover gasket",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"oil smell from engine",
"oil leak near engine top"
],
"user_checks":[
"inspect valve cover area"
],
"repair_cost":{"min":2000,"max":7000}
},

{
"id":128,
"problem":"Oil Filter Loose",
"system":"engine",
"component":"oil filter",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"oil leak after service"
],
"user_checks":[
"inspect oil filter area"
],
"repair_cost":{"min":500,"max":2000}
},

{
"id":129,
"problem":"Engine Oil Pressure Sensor Fault",
"system":"engine",
"component":"oil pressure sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"oil pressure warning light"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":2000,"max":6000}
},

{
"id":130,
"problem":"Oil Cooler Leak",
"system":"engine",
"component":"oil cooler",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"engine oil leak",
"engine overheating"
],
"user_checks":[
"inspect oil cooler lines"
],
"repair_cost":{"min":4000,"max":15000}
},

# ================= HVAC SYSTEM =================

{
"id":131,
"problem":"AC Expansion Valve Fault",
"system":"ac",
"component":"expansion valve",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"AC cooling inconsistent"
],
"user_checks":[
"observe AC cooling performance"
],
"repair_cost":{"min":3000,"max":9000}
},

{
"id":132,
"problem":"AC Evaporator Leak",
"system":"ac",
"component":"evaporator",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"AC gas leakage",
"weak cooling"
],
"user_checks":[
"check AC gas level"
],
"repair_cost":{"min":8000,"max":25000}
},

{
"id":133,
"problem":"Heater Blower Resistor Fault",
"system":"ac",
"component":"blower resistor",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"blower fan working only at one speed"
],
"user_checks":[
"test blower speed settings"
],
"repair_cost":{"min":1000,"max":4000}
},

{
"id":134,
"problem":"AC Temperature Sensor Fault",
"system":"ac",
"component":"AC sensor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"AC temperature fluctuating"
],
"user_checks":[
"observe AC cooling cycles"
],
"repair_cost":{"min":1500,"max":6000}
},

{
"id":135,
"problem":"AC Blend Door Motor Failure",
"system":"ac",
"component":"blend door motor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"AC airflow direction incorrect"
],
"user_checks":[
"change AC airflow settings"
],
"repair_cost":{"min":3000,"max":10000}
},

# ================= HYBRID VEHICLE SYSTEM =================

{
"id":136,
"problem":"Hybrid Battery Degradation",
"system":"hybrid",
"component":"hybrid battery",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"reduced electric range",
"hybrid warning light"
],
"user_checks":[
"check hybrid system warning"
],
"repair_cost":{"min":40000,"max":200000}
},

{
"id":137,
"problem":"Hybrid Inverter Failure",
"system":"hybrid",
"component":"inverter",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"hybrid system malfunction warning"
],
"user_checks":[
"scan hybrid ECU codes"
],
"repair_cost":{"min":30000,"max":150000}
},

{
"id":138,
"problem":"Hybrid Cooling Pump Failure",
"system":"hybrid",
"component":"battery cooling pump",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"hybrid battery overheating warning"
],
"user_checks":[
"check hybrid warning lights"
],
"repair_cost":{"min":10000,"max":40000}
},

{
"id":139,
"problem":"Hybrid System Sensor Fault",
"system":"hybrid",
"component":"hybrid sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"hybrid system warning"
],
"user_checks":[
"scan hybrid diagnostic codes"
],
"repair_cost":{"min":5000,"max":20000}
},

{
"id":140,
"problem":"Regenerative Braking Fault",
"system":"hybrid",
"component":"regenerative braking system",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"reduced regenerative braking"
],
"user_checks":[
"observe braking behavior"
],
"repair_cost":{"min":8000,"max":30000}
},

# ================= EV SYSTEM =================

{
"id":141,
"problem":"EV Battery Cell Imbalance",
"system":"ev",
"component":"battery pack",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"range drop suddenly"
],
"user_checks":[
"check EV range behavior"
],
"repair_cost":{"min":50000,"max":300000}
},

{
"id":142,
"problem":"EV Charging Port Fault",
"system":"ev",
"component":"charging port",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"vehicle not charging"
],
"user_checks":[
"check charging cable"
],
"repair_cost":{"min":5000,"max":30000}
},

{
"id":143,
"problem":"EV Onboard Charger Failure",
"system":"ev",
"component":"onboard charger",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"charging error message"
],
"user_checks":[
"try different charger"
],
"repair_cost":{"min":20000,"max":150000}
},

{
"id":144,
"problem":"EV Cooling System Failure",
"system":"ev",
"component":"battery cooling system",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"battery temperature warning"
],
"user_checks":[
"check EV temperature warning"
],
"repair_cost":{"min":15000,"max":80000}
},

{
"id":145,
"problem":"EV Motor Controller Fault",
"system":"ev",
"component":"motor controller",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"vehicle not accelerating"
],
"user_checks":[
"check EV warning lights"
],
"repair_cost":{"min":30000,"max":200000}
},

# ================= BODY ELECTRONICS =================

{
"id":146,
"problem":"Rain Sensor Failure",
"system":"electrical",
"component":"rain sensor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"automatic wipers not working"
],
"user_checks":[
"test auto wiper mode"
],
"repair_cost":{"min":2000,"max":8000}
},

{
"id":147,
"problem":"Ambient Light Sensor Fault",
"system":"electrical",
"component":"light sensor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"auto headlights not working"
],
"user_checks":[
"test headlight auto mode"
],
"repair_cost":{"min":2000,"max":7000}
},

{
"id":148,
"problem":"Power Window Switch Failure",
"system":"electrical",
"component":"window switch",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"window not responding"
],
"user_checks":[
"test other window switches"
],
"repair_cost":{"min":1500,"max":5000}
},

{
"id":149,
"problem":"Interior Fuse Box Corrosion",
"system":"electrical",
"component":"fuse box",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"multiple electrical failures"
],
"user_checks":[
"inspect fuse box condition"
],
"repair_cost":{"min":2000,"max":10000}
},

{
"id":150,
"problem":"Sunroof Motor Failure",
"system":"body",
"component":"sunroof motor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"sunroof not opening"
],
"user_checks":[
"test sunroof switch"
],
"repair_cost":{"min":4000,"max":15000}
},
# ================= ADAS SYSTEMS =================

{
"id":151,
"problem":"Lane Assist Camera Failure",
"system":"ADAS",
"component":"lane camera",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"lane assist warning",
"lane assist not functioning"
],
"user_checks":[
"clean windshield camera area"
],
"repair_cost":{"min":5000,"max":25000}
},

{
"id":152,
"problem":"Adaptive Cruise Radar Fault",
"system":"ADAS",
"component":"radar sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"adaptive cruise not working"
],
"user_checks":[
"check radar sensor obstruction"
],
"repair_cost":{"min":8000,"max":40000}
},

{
"id":153,
"problem":"Forward Collision Sensor Error",
"system":"ADAS",
"component":"collision sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"collision warning unavailable"
],
"user_checks":[
"inspect front bumper sensor"
],
"repair_cost":{"min":7000,"max":35000}
},

{
"id":154,
"problem":"Rear Cross Traffic Sensor Fault",
"system":"ADAS",
"component":"rear radar sensor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"rear cross traffic alert not working"
],
"user_checks":[
"check rear bumper sensors"
],
"repair_cost":{"min":6000,"max":30000}
},

{
"id":155,
"problem":"Automatic Emergency Braking Fault",
"system":"ADAS",
"component":"AEB system",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"AEB warning light"
],
"user_checks":[
"scan ADAS diagnostic codes"
],
"repair_cost":{"min":10000,"max":50000}
},

# ================= COOLING SYSTEM EXTENDED =================

{
"id":156,
"problem":"Radiator Fan Blade Damage",
"system":"cooling",
"component":"radiator fan",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine overheating",
"fan noise"
],
"user_checks":[
"inspect radiator fan blades"
],
"repair_cost":{"min":2000,"max":7000}
},

{
"id":157,
"problem":"Coolant Reservoir Crack",
"system":"cooling",
"component":"coolant reservoir",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"coolant leakage"
],
"user_checks":[
"inspect coolant reservoir"
],
"repair_cost":{"min":1000,"max":5000}
},

{
"id":158,
"problem":"Cooling System Air Lock",
"system":"cooling",
"component":"cooling circuit",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine overheating intermittently"
],
"user_checks":[
"check coolant circulation"
],
"repair_cost":{"min":1000,"max":4000}
},

{
"id":159,
"problem":"Radiator Thermo Switch Failure",
"system":"cooling",
"component":"thermo switch",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"radiator fan not activating"
],
"user_checks":[
"observe fan operation"
],
"repair_cost":{"min":2000,"max":6000}
},

{
"id":160,
"problem":"Coolant Pipe Blockage",
"system":"cooling",
"component":"coolant pipe",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"engine overheating"
],
"user_checks":[
"inspect coolant pipes"
],
"repair_cost":{"min":2000,"max":8000}
},

# ================= DRIVETRAIN EXTENDED =================

{
"id":161,
"problem":"Propeller Shaft Imbalance",
"system":"drivetrain",
"component":"propeller shaft",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"vibration during acceleration"
],
"user_checks":[
"observe vibration at high speed"
],
"repair_cost":{"min":5000,"max":20000}
},

{
"id":162,
"problem":"Axle Shaft Damage",
"system":"drivetrain",
"component":"axle shaft",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"knocking noise while driving"
],
"user_checks":[
"inspect axle shaft area"
],
"repair_cost":{"min":7000,"max":25000}
},

{
"id":163,
"problem":"Differential Oil Low",
"system":"drivetrain",
"component":"differential",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"whining noise from rear axle"
],
"user_checks":[
"check differential oil level"
],
"repair_cost":{"min":1000,"max":5000}
},

{
"id":164,
"problem":"Limited Slip Differential Fault",
"system":"drivetrain",
"component":"LSD",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"traction issues during acceleration"
],
"user_checks":[
"observe wheel spin behavior"
],
"repair_cost":{"min":15000,"max":70000}
},

{
"id":165,
"problem":"Transfer Case Failure",
"system":"drivetrain",
"component":"transfer case",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"4WD not engaging"
],
"user_checks":[
"test 4WD engagement"
],
"repair_cost":{"min":20000,"max":90000}
},

# ================= SENSORS ADVANCED =================

{
"id":166,
"problem":"Wheel Speed Sensor Failure",
"system":"brake",
"component":"wheel speed sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"ABS warning light"
],
"user_checks":[
"scan ABS system codes"
],
"repair_cost":{"min":2500,"max":9000}
},

{
"id":167,
"problem":"Yaw Rate Sensor Fault",
"system":"stability",
"component":"yaw sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"ESP warning light"
],
"user_checks":[
"scan ESP codes"
],
"repair_cost":{"min":5000,"max":20000}
},

{
"id":168,
"problem":"Steering Angle Sensor Fault",
"system":"stability",
"component":"steering angle sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"ESP malfunction warning"
],
"user_checks":[
"scan diagnostic codes"
],
"repair_cost":{"min":5000,"max":18000}
},

{
"id":169,
"problem":"Brake Pressure Sensor Fault",
"system":"brake",
"component":"brake pressure sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"brake warning light"
],
"user_checks":[
"scan brake system codes"
],
"repair_cost":{"min":4000,"max":15000}
},

{
"id":170,
"problem":"Transmission Speed Sensor Fault",
"system":"transmission",
"component":"speed sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"gear shifting abnormal"
],
"user_checks":[
"scan transmission codes"
],
"repair_cost":{"min":3000,"max":10000}
},

# ================= BODY ELECTRONICS =================

{
"id":171,
"problem":"Electric Seat Motor Failure",
"system":"body",
"component":"seat motor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"seat adjustment not working"
],
"user_checks":[
"test seat adjustment switches"
],
"repair_cost":{"min":3000,"max":15000}
},

{
"id":172,
"problem":"Tail Light Circuit Fault",
"system":"electrical",
"component":"tail light wiring",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"tail lights not working"
],
"user_checks":[
"inspect tail light bulbs"
],
"repair_cost":{"min":500,"max":4000}
},

{
"id":173,
"problem":"Fog Light Relay Failure",
"system":"electrical",
"component":"fog light relay",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"fog lights not working"
],
"user_checks":[
"inspect fog light relay"
],
"repair_cost":{"min":500,"max":3000}
},

{
"id":174,
"problem":"Windshield Washer Pump Failure",
"system":"body",
"component":"washer pump",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"washer fluid not spraying"
],
"user_checks":[
"check washer fluid level"
],
"repair_cost":{"min":800,"max":3000}
},

{
"id":175,
"problem":"Rear Defogger Not Working",
"system":"electrical",
"component":"rear defogger",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"rear windshield fog not clearing"
],
"user_checks":[
"check defogger switch"
],
"repair_cost":{"min":1500,"max":6000}
},

# ================= EV BATTERY MANAGEMENT =================

{
"id":176,
"problem":"Battery Management System Fault",
"system":"ev",
"component":"BMS",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"EV battery warning light",
"reduced driving range"
],
"user_checks":[
"scan EV diagnostic codes"
],
"repair_cost":{"min":10000,"max":60000}
},

{
"id":177,
"problem":"EV Battery Thermal Sensor Fault",
"system":"ev",
"component":"battery temperature sensor",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"battery overheating warning"
],
"user_checks":[
"scan EV battery temperature data"
],
"repair_cost":{"min":5000,"max":25000}
},

{
"id":178,
"problem":"EV Battery Cooling Fan Failure",
"system":"ev",
"component":"battery cooling fan",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"battery temperature warning"
],
"user_checks":[
"inspect battery cooling fan"
],
"repair_cost":{"min":8000,"max":35000}
},

{
"id":179,
"problem":"EV High Voltage Cable Fault",
"system":"ev",
"component":"high voltage cable",
"severity":"critical",
"urgency":"stop_driving",
"probability":2,
"symptoms":[
"EV power loss",
"high voltage system warning"
],
"user_checks":[
"check EV warning lights"
],
"repair_cost":{"min":20000,"max":100000}
},

{
"id":180,
"problem":"EV Motor Bearing Wear",
"system":"ev",
"component":"electric motor bearing",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"whining noise from EV motor"
],
"user_checks":[
"listen for motor noise"
],
"repair_cost":{"min":20000,"max":120000}
},

# ================= SUSPENSION GEOMETRY =================

{
"id":181,
"problem":"Control Arm Bush Wear",
"system":"suspension",
"component":"control arm bush",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"clunk noise over bumps"
],
"user_checks":[
"inspect suspension bushings"
],
"repair_cost":{"min":2000,"max":8000}
},

{
"id":182,
"problem":"Control Arm Ball Joint Wear",
"system":"suspension",
"component":"ball joint",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"clunk noise while turning"
],
"user_checks":[
"inspect ball joints"
],
"repair_cost":{"min":3000,"max":10000}
},

{
"id":183,
"problem":"Strut Mount Bearing Failure",
"system":"suspension",
"component":"strut mount",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"steering noise while turning"
],
"user_checks":[
"observe steering noise"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":184,
"problem":"Anti Roll Bar Link Wear",
"system":"suspension",
"component":"stabilizer link",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"rattling noise on rough road"
],
"user_checks":[
"inspect stabilizer link"
],
"repair_cost":{"min":1500,"max":5000}
},

{
"id":185,
"problem":"Subframe Mount Wear",
"system":"suspension",
"component":"subframe mount",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"vibration during acceleration"
],
"user_checks":[
"inspect subframe mounts"
],
"repair_cost":{"min":5000,"max":20000}
},

# ================= TRANSMISSION ELECTRONICS =================

{
"id":186,
"problem":"Transmission Control Module Fault",
"system":"transmission",
"component":"TCM",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"gear shifting erratic"
],
"user_checks":[
"scan transmission diagnostic codes"
],
"repair_cost":{"min":8000,"max":40000}
},

{
"id":187,
"problem":"Dual Clutch Transmission Overheat",
"system":"transmission",
"component":"DCT system",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"transmission overheating warning"
],
"user_checks":[
"observe gearbox temperature warnings"
],
"repair_cost":{"min":15000,"max":70000}
},

{
"id":188,
"problem":"Clutch Position Sensor Fault",
"system":"transmission",
"component":"clutch sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"gear shift delay"
],
"user_checks":[
"scan transmission codes"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":189,
"problem":"Gear Selector Module Failure",
"system":"transmission",
"component":"gear selector module",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"gear selector not responding"
],
"user_checks":[
"inspect gear selector operation"
],
"repair_cost":{"min":5000,"max":25000}
},

{
"id":190,
"problem":"Transmission Fluid Temperature Sensor Fault",
"system":"transmission",
"component":"temperature sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"transmission overheating warning"
],
"user_checks":[
"scan transmission data"
],
"repair_cost":{"min":3000,"max":10000}
},

# ================= DRIVETRAIN SENSORS =================

{
"id":191,
"problem":"Traction Control Sensor Fault",
"system":"stability",
"component":"traction control sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"traction control warning light"
],
"user_checks":[
"scan traction control codes"
],
"repair_cost":{"min":4000,"max":15000}
},

{
"id":192,
"problem":"Hill Assist Sensor Fault",
"system":"stability",
"component":"hill assist system",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"hill assist warning"
],
"user_checks":[
"scan vehicle diagnostics"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":193,
"problem":"Electronic Parking Brake Motor Failure",
"system":"brake",
"component":"EPB motor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"parking brake warning light"
],
"user_checks":[
"test electronic parking brake"
],
"repair_cost":{"min":5000,"max":20000}
},

{
"id":194,
"problem":"Brake Booster Vacuum Leak",
"system":"brake",
"component":"brake booster",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"hard brake pedal"
],
"user_checks":[
"observe brake pedal feel"
],
"repair_cost":{"min":4000,"max":15000}
},

{
"id":195,
"problem":"Brake Master Cylinder Failure",
"system":"brake",
"component":"master cylinder",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"brake pedal sinking"
],
"user_checks":[
"check brake fluid level"
],
"repair_cost":{"min":5000,"max":20000}
},

# ================= BODY CONTROL MODULE =================

{
"id":196,
"problem":"Body Control Module Failure",
"system":"electrical",
"component":"BCM",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"multiple electrical features malfunction"
],
"user_checks":[
"scan BCM diagnostic codes"
],
"repair_cost":{"min":8000,"max":50000}
},

{
"id":197,
"problem":"Interior CAN Network Fault",
"system":"electrical",
"component":"CAN network",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"dashboard errors"
],
"user_checks":[
"scan network communication errors"
],
"repair_cost":{"min":6000,"max":40000}
},

{
"id":198,
"problem":"Driver Assistance ECU Fault",
"system":"ADAS",
"component":"ADAS ECU",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"ADAS system unavailable"
],
"user_checks":[
"scan ADAS diagnostic codes"
],
"repair_cost":{"min":10000,"max":50000}
},

{
"id":199,
"problem":"Vehicle Speed Limiter Fault",
"system":"engine",
"component":"speed limiter system",
"severity":"low",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"vehicle speed restricted"
],
"user_checks":[
"check vehicle settings"
],
"repair_cost":{"min":3000,"max":15000}
},

{
"id":200,
"problem":"Drive Mode Selector Fault",
"system":"electrical",
"component":"drive mode module",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"drive mode not changing"
],
"user_checks":[
"test drive mode switch"
],
"repair_cost":{"min":2000,"max":10000}
},

# ================= ADVANCED EV SYSTEMS =================

{
"id":201,
"problem":"EV Inverter Cooling Failure",
"system":"ev",
"component":"inverter cooling system",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"inverter temperature warning",
"reduced EV power"
],
"user_checks":[
"check EV cooling warnings"
],
"repair_cost":{"min":15000,"max":70000}
},

{
"id":202,
"problem":"EV DC-DC Converter Failure",
"system":"ev",
"component":"DC-DC converter",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"12V battery not charging",
"electrical systems shutting down"
],
"user_checks":[
"check 12V battery voltage"
],
"repair_cost":{"min":20000,"max":80000}
},

{
"id":203,
"problem":"EV Regenerative Braking Sensor Fault",
"system":"ev",
"component":"regen braking sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"regen braking reduced"
],
"user_checks":[
"observe braking energy recovery"
],
"repair_cost":{"min":6000,"max":20000}
},

{
"id":204,
"problem":"EV Motor Position Sensor Fault",
"system":"ev",
"component":"motor position sensor",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"EV acceleration irregular"
],
"user_checks":[
"scan EV diagnostic codes"
],
"repair_cost":{"min":15000,"max":70000}
},

{
"id":205,
"problem":"EV Charging Communication Error",
"system":"ev",
"component":"charging communication module",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"charging station not detected"
],
"user_checks":[
"try another charging station"
],
"repair_cost":{"min":5000,"max":20000}
},

# ================= ADAS CALIBRATION =================

{
"id":206,
"problem":"ADAS Camera Calibration Error",
"system":"ADAS",
"component":"front camera",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"lane assist unavailable"
],
"user_checks":[
"check windshield cleanliness"
],
"repair_cost":{"min":6000,"max":25000}
},

{
"id":207,
"problem":"Radar Sensor Misalignment",
"system":"ADAS",
"component":"radar sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"adaptive cruise warning"
],
"user_checks":[
"inspect radar mounting area"
],
"repair_cost":{"min":7000,"max":30000}
},

{
"id":208,
"problem":"Parking Assist ECU Fault",
"system":"ADAS",
"component":"parking ECU",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"parking assist unavailable"
],
"user_checks":[
"test parking assist function"
],
"repair_cost":{"min":5000,"max":20000}
},

{
"id":209,
"problem":"Blind Spot Monitoring Module Fault",
"system":"ADAS",
"component":"blind spot module",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"blind spot warning unavailable"
],
"user_checks":[
"inspect side sensors"
],
"repair_cost":{"min":8000,"max":35000}
},

{
"id":210,
"problem":"Traffic Sign Recognition Fault",
"system":"ADAS",
"component":"traffic sign recognition camera",
"severity":"low",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"traffic sign display missing"
],
"user_checks":[
"clean windshield camera area"
],
"repair_cost":{"min":6000,"max":25000}
},

# ================= LIGHTING SYSTEM =================

{
"id":211,
"problem":"LED Headlight Driver Failure",
"system":"electrical",
"component":"LED driver module",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"LED headlight not working"
],
"user_checks":[
"inspect headlight wiring"
],
"repair_cost":{"min":4000,"max":20000}
},

{
"id":212,
"problem":"Adaptive Headlight Motor Fault",
"system":"electrical",
"component":"headlight motor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"headlight direction not adjusting"
],
"user_checks":[
"test headlight leveling"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":213,
"problem":"Daytime Running Light Failure",
"system":"electrical",
"component":"DRL module",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"DRL not working"
],
"user_checks":[
"inspect DRL fuse"
],
"repair_cost":{"min":1000,"max":5000}
},

{
"id":214,
"problem":"Tail Lamp Control Module Fault",
"system":"electrical",
"component":"tail lamp module",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"rear lights malfunction"
],
"user_checks":[
"inspect rear light wiring"
],
"repair_cost":{"min":2000,"max":8000}
},

{
"id":215,
"problem":"Ambient Interior Lighting Failure",
"system":"electrical",
"component":"ambient light module",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"ambient lighting not working"
],
"user_checks":[
"check lighting settings"
],
"repair_cost":{"min":1500,"max":6000}
},

# ================= HVAC AIRFLOW =================

{
"id":216,
"problem":"Cabin Air Distribution Door Jam",
"system":"ac",
"component":"air distribution door",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"airflow stuck in one direction"
],
"user_checks":[
"change airflow settings"
],
"repair_cost":{"min":3000,"max":9000}
},

{
"id":217,
"problem":"HVAC Control Module Failure",
"system":"ac",
"component":"HVAC control module",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"AC controls not responding"
],
"user_checks":[
"restart infotainment system"
],
"repair_cost":{"min":6000,"max":20000}
},

{
"id":218,
"problem":"Cabin Temperature Sensor Fault",
"system":"ac",
"component":"temperature sensor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"incorrect cabin temperature reading"
],
"user_checks":[
"observe AC cooling pattern"
],
"repair_cost":{"min":1500,"max":5000}
},

{
"id":219,
"problem":"Rear AC Blower Failure",
"system":"ac",
"component":"rear blower motor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"rear AC airflow weak"
],
"user_checks":[
"test rear AC blower"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":220,
"problem":"AC Compressor Clutch Failure",
"system":"ac",
"component":"compressor clutch",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"AC compressor not engaging"
],
"user_checks":[
"observe compressor clutch engagement"
],
"repair_cost":{"min":4000,"max":15000}
},

# ================= SECURITY =================

{
"id":221,
"problem":"Alarm System Fault",
"system":"security",
"component":"alarm module",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"alarm triggering randomly"
],
"user_checks":[
"check door sensors"
],
"repair_cost":{"min":2000,"max":10000}
},

{
"id":222,
"problem":"Remote Start System Failure",
"system":"security",
"component":"remote start module",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"remote start not working"
],
"user_checks":[
"test remote start feature"
],
"repair_cost":{"min":4000,"max":15000}
},

{
"id":223,
"problem":"Immobilizer Key Recognition Error",
"system":"security",
"component":"immobilizer antenna",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"car not recognizing key"
],
"user_checks":[
"try spare key"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":224,
"problem":"Smart Key Proximity Sensor Fault",
"system":"security",
"component":"proximity sensor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"keyless entry not detecting key"
],
"user_checks":[
"replace key battery"
],
"repair_cost":{"min":2000,"max":9000}
},

{
"id":225,
"problem":"Door Handle Touch Sensor Failure",
"system":"security",
"component":"touch sensor",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"touch unlock not working"
],
"user_checks":[
"test door handle sensor"
],
"repair_cost":{"min":2000,"max":8000}
},

# ================= STEERING ELECTRONICS =================

{
"id":226,
"problem":"Electric Power Steering Motor Failure",
"system":"steering",
"component":"EPS motor",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"steering suddenly heavy",
"EPS warning light"
],
"user_checks":[
"restart vehicle and check EPS warning"
],
"repair_cost":{"min":10000,"max":50000}
},

{
"id":227,
"problem":"Steering Torque Sensor Fault",
"system":"steering",
"component":"torque sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"inconsistent steering assist"
],
"user_checks":[
"scan steering system codes"
],
"repair_cost":{"min":5000,"max":20000}
},

{
"id":228,
"problem":"Steering ECU Failure",
"system":"steering",
"component":"steering ECU",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"EPS malfunction warning"
],
"user_checks":[
"scan steering ECU diagnostics"
],
"repair_cost":{"min":8000,"max":40000}
},

{
"id":229,
"problem":"Steering Column Lock Fault",
"system":"steering",
"component":"column lock module",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"steering locked warning"
],
"user_checks":[
"restart ignition"
],
"repair_cost":{"min":6000,"max":25000}
},

{
"id":230,
"problem":"Active Steering Calibration Error",
"system":"steering",
"component":"active steering system",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"steering warning message"
],
"user_checks":[
"scan ADAS calibration codes"
],
"repair_cost":{"min":7000,"max":30000}
},

# ================= ELECTRONIC SUSPENSION =================

{
"id":231,
"problem":"Adaptive Suspension Damper Failure",
"system":"suspension",
"component":"adaptive damper",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"ride comfort reduced",
"suspension warning light"
],
"user_checks":[
"inspect suspension behavior"
],
"repair_cost":{"min":10000,"max":50000}
},

{
"id":232,
"problem":"Air Suspension Compressor Failure",
"system":"suspension",
"component":"air compressor",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"vehicle height uneven"
],
"user_checks":[
"observe vehicle ride height"
],
"repair_cost":{"min":15000,"max":70000}
},

{
"id":233,
"problem":"Air Suspension Leak",
"system":"suspension",
"component":"air suspension bag",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"vehicle sagging"
],
"user_checks":[
"inspect air suspension lines"
],
"repair_cost":{"min":10000,"max":50000}
},

{
"id":234,
"problem":"Electronic Ride Height Sensor Fault",
"system":"suspension",
"component":"ride height sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"suspension warning light"
],
"user_checks":[
"scan suspension system codes"
],
"repair_cost":{"min":4000,"max":15000}
},

{
"id":235,
"problem":"Suspension Control Module Failure",
"system":"suspension",
"component":"suspension ECU",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"adaptive suspension not working"
],
"user_checks":[
"scan suspension ECU"
],
"repair_cost":{"min":10000,"max":40000}
},

# ================= HYBRID SYSTEM CONTROL =================

{
"id":236,
"problem":"Hybrid Motor Controller Fault",
"system":"hybrid",
"component":"motor controller",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"hybrid system warning"
],
"user_checks":[
"scan hybrid ECU codes"
],
"repair_cost":{"min":20000,"max":100000}
},

{
"id":237,
"problem":"Hybrid Regenerative Brake Module Fault",
"system":"hybrid",
"component":"regen control module",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"regenerative braking weak"
],
"user_checks":[
"observe braking energy recovery"
],
"repair_cost":{"min":15000,"max":70000}
},

{
"id":238,
"problem":"Hybrid Power Distribution Module Fault",
"system":"hybrid",
"component":"power distribution unit",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"hybrid power delivery irregular"
],
"user_checks":[
"scan hybrid power system codes"
],
"repair_cost":{"min":30000,"max":120000}
},

{
"id":239,
"problem":"Hybrid Drive Motor Cooling Failure",
"system":"hybrid",
"component":"motor cooling system",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"hybrid motor overheating warning"
],
"user_checks":[
"check hybrid cooling warnings"
],
"repair_cost":{"min":20000,"max":80000}
},

{
"id":240,
"problem":"Hybrid Battery Control Module Fault",
"system":"hybrid",
"component":"battery ECU",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"hybrid battery warning"
],
"user_checks":[
"scan hybrid battery codes"
],
"repair_cost":{"min":25000,"max":120000}
},

# ================= INFOTAINMENT =================

{
"id":241,
"problem":"Infotainment Software Crash",
"system":"electrical",
"component":"infotainment software",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"screen freezing"
],
"user_checks":[
"restart infotainment system"
],
"repair_cost":{"min":0,"max":5000}
},

{
"id":242,
"problem":"Bluetooth Connectivity Failure",
"system":"electrical",
"component":"bluetooth module",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"phone not connecting"
],
"user_checks":[
"reset bluetooth pairing"
],
"repair_cost":{"min":0,"max":3000}
},

{
"id":243,
"problem":"GPS Navigation Module Fault",
"system":"electrical",
"component":"GPS module",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"navigation location incorrect"
],
"user_checks":[
"restart navigation system"
],
"repair_cost":{"min":2000,"max":10000}
},

{
"id":244,
"problem":"Apple CarPlay Connection Failure",
"system":"electrical",
"component":"CarPlay interface",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"CarPlay not connecting"
],
"user_checks":[
"change USB cable"
],
"repair_cost":{"min":0,"max":5000}
},

{
"id":245,
"problem":"Android Auto Connection Failure",
"system":"electrical",
"component":"Android Auto interface",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"Android Auto disconnecting"
],
"user_checks":[
"check USB cable"
],
"repair_cost":{"min":0,"max":5000}
},

# ================= VEHICLE NETWORK =================

{
"id":246,
"problem":"Telematics Control Unit Fault",
"system":"electrical",
"component":"TCU module",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"vehicle connectivity lost"
],
"user_checks":[
"restart vehicle connectivity"
],
"repair_cost":{"min":5000,"max":25000}
},

{
"id":247,
"problem":"OTA Update Failure",
"system":"electrical",
"component":"software update module",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"update stuck"
],
"user_checks":[
"restart infotainment system"
],
"repair_cost":{"min":0,"max":2000}
},

{
"id":248,
"problem":"Vehicle Gateway Module Failure",
"system":"electrical",
"component":"gateway module",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"multiple ECU communication errors"
],
"user_checks":[
"scan network diagnostic codes"
],
"repair_cost":{"min":8000,"max":40000}
},

{
"id":249,
"problem":"OBD Communication Error",
"system":"electrical",
"component":"OBD port",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"OBD scanner not connecting"
],
"user_checks":[
"inspect OBD port"
],
"repair_cost":{"min":1000,"max":4000}
},
{
"id":250,
"problem":"Vehicle Software Configuration Error",
"system":"electrical",
"component":"vehicle configuration software",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"features not working correctly"
],
"user_checks":[
"perform system reset"
],
"repair_cost":{"min":2000,"max":15000}
},
# ================= ENGINE INTERNAL FAILURES =================

{
"id":251,
"problem":"Piston Ring Wear",
"system":"engine",
"component":"piston rings",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"blue smoke from exhaust",
"high oil consumption"
],
"user_checks":[
"check engine oil level frequently"
],
"repair_cost":{"min":20000,"max":80000}
},

{
"id":252,
"problem":"Cylinder Compression Loss",
"system":"engine",
"component":"cylinder",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine power loss",
"engine misfire"
],
"user_checks":[
"observe engine power drop"
],
"repair_cost":{"min":15000,"max":70000}
},

{
"id":253,
"problem":"Valve Timing Misalignment",
"system":"engine",
"component":"valve timing system",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"engine rough running"
],
"user_checks":[
"listen for abnormal engine sound"
],
"repair_cost":{"min":10000,"max":40000}
},

{
"id":254,
"problem":"Valve Spring Failure",
"system":"engine",
"component":"valve spring",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"engine misfire"
],
"user_checks":[
"observe engine vibration"
],
"repair_cost":{"min":15000,"max":60000}
},

{
"id":255,
"problem":"Camshaft Wear",
"system":"engine",
"component":"camshaft",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"engine ticking noise"
],
"user_checks":[
"listen for engine ticking sound"
],
"repair_cost":{"min":20000,"max":90000}
},

# ================= RARE DRIVETRAIN =================

{
"id":256,
"problem":"CV Axle Boot Tear",
"system":"drivetrain",
"component":"CV boot",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"grease leak near wheel"
],
"user_checks":[
"inspect axle boot"
],
"repair_cost":{"min":1500,"max":6000}
},

{
"id":257,
"problem":"Drive Shaft Universal Joint Wear",
"system":"drivetrain",
"component":"U-joint",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"clunk noise during acceleration"
],
"user_checks":[
"inspect driveshaft joints"
],
"repair_cost":{"min":4000,"max":15000}
},

{
"id":258,
"problem":"Rear Differential Bearing Failure",
"system":"drivetrain",
"component":"differential bearing",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"whining noise at speed"
],
"user_checks":[
"listen for axle noise"
],
"repair_cost":{"min":15000,"max":60000}
},

{
"id":259,
"problem":"Transfer Case Chain Stretch",
"system":"drivetrain",
"component":"transfer case chain",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"4WD slipping"
],
"user_checks":[
"test 4WD engagement"
],
"repair_cost":{"min":20000,"max":80000}
},

{
"id":260,
"problem":"Differential Lock Actuator Failure",
"system":"drivetrain",
"component":"diff lock actuator",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"differential lock not engaging"
],
"user_checks":[
"test diff lock switch"
],
"repair_cost":{"min":8000,"max":30000}
},

# ================= ELECTRICAL ARCHITECTURE =================

{
"id":261,
"problem":"Battery Ground Connection Loose",
"system":"electrical",
"component":"ground cable",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"random electrical glitches"
],
"user_checks":[
"inspect battery ground cable"
],
"repair_cost":{"min":500,"max":3000}
},

{
"id":262,
"problem":"Alternator Voltage Regulator Fault",
"system":"electrical",
"component":"voltage regulator",
"severity":"high",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"battery warning light"
],
"user_checks":[
"measure charging voltage"
],
"repair_cost":{"min":4000,"max":15000}
},

{
"id":263,
"problem":"Fuse Relay Block Failure",
"system":"electrical",
"component":"relay block",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"multiple accessories not working"
],
"user_checks":[
"inspect relay box"
],
"repair_cost":{"min":2000,"max":10000}
},

{
"id":264,
"problem":"Starter Solenoid Failure",
"system":"electrical",
"component":"starter solenoid",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"engine not cranking"
],
"user_checks":[
"listen for click during ignition"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":265,
"problem":"Alternator Pulley Failure",
"system":"engine",
"component":"alternator pulley",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"squealing belt noise"
],
"user_checks":[
"inspect belt system"
],
"repair_cost":{"min":2000,"max":8000}
},

# ================= SENSOR FUSION =================

{
"id":266,
"problem":"Sensor Data Mismatch",
"system":"electronics",
"component":"sensor fusion module",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"ADAS warnings"
],
"user_checks":[
"scan vehicle diagnostics"
],
"repair_cost":{"min":8000,"max":40000}
},

{
"id":267,
"problem":"Camera Sensor Dirty",
"system":"ADAS",
"component":"front camera",
"severity":"low",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"lane assist disabled"
],
"user_checks":[
"clean windshield camera area"
],
"repair_cost":{"min":0,"max":1000}
},

{
"id":268,
"problem":"Radar Sensor Blocked",
"system":"ADAS",
"component":"radar sensor",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"adaptive cruise unavailable"
],
"user_checks":[
"clean radar sensor area"
],
"repair_cost":{"min":0,"max":1000}
},

{
"id":269,
"problem":"Ultrasonic Parking Sensor Dirty",
"system":"ADAS",
"component":"parking sensor",
"severity":"low",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"parking assist error"
],
"user_checks":[
"clean parking sensors"
],
"repair_cost":{"min":0,"max":500}
},

{
"id":270,
"problem":"Driver Monitoring Camera Fault",
"system":"ADAS",
"component":"driver monitoring camera",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"driver attention warning"
],
"user_checks":[
"inspect camera area"
],
"repair_cost":{"min":5000,"max":20000}
},

# ================= EDGE DIAGNOSTIC CASES =================

{
"id":271,
"problem":"Fuel Cap Not Tight",
"system":"fuel",
"component":"fuel cap",
"severity":"low",
"urgency":"service_soon",
"probability":5,
"symptoms":[
"check engine light"
],
"user_checks":[
"tighten fuel cap"
],
"repair_cost":{"min":0,"max":500}
},

{
"id":272,
"problem":"Loose Engine Mount Bolt",
"system":"engine",
"component":"engine mount bolt",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine vibration"
],
"user_checks":[
"inspect engine mounts"
],
"repair_cost":{"min":1000,"max":5000}
},

{
"id":273,
"problem":"Loose Exhaust Heat Shield",
"system":"exhaust",
"component":"heat shield",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"rattling noise under car"
],
"user_checks":[
"inspect exhaust shield"
],
"repair_cost":{"min":500,"max":2000}
},

{
"id":274,
"problem":"Loose Battery Clamp",
"system":"electrical",
"component":"battery clamp",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"battery movement"
],
"user_checks":[
"inspect battery mounting"
],
"repair_cost":{"min":200,"max":1000}
},

{
"id":275,
"problem":"Loose Wheel Lug Nuts",
"system":"suspension",
"component":"wheel nuts",
"severity":"critical",
"urgency":"stop_driving",
"probability":3,
"symptoms":[
"wheel vibration"
],
"user_checks":[
"inspect wheel nuts"
],
"repair_cost":{"min":0,"max":1000}
},

{
"id":276,
"problem":"Incorrect Tire Size Installed",
"system":"suspension",
"component":"tire",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"speedometer error"
],
"user_checks":[
"check tire size"
],
"repair_cost":{"min":0,"max":5000}
},

{
"id":277,
"problem":"Loose Intake Clamp",
"system":"engine",
"component":"intake clamp",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"hissing sound"
],
"user_checks":[
"inspect intake pipes"
],
"repair_cost":{"min":200,"max":1000}
},

{
"id":278,
"problem":"Loose Ground Wire",
"system":"electrical",
"component":"ground wire",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"random ECU faults"
],
"user_checks":[
"inspect ground wiring"
],
"repair_cost":{"min":500,"max":3000}
},

{
"id":279,
"problem":"ECU Reset Required",
"system":"electrical",
"component":"ECU",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"random warning lights"
],
"user_checks":[
"restart vehicle"
],
"repair_cost":{"min":0,"max":2000}
},

{
"id":280,
"problem":"Temporary Sensor Glitch",
"system":"electronics",
"component":"sensor system",
"severity":"low",
"urgency":"monitor",
"probability":3,
"symptoms":[
"temporary warning message"
],
"user_checks":[
"restart vehicle"
],
"repair_cost":{"min":0,"max":1000}
},

{
"id":281,
"problem":"Loose Wiring Harness",
"system":"electrical",
"component":"wiring harness",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"intermittent electrical faults"
],
"user_checks":[
"inspect wiring harness"
],
"repair_cost":{"min":1000,"max":8000}
},

{
"id":282,
"problem":"ECU Ground Fault",
"system":"electrical",
"component":"ECU ground",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"multiple warning lights"
],
"user_checks":[
"inspect ECU ground connection"
],
"repair_cost":{"min":2000,"max":10000}
},

{
"id":283,
"problem":"Loose Sensor Connector",
"system":"electronics",
"component":"sensor connector",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"sensor error code"
],
"user_checks":[
"inspect sensor connector"
],
"repair_cost":{"min":500,"max":3000}
},

{
"id":284,
"problem":"Low Engine Oil Level",
"system":"engine",
"component":"lubrication system",
"severity":"high",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"oil pressure warning"
],
"user_checks":[
"check oil dipstick"
],
"repair_cost":{"min":500,"max":3000}
},

{
"id":285,
"problem":"Incorrect Fuel Type Used",
"system":"fuel",
"component":"fuel system",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"engine knocking"
],
"user_checks":[
"verify fuel used"
],
"repair_cost":{"min":2000,"max":15000}
},

{
"id":286,
"problem":"Fuel Pump Relay Failure",
"system":"fuel",
"component":"fuel pump relay",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine not starting"
],
"user_checks":[
"inspect fuel pump relay"
],
"repair_cost":{"min":1000,"max":5000}
},

{
"id":287,
"problem":"Throttle Body Stuck",
"system":"engine",
"component":"throttle body",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine RPM stuck"
],
"user_checks":[
"inspect throttle body"
],
"repair_cost":{"min":3000,"max":12000}
},

{
"id":288,
"problem":"Mass Airflow Sensor Dirty",
"system":"engine",
"component":"MAF sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"poor acceleration"
],
"user_checks":[
"clean MAF sensor"
],
"repair_cost":{"min":1500,"max":6000}
},

{
"id":289,
"problem":"Oxygen Sensor Dirty",
"system":"engine",
"component":"O2 sensor",
"severity":"medium",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"poor fuel economy"
],
"user_checks":[
"scan OBD codes"
],
"repair_cost":{"min":2500,"max":9000}
},

{
"id":290,
"problem":"Spark Plug Wire Damage",
"system":"engine",
"component":"spark plug wire",
"severity":"medium",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"engine misfire"
],
"user_checks":[
"inspect ignition wires"
],
"repair_cost":{"min":1500,"max":7000}
},

{
"id":291,
"problem":"Ignition Module Failure",
"system":"engine",
"component":"ignition module",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"engine stall"
],
"user_checks":[
"scan ignition system codes"
],
"repair_cost":{"min":5000,"max":20000}
},

{
"id":292,
"problem":"ECU Firmware Corruption",
"system":"electrical",
"component":"ECU firmware",
"severity":"high",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"vehicle malfunction warnings"
],
"user_checks":[
"scan ECU software"
],
"repair_cost":{"min":5000,"max":30000}
},

{
"id":293,
"problem":"Battery Management Calibration Error",
"system":"electrical",
"component":"battery ECU",
"severity":"medium",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"battery level incorrect"
],
"user_checks":[
"restart vehicle"
],
"repair_cost":{"min":2000,"max":8000}
},

{
"id":294,
"problem":"Climate Control Calibration Error",
"system":"ac",
"component":"climate ECU",
"severity":"low",
"urgency":"service_soon",
"probability":2,
"symptoms":[
"temperature incorrect"
],
"user_checks":[
"reset climate control"
],
"repair_cost":{"min":1000,"max":5000}
},

{
"id":295,
"problem":"Body Panel Loose",
"system":"body",
"component":"body panel",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"panel vibration noise"
],
"user_checks":[
"inspect body panels"
],
"repair_cost":{"min":500,"max":5000}
},

{
"id":296,
"problem":"Windshield Seal Leak",
"system":"body",
"component":"windshield seal",
"severity":"low",
"urgency":"service_soon",
"probability":3,
"symptoms":[
"water entering cabin"
],
"user_checks":[
"inspect windshield seal"
],
"repair_cost":{"min":2000,"max":8000}
},

{
"id":297,
"problem":"Door Seal Worn",
"system":"body",
"component":"door seal",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"wind noise"
],
"user_checks":[
"inspect door rubber seals"
],
"repair_cost":{"min":1000,"max":5000}
},

{
"id":298,
"problem":"Loose Interior Trim",
"system":"body",
"component":"interior trim",
"severity":"low",
"urgency":"service_soon",
"probability":4,
"symptoms":[
"rattling inside cabin"
],
"user_checks":[
"inspect dashboard trim"
],
"repair_cost":{"min":500,"max":3000}
},

{
"id":299,
"problem":"Dashboard Warning Sensor Fault",
"system":"electronics",
"component":"dashboard sensor",
"severity":"low",
"urgency":"monitor",
"probability":2,
"symptoms":[
"random warning message"
],
"user_checks":[
"restart vehicle"
],
"repair_cost":{"min":0,"max":2000}
},

{
"id":300,
"problem":"Unknown Intermittent Electrical Fault",
"system":"electrical",
"component":"vehicle electrical system",
"severity":"medium",
"urgency":"service_soon",
"probability":1,
"symptoms":[
"intermittent vehicle malfunction"
],
"user_checks":[
"perform full vehicle diagnostics"
],
"repair_cost":{"min":3000,"max":20000}
},]