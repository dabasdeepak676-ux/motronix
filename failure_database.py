# failure_database.py

FAILURE_DATABASE = [

{
"id":1,
"problem":"Battery Dead",
"system":"electrical",
"component":"battery",
"severity":"medium",
"urgency":"service_soon",

"probability":5,

"symptoms":[
"car not starting",
"clicking sound while starting",
"dashboard lights dim",
"engine not cranking"
],

"possible_causes":[
"battery discharged",
"battery terminals loose",
"battery old",
"alternator not charging"
],

"user_checks":[
"check if dashboard lights are dim",
"check if car makes clicking sound while starting",
"check if headlights are weak"
],

"user_actions":[
"try jump starting the car",
"avoid turning on electrical accessories",
"visit nearest service center"
],

"mechanic_checks":[
"check battery voltage using multimeter",
"inspect battery terminals corrosion",
"test alternator charging output"
],

"repair_cost":{
"min":2000,
"max":6000
}
},

{
"id":2,
"problem":"Starter Motor Failure",
"system":"electrical",
"component":"starter motor",
"severity":"high",
"urgency":"service_soon",

"probability":4,

"symptoms":[
"car not starting",
"single click sound",
"engine not cranking"
],

"possible_causes":[
"starter motor faulty",
"starter relay problem",
"wiring issue"
],

"user_checks":[
"check if clicking sound comes when starting",
"check if dashboard lights are normal"
],

"user_actions":[
"try starting car again after few seconds",
"avoid repeated cranking"
],

"mechanic_checks":[
"check starter relay",
"test starter motor current",
"inspect wiring"
],

"repair_cost":{
"min":3000,
"max":8000
}
},

{
"id":3,
"problem":"Alternator Failure",
"system":"electrical",
"component":"alternator",
"severity":"high",
"urgency":"service_soon",

"probability":3,

"symptoms":[
"battery warning light",
"car battery draining",
"headlights dim"
],

"possible_causes":[
"alternator not charging",
"drive belt loose",
"voltage regulator failure"
],

"user_checks":[
"check if battery warning light is on",
"check if headlights become dim"
],

"user_actions":[
"avoid long driving",
"visit service center soon"
],

"mechanic_checks":[
"measure charging voltage",
"inspect alternator belt"
],

"repair_cost":{
"min":4000,
"max":12000
}
},

{
"id":4,
"problem":"Engine Overheating",
"system":"cooling",
"component":"cooling system",
"severity":"critical",
"urgency":"stop_driving",

"probability":4,

"symptoms":[
"temperature gauge high",
"steam from bonnet",
"coolant warning light"
],

"possible_causes":[
"low coolant",
"radiator fan failure",
"water pump issue",
"thermostat stuck"
],

"user_checks":[
"check if temperature gauge is high",
"check if coolant level is low"
],

"user_actions":[
"stop the car immediately",
"turn off AC",
"allow engine to cool"
],

"mechanic_checks":[
"check coolant level",
"inspect radiator fan",
"check coolant leakage"
],

"repair_cost":{
"min":2000,
"max":15000
}
},

{
"id":5,
"problem":"Brake Pad Wear",
"system":"brake",
"component":"brake pads",
"severity":"medium",
"urgency":"service_soon",

"probability":5,

"symptoms":[
"squeaking while braking",
"brake noise",
"reduced braking performance"
],

"possible_causes":[
"brake pads worn",
"brake pads thin",
"brake pads contaminated"
],

"user_checks":[
"check if noise happens only while braking",
"check if braking performance reduced"
],

"user_actions":[
"avoid hard braking",
"visit service center"
],

"mechanic_checks":[
"inspect brake pads",
"check brake disc condition"
],

"repair_cost":{
"min":2500,
"max":7000
}
},

{
"id":14,
"problem":"Spark Plug Failure",
"system":"engine",
"component":"spark plug",
"severity":"medium",
"urgency":"service_soon",

"probability":5,

"symptoms":[
"engine misfire",
"engine shaking",
"engine shaking",
"poor fuel economy",
"difficulty starting"
],

"possible_causes":[
"spark plug worn",
"spark plug carbon deposit"
],

"user_checks":[
"check if engine struggles to start"
],

"user_actions":[
"avoid aggressive driving"
],

"mechanic_checks":[
"inspect spark plugs",
"check spark plug gap"
],

"repair_cost":{
"min":1000,
"max":4000
}
},

{
"id":15,
"problem":"Ignition Coil Failure",
"system":"engine",
"component":"ignition coil",
"severity":"high",
"urgency":"service_soon",

"probability":5,

"symptoms":[
"engine misfire",
"check engine light"
"loss of power"
],

"possible_causes":[
"ignition coil damaged",
"coil wiring fault"
],

"user_checks":[
"check if engine shakes during acceleration"
],

"user_actions":[
"avoid driving at high RPM"
],

"mechanic_checks":[
"scan obd codes",
"test ignition coil"
],

"repair_cost":{
"min":2000,
"max":8000
}
},
{
"id":16,
"problem":"Brake Pad Wear",
"system":"brake",
"component":"brake pads",
"severity":"medium",
"urgency":"service_soon",

"symptoms":[
"squeaking noise while braking",
"grinding noise during braking",
"reduced braking performance"
],

"possible_causes":[
"brake pads worn",
"thin brake pad material",
"metal contact with brake disc"
],

"user_checks":[
"check if noise occurs while braking",
"check if braking distance increased"
],

"user_actions":[
"avoid sudden braking",
"visit service center for inspection"
],

"mechanic_checks":[
"inspect brake pad thickness",
"check brake disc condition"
],

"repair_cost":{
"min":2500,
"max":7000
}
},

{
"id":17,
"problem":"Brake Disc Warped",
"system":"brake",
"component":"brake disc",
"severity":"medium",
"urgency":"service_soon",

"symptoms":[
"vibration while braking",
"steering vibration during braking",
"uneven braking feel"
],

"possible_causes":[
"brake disc overheating",
"disc surface uneven",
"heavy braking repeatedly"
],

"user_checks":[
"check if steering vibrates during braking",
"check if vibration increases at high speed braking"
],

"user_actions":[
"avoid high speed braking",
"visit service center soon"
],

"mechanic_checks":[
"measure brake disc runout",
"inspect disc surface"
],

"repair_cost":{
"min":4000,
"max":12000
}
},

{
"id":18,
"problem":"Brake Pad Glazing",
"system":"brake",
"component":"brake pads",
"severity":"medium",
"urgency":"service_soon",

"symptoms":[
"hard brake pedal",
"reduced braking power",
"squeaking brake noise"
],

"possible_causes":[
"overheated brake pads",
"brake pads hardened surface"
],

"user_checks":[
"check if braking feels weak",
"check if brake pedal feels hard"
],

"user_actions":[
"avoid aggressive braking",
"visit service center"
],

"mechanic_checks":[
"inspect brake pad surface",
"check brake disc condition"
],

"repair_cost":{
"min":2500,
"max":6000
}
},

{
"id":19,
"problem":"Brake Dust Accumulation",
"system":"brake",
"component":"brake pads",
"severity":"low",
"urgency":"service_soon",

"symptoms":[
"squeaking noise while braking",
"black dust on wheels"
],

"possible_causes":[
"brake dust accumulation",
"dust between pad and disc"
],

"user_checks":[
"check for black dust on wheel rim",
"check if noise occurs at low speed braking"
],

"user_actions":[
"clean brake area",
"visit service center if noise continues"
],

"mechanic_checks":[
"clean brake assembly",
"inspect brake pads"
],

"repair_cost":{
"min":500,
"max":2000
}
},

{
"id":20,
"problem":"Brake Caliper Stuck",
"system":"brake",
"component":"brake caliper",
"severity":"high",
"urgency":"service_soon",

"symptoms":[
"car pulling to one side while braking",
"uneven brake pad wear",
"brake overheating"
],

"possible_causes":[
"caliper piston stuck",
"brake caliper slide jammed"
],

"user_checks":[
"check if car pulls to one side during braking"
],

"user_actions":[
"avoid driving long distance",
"visit mechanic immediately"
],

"mechanic_checks":[
"inspect caliper piston movement",
"check brake caliper slide pins"
],

"repair_cost":{
"min":2000,
"max":8000
}
},
{
"id":21,
"problem":"Clogged Air Filter",

"system":"engine",
"component":"air intake",

"symptoms":[
"loss of power",
"poor acceleration",
"engine feels restricted",
"reduced fuel efficiency"
],

"possible_causes":[
"air filter clogged with dust",
"air filter overdue for replacement"
],

"user_checks":[
"check air filter condition",
"inspect if filter is dirty"
],

"repair_cost":{"min":300,"max":1500},

"probability":4
},

{
"id":22,
"problem":"Dirty Throttle Body",

"system":"engine",
"component":"throttle body",

"symptoms":[
"rough idle",
"engine hesitation",
"engine stalls at idle",
"delayed acceleration"
],

"possible_causes":[
"carbon buildup on throttle plate",
"dirty throttle body"
],

"user_checks":[
"observe unstable idle RPM",
"check throttle body cleanliness"
],

"repair_cost":{"min":1500,"max":4000},

"probability":4
},

{
"id":23,
"problem":"Fuel Injector Clogged",

"system":"fuel",
"component":"fuel injector",

"symptoms":[
"engine misfire",
"loss of power",
"poor fuel economy",
"engine vibration"
],

"possible_causes":[
"fuel injector clogged",
"dirty fuel system"
],

"user_checks":[
"check if engine misfires during acceleration"
],

"repair_cost":{"min":2500,"max":7000},

"probability":4
},

{
"id":24,
"problem":"MAF Sensor Fault",

"system":"engine",
"component":"maf sensor",

"symptoms":[
"engine hesitation",
"poor acceleration",
"engine stalling",
"check engine light"
],

"possible_causes":[
"dirty MAF sensor",
"MAF sensor failure"
],

"user_checks":[
"scan OBD codes",
"check engine performance"
],

"repair_cost":{"min":3000,"max":9000},

"probability":4
},

{
"id":25,
"problem":"Spark Plug Worn",

"system":"engine",
"component":"spark plug",

"symptoms":[
"engine misfire",
"rough engine idle",
"difficulty starting engine",
"loss of power"
],

"possible_causes":[
"spark plug worn",
"spark plug gap increased"
],

"user_checks":[
"check service history",
"inspect spark plugs"
],

"repair_cost":{"min":800,"max":3000},

"probability":5
},

{
"id":26,
"problem":"Ignition Coil Failure",

"system":"engine",
"component":"ignition coil",

"symptoms":[
"engine misfire",
"check engine light",
"loss of power"
"engine vibration"
],

"possible_causes":[
"ignition coil failure",
"weak ignition spark"
],

"user_checks":[
"scan OBD codes",
"check misfire symptoms"
],

"repair_cost":{"min":2000,"max":6000},

"probability":4
},

{
"id":27,
"problem":"EGR Valve Blocked",

"system":"engine",
"component":"EGR valve",

"symptoms":[
"rough idle",
"engine knocking",
"engine hesitation",
"poor fuel economy"
],

"possible_causes":[
"EGR valve clogged",
"carbon buildup in EGR valve"
],

"user_checks":[
"check engine performance",
"scan OBD codes"
],

"repair_cost":{"min":2500,"max":7000},

"probability":3
},

{
"id":28,
"problem":"Timing Chain Noise",

"system":"engine",
"component":"timing chain",

"symptoms":[
"rattling noise from engine",
"engine noise at startup",
"engine timing issues"
],

"possible_causes":[
"timing chain worn",
"timing chain tensioner failure"
],

"user_checks":[
"listen for rattling noise during startup"
],

"repair_cost":{"min":8000,"max":25000},

"probability":3
},

{
"id":29,
"problem":"Engine Vacuum Leak",

"system":"engine",
"component":"vacuum system",

"symptoms":[
"rough idle",
"engine hesitation",
"high idle RPM",
"poor fuel economy"
],

"possible_causes":[
"vacuum hose leak",
"intake manifold gasket leak"
],

"user_checks":[
"listen for hissing sound from engine"
],

"repair_cost":{"min":1500,"max":8000},

"probability":3
},

{
"id":30,
"problem":"Engine Overheating",

"system":"cooling",
"component":"cooling system",

"symptoms":[
"temperature gauge high",
"engine overheating warning",
"steam from engine bay"
],

"possible_causes":[
"coolant low",
"radiator blocked",
"cooling fan failure"
],

"user_checks":[
"check coolant level",
"inspect radiator fan operation"
],

"repair_cost":{"min":2000,"max":15000},

"probability":5
},
{
"id":31,
"problem":"Thermostat Stuck Closed",

"system":"cooling",
"component":"thermostat",

"symptoms":[
"engine overheating",
"temperature gauge rising quickly",
"coolant boiling",
"heater not working properly"
],

"possible_causes":[
"thermostat stuck closed",
"coolant circulation blocked"
],

"user_checks":[
"check if temperature rises quickly after start",
"inspect coolant flow"
],

"repair_cost":{"min":2000,"max":6000},

"probability":4
},

{
"id":32,
"problem":"Radiator Fan Failure",

"system":"cooling",
"component":"cooling fan",

"symptoms":[
"engine overheating in traffic",
"temperature normal on highway",
"fan not spinning"
],

"possible_causes":[
"cooling fan motor failure",
"fan relay fault"
],

"user_checks":[
"check if radiator fan spins when engine hot"
],

"repair_cost":{"min":2500,"max":8000},

"probability":4
},

{
"id":33,
"problem":"Low Coolant Level",

"system":"cooling",
"component":"coolant system",

"symptoms":[
"engine overheating",
"low coolant warning",
"heater not producing heat"
],

"possible_causes":[
"coolant leak",
"evaporation over time"
],

"user_checks":[
"check coolant reservoir level"
],

"repair_cost":{"min":500,"max":3000},

"probability":5
},

{
"id":34,
"problem":"Radiator Blocked",

"system":"cooling",
"component":"radiator",

"symptoms":[
"engine overheating",
"coolant temperature high",
"poor cooling efficiency"
],

"possible_causes":[
"radiator clogged",
"coolant contamination"
],

"user_checks":[
"inspect radiator fins and coolant flow"
],

"repair_cost":{"min":3000,"max":12000},

"probability":3
},

{
"id":35,
"problem":"Water Pump Failure",

"system":"cooling",
"component":"water pump",

"symptoms":[
"engine overheating",
"coolant leak near pump",
"whining noise from engine"
],

"possible_causes":[
"water pump bearing failure",
"water pump seal leak"
],

"user_checks":[
"inspect coolant leakage near pump area"
],

"repair_cost":{"min":4000,"max":15000},

"probability":3
},

{
"id":36,
"problem":"Battery Weak",

"system":"electrical",
"component":"battery",

"symptoms":[
"slow engine cranking",
"dim headlights",
"battery warning light"
],

"possible_causes":[
"battery aging",
"battery charge low"
],

"user_checks":[
"check battery voltage",
"inspect battery terminals"
],

"repair_cost":{"min":3000,"max":8000},

"probability":5
},

{
"id":37,
"problem":"Alternator Failure",

"system":"electrical",
"component":"alternator",

"symptoms":[
"battery warning light",
"battery draining quickly",
"electrical systems malfunction"
],

"possible_causes":[
"alternator failure",
"charging system malfunction"
],

"user_checks":[
"check battery voltage while engine running"
],

"repair_cost":{"min":5000,"max":15000},

"probability":4
},

{
"id":38,
"problem":"Starter Motor Failure",

"system":"electrical",
"component":"starter motor",

"symptoms":[
"engine not cranking",
"clicking sound when starting",
"car not starting"
],

"possible_causes":[
"starter motor failure",
"starter solenoid fault"
],

"user_checks":[
"listen for clicking sound during ignition"
],

"repair_cost":{"min":4000,"max":12000},

"probability":4
},

{
"id":39,
"problem":"Loose Battery Terminal",

"system":"electrical",
"component":"battery terminal",

"symptoms":[
"car not starting",
"intermittent electrical failure",
"dashboard flickering"
],

"possible_causes":[
"loose battery terminal",
"corroded battery connection"
],

"user_checks":[
"inspect battery terminals"
],

"repair_cost":{"min":200,"max":800},

"probability":5
},

{
"id":40,
"problem":"Head Gasket Leak",

"system":"engine",
"component":"head gasket",

"symptoms":[
"white smoke from exhaust",
"engine overheating",
"coolant loss"
],

"possible_causes":[
"head gasket blown",
"engine overheating damage"
],

"user_checks":[
"check coolant level frequently",
"observe exhaust smoke"
],

"repair_cost":{"min":20000,"max":60000},

"probability":2
},
{
"id":41,
"problem":"Brake Pad Wear",

"system":"brake",
"component":"brake pads",

"symptoms":[
"squeaking while braking",
"reduced braking performance",
"grinding noise while braking"
],

"possible_causes":[
"brake pads worn",
"brake pad material finished"
],

"user_checks":[
"inspect brake pad thickness",
"listen for noise during braking"
],

"repair_cost":{"min":2500,"max":7000},

"probability":5
},

{
"id":42,
"problem":"Brake Disc Warped",

"system":"brake",
"component":"brake disc",

"symptoms":[
"steering vibration during braking",
"pulsation in brake pedal",
"uneven braking"
],

"possible_causes":[
"brake disc warped due to heat",
"uneven brake disc surface"
],

"user_checks":[
"check vibration while braking"
],

"repair_cost":{"min":4000,"max":12000},

"probability":4
},

{
"id":43,
"problem":"Brake Fluid Low",

"system":"brake",
"component":"brake fluid system",

"symptoms":[
"soft brake pedal",
"brake warning light",
"reduced braking power"
],

"possible_causes":[
"brake fluid leak",
"brake fluid level low"
],

"user_checks":[
"check brake fluid reservoir"
],

"repair_cost":{"min":500,"max":3000},

"probability":5
},

{
"id":44,
"problem":"Brake Caliper Stuck",

"system":"brake",
"component":"brake caliper",

"symptoms":[
"car pulling to one side",
"uneven brake wear",
"brake overheating"
],

"possible_causes":[
"caliper piston stuck",
"caliper slide pins seized"
],

"user_checks":[
"check wheel heat after driving"
],

"repair_cost":{"min":3000,"max":10000},

"probability":4
},

{
"id":45,
"problem":"Brake Hose Leak",

"system":"brake",
"component":"brake hose",

"symptoms":[
"brake fluid leak",
"soft brake pedal",
"braking power reduced"
],

"possible_causes":[
"brake hose crack",
"brake hose damage"
],

"user_checks":[
"inspect brake lines for leakage"
],

"repair_cost":{"min":2000,"max":6000},

"probability":3
},

{
"id":46,
"problem":"Shock Absorber Worn",

"system":"suspension",
"component":"shock absorber",

"symptoms":[
"car bouncing after bumps",
"poor ride comfort",
"excessive body roll"
],

"possible_causes":[
"shock absorber worn",
"shock absorber oil leakage"
],

"user_checks":[
"perform bounce test on vehicle"
],

"repair_cost":{"min":4000,"max":15000},

"probability":4
},

{
"id":47,
"problem":"Suspension Bush Wear",

"system":"suspension",
"component":"suspension bush",

"symptoms":[
"clunk noise on bumps",
"loose steering feel",
"vibration while driving"
],

"possible_causes":[
"suspension bush worn",
"rubber bush deterioration"
],

"user_checks":[
"inspect bushings under vehicle"
],

"repair_cost":{"min":1500,"max":6000},

"probability":4
},

{
"id":48,
"problem":"Wheel Bearing Failure",

"system":"suspension",
"component":"wheel bearing",

"symptoms":[
"humming noise while driving",
"noise increasing with speed",
"wheel vibration"
],

"possible_causes":[
"wheel bearing worn",
"bearing lubrication failure"
],

"user_checks":[
"listen for humming noise from wheel area"
],

"repair_cost":{"min":3000,"max":10000},

"probability":4
},

{
"id":49,
"problem":"Tie Rod End Wear",

"system":"steering",
"component":"tie rod",

"symptoms":[
"loose steering",
"uneven tire wear",
"clunk noise while turning"
],

"possible_causes":[
"tie rod joint wear",
"steering linkage looseness"
],

"user_checks":[
"inspect steering play"
],

"repair_cost":{"min":2500,"max":8000},

"probability":4
},

{
"id":50,
"problem":"Power Steering Fluid Low",

"system":"steering",
"component":"power steering system",

"symptoms":[
"hard steering",
"whining noise while turning",
"steering jerks"
],

"possible_causes":[
"power steering fluid low",
"power steering leak"
],

"user_checks":[
"check power steering fluid level"
],

"repair_cost":{"min":500,"max":4000},

"probability":4
},
{
"id":41,
"problem":"Brake Pad Wear",

"system":"brake",
"component":"brake pads",

"symptoms":[
"squeaking while braking",
"reduced braking performance",
"grinding noise while braking"
],

"possible_causes":[
"brake pads worn",
"brake pad material finished"
],

"user_checks":[
"inspect brake pad thickness",
"listen for noise during braking"
],

"repair_cost":{"min":2500,"max":7000},

"probability":5
},

{
"id":42,
"problem":"Brake Disc Warped",

"system":"brake",
"component":"brake disc",

"symptoms":[
"steering vibration during braking",
"pulsation in brake pedal",
"uneven braking"
],

"possible_causes":[
"brake disc warped due to heat",
"uneven brake disc surface"
],

"user_checks":[
"check vibration while braking"
],

"repair_cost":{"min":4000,"max":12000},

"probability":4
},

{
"id":43,
"problem":"Brake Fluid Low",

"system":"brake",
"component":"brake fluid system",

"symptoms":[
"soft brake pedal",
"brake warning light",
"reduced braking power"
],

"possible_causes":[
"brake fluid leak",
"brake fluid level low"
],

"user_checks":[
"check brake fluid reservoir"
],

"repair_cost":{"min":500,"max":3000},

"probability":5
},

{
"id":44,
"problem":"Brake Caliper Stuck",

"system":"brake",
"component":"brake caliper",

"symptoms":[
"car pulling to one side",
"uneven brake wear",
"brake overheating"
],

"possible_causes":[
"caliper piston stuck",
"caliper slide pins seized"
],

"user_checks":[
"check wheel heat after driving"
],

"repair_cost":{"min":3000,"max":10000},

"probability":4
},

{
"id":45,
"problem":"Brake Hose Leak",

"system":"brake",
"component":"brake hose",

"symptoms":[
"brake fluid leak",
"soft brake pedal",
"braking power reduced"
],

"possible_causes":[
"brake hose crack",
"brake hose damage"
],

"user_checks":[
"inspect brake lines for leakage"
],

"repair_cost":{"min":2000,"max":6000},

"probability":3
},

{
"id":46,
"problem":"Shock Absorber Worn",

"system":"suspension",
"component":"shock absorber",

"symptoms":[
"car bouncing after bumps",
"poor ride comfort",
"excessive body roll"
],

"possible_causes":[
"shock absorber worn",
"shock absorber oil leakage"
],

"user_checks":[
"perform bounce test on vehicle"
],

"repair_cost":{"min":4000,"max":15000},

"probability":4
},

{
"id":47,
"problem":"Suspension Bush Wear",

"system":"suspension",
"component":"suspension bush",

"symptoms":[
"clunk noise on bumps",
"loose steering feel",
"vibration while driving"
],

"possible_causes":[
"suspension bush worn",
"rubber bush deterioration"
],

"user_checks":[
"inspect bushings under vehicle"
],

"repair_cost":{"min":1500,"max":6000},

"probability":4
},

{
"id":48,
"problem":"Wheel Bearing Failure",

"system":"suspension",
"component":"wheel bearing",

"symptoms":[
"humming noise while driving",
"noise increasing with speed",
"wheel vibration"
],

"possible_causes":[
"wheel bearing worn",
"bearing lubrication failure"
],

"user_checks":[
"listen for humming noise from wheel area"
],

"repair_cost":{"min":3000,"max":10000},

"probability":4
},

{
"id":49,
"problem":"Tie Rod End Wear",

"system":"steering",
"component":"tie rod",

"symptoms":[
"loose steering",
"uneven tire wear",
"clunk noise while turning"
],

"possible_causes":[
"tie rod joint wear",
"steering linkage looseness"
],

"user_checks":[
"inspect steering play"
],

"repair_cost":{"min":2500,"max":8000},

"probability":4
},

{
"id":50,
"problem":"Power Steering Fluid Low",

"system":"steering",
"component":"power steering system",

"symptoms":[
"hard steering",
"whining noise while turning",
"steering jerks"
],

"possible_causes":[
"power steering fluid low",
"power steering leak"
],

"user_checks":[
"check power steering fluid level"
],

"repair_cost":{"min":500,"max":4000},

"probability":4
},
{
"id":51,
"problem":"Clutch Plate Worn",

"system":"transmission",
"component":"clutch plate",

"symptoms":[
"engine revs high but speed not increasing",
"burning smell from clutch",
"difficulty accelerating"
],

"possible_causes":[
"clutch plate worn",
"clutch friction material finished"
],

"user_checks":[
"check if engine RPM increases without speed increase"
],

"repair_cost":{"min":6000,"max":20000},

"probability":5
},

{
"id":52,
"problem":"Clutch Cable Loose",

"system":"transmission",
"component":"clutch cable",

"symptoms":[
"clutch pedal feels loose",
"gear shifting difficult",
"clutch not disengaging fully"
],

"possible_causes":[
"clutch cable stretched",
"clutch cable adjustment incorrect"
],

"user_checks":[
"check clutch pedal free play"
],

"repair_cost":{"min":800,"max":3000},

"probability":4
},

{
"id":53,
"problem":"Gearbox Oil Low",

"system":"transmission",
"component":"gearbox",

"symptoms":[
"gear shifting hard",
"gearbox noise",
"gear grinding sound"
],

"possible_causes":[
"gearbox oil level low",
"gearbox oil leak"
],

"user_checks":[
"check gearbox oil level"
],

"repair_cost":{"min":800,"max":4000},

"probability":4
},

{
"id":54,
"problem":"Gear Synchronizer Wear",

"system":"transmission",
"component":"gear synchronizer",

"symptoms":[
"gear grinding while shifting",
"difficulty shifting gears",
"gear slipping"
],

"possible_causes":[
"synchronizer worn",
"gearbox internal wear"
],

"user_checks":[
"check if grinding occurs while shifting"
],

"repair_cost":{"min":10000,"max":35000},

"probability":3
},

{
"id":55,
"problem":"AC Gas Low",

"system":"ac",
"component":"ac refrigerant",

"symptoms":[
"ac not cooling properly",
"weak cooling from vents",
"ac compressor cycling frequently"
],

"possible_causes":[
"refrigerant level low",
"ac system leak"
],

"user_checks":[
"check cooling performance"
],

"repair_cost":{"min":1500,"max":4000},

"probability":5
},

{
"id":56,
"problem":"AC Compressor Failure",

"system":"ac",
"component":"ac compressor",

"symptoms":[
"ac not cooling",
"loud noise from compressor",
"ac clutch not engaging"
],

"possible_causes":[
"compressor internal failure",
"compressor clutch failure"
],

"user_checks":[
"check if compressor engages when AC on"
],

"repair_cost":{"min":8000,"max":25000},

"probability":4
},

{
"id":57,
"problem":"Cabin Air Filter Clogged",

"system":"ac",
"component":"cabin air filter",

"symptoms":[
"weak airflow from vents",
"bad smell inside cabin",
"ac cooling reduced"
],

"possible_causes":[
"cabin filter clogged",
"dust accumulation in cabin filter"
],

"user_checks":[
"inspect cabin air filter"
],

"repair_cost":{"min":300,"max":1500},

"probability":5
},

{
"id":58,
"problem":"Oxygen Sensor Fault",

"system":"engine",
"component":"oxygen sensor",

"symptoms":[
"check engine light",
"poor fuel economy",
"engine running rich or lean"
],

"possible_causes":[
"oxygen sensor failure",
"sensor contamination"
],

"user_checks":[
"scan OBD codes"
],

"repair_cost":{"min":3000,"max":9000},

"probability":4
},

{
"id":59,
"problem":"Throttle Position Sensor Fault",

"system":"engine",
"component":"throttle position sensor",

"symptoms":[
"engine hesitation",
"irregular acceleration",
"engine stalling"
],

"possible_causes":[
"TPS sensor failure",
"sensor signal irregular"
],

"user_checks":[
"scan OBD codes",
"observe throttle response"
],

"repair_cost":{"min":3000,"max":8000},

"probability":4
},

{
"id":60,
"problem":"Engine Mount Worn",

"system":"engine",
"component":"engine mount",

"symptoms":[
"excessive engine vibration",
"thud sound during acceleration",
"engine movement visible"
],

"possible_causes":[
"engine mount rubber worn",
"engine mount broken"
],

"user_checks":[
"inspect engine movement while revving"
],

"repair_cost":{"min":3000,"max":10000},

"probability":2
},
{
"id":61,
"problem":"Fuel Pump Weak",

"system":"fuel",
"component":"fuel pump",

"symptoms":[
"engine hard to start",
"loss of power during acceleration",
"engine stalling while driving"
],

"possible_causes":[
"fuel pump worn",
"fuel pump pressure low"
],

"user_checks":[
"listen for fuel pump sound during ignition"
],

"repair_cost":{"min":4000,"max":12000},

"probability":4
},

{
"id":62,
"problem":"Fuel Filter Clogged",

"system":"fuel",
"component":"fuel filter",

"symptoms":[
"engine hesitation",
"loss of power",
"engine misfire during acceleration"
],

"possible_causes":[
"fuel filter clogged",
"dirty fuel contamination"
],

"user_checks":[
"check service history for fuel filter replacement"
],

"repair_cost":{"min":800,"max":3000},

"probability":5
},

{
"id":63,
"problem":"Turbocharger Lag",

"system":"engine",
"component":"turbocharger",

"symptoms":[
"delayed acceleration",
"lack of power at low RPM",
"slow turbo response"
],

"possible_causes":[
"turbocharger wear",
"boost pressure delay"
],

"user_checks":[
"observe turbo boost during acceleration"
],

"repair_cost":{"min":8000,"max":30000},

"probability":3
},

{
"id":64,
"problem":"Turbocharger Failure",

"system":"engine",
"component":"turbocharger",

"symptoms":[
"loss of engine power",
"whistling noise from engine",
"black smoke from exhaust"
],

"possible_causes":[
"turbocharger internal damage",
"turbo bearing failure"
],

"user_checks":[
"inspect turbo sound during acceleration"
],

"repair_cost":{"min":15000,"max":60000},

"probability":3
},

{
"id":65,
"problem":"DPF Filter Blocked",

"system":"exhaust",
"component":"diesel particulate filter",

"symptoms":[
"engine power reduced",
"DPF warning light",
"poor acceleration"
],

"possible_causes":[
"DPF clogged with soot",
"incomplete regeneration"
],

"user_checks":[
"check DPF warning indicator"
],

"repair_cost":{"min":5000,"max":25000},

"probability":4
},

{
"id":66,
"problem":"Catalytic Converter Blocked",

"system":"exhaust",
"component":"catalytic converter",

"symptoms":[
"engine power loss",
"engine overheating",
"reduced fuel efficiency"
],

"possible_causes":[
"catalytic converter clogged",
"exhaust flow restriction"
],

"user_checks":[
"check exhaust flow and engine power"
],

"repair_cost":{"min":8000,"max":35000},

"probability":3
},

{
"id":67,
"problem":"ABS Sensor Fault",

"system":"brake",
"component":"abs sensor",

"symptoms":[
"ABS warning light",
"ABS system not functioning",
"wheel speed sensor error"
],

"possible_causes":[
"ABS sensor failure",
"sensor wiring damage"
],

"user_checks":[
"scan OBD codes for ABS"
],

"repair_cost":{"min":2500,"max":9000},

"probability":4
},

{
"id":68,
"problem":"Wheel Alignment Incorrect",

"system":"suspension",
"component":"wheel alignment",

"symptoms":[
"car pulling to one side",
"uneven tire wear",
"steering wheel off center"
],

"possible_causes":[
"wheel alignment incorrect",
"suspension geometry disturbed"
],

"user_checks":[
"observe vehicle direction on straight road"
],

"repair_cost":{"min":800,"max":2500},

"probability":5
},

{
"id":69,
"problem":"Tire Pressure Low",

"system":"suspension",
"component":"tire",

"symptoms":[
"vehicle pulling to one side",
"reduced fuel efficiency",
"tire pressure warning light"
],

"possible_causes":[
"tire pressure low",
"slow tire air leak"
],

"user_checks":[
"check tire pressure with gauge"
],

"repair_cost":{"min":0,"max":500},

"probability":5
},

{
"id":70,
"problem":"ECU Sensor Communication Error",

"system":"electrical",
"component":"ECU system",

"symptoms":[
"multiple warning lights",
"engine performance irregular",
"diagnostic trouble codes present"
],

"possible_causes":[
"ECU communication error",
"sensor network malfunction"
],

"user_checks":[
"scan OBD system for multiple codes"
],

"repair_cost":{"min":3000,"max":20000},

"probability":3
},{
"id":71,
"problem":"Crankshaft Position Sensor Fault",

"system":"engine",
"component":"crankshaft position sensor",

"symptoms":[
"engine not starting",
"engine stalling suddenly",
"check engine light"
],

"possible_causes":[
"crankshaft sensor failure",
"sensor wiring fault"
],

"user_checks":[
"scan OBD codes",
"check if engine stalls randomly"
],

"repair_cost":{"min":2500,"max":8000},

"probability":4
},

{
"id":72,
"problem":"Camshaft Position Sensor Fault",

"system":"engine",
"component":"camshaft position sensor",

"symptoms":[
"engine misfire",
"poor acceleration",
"check engine light"
],

"possible_causes":[
"camshaft sensor failure",
"sensor signal incorrect"
],

"user_checks":[
"scan OBD codes"
],

"repair_cost":{"min":2500,"max":9000},

"probability":4
},

{
"id":73,
"problem":"Idle Air Control Valve Fault",

"system":"engine",
"component":"idle air control valve",

"symptoms":[
"engine idle unstable",
"engine stalling at idle",
"RPM fluctuating"
],

"possible_causes":[
"IAC valve dirty",
"IAC valve failure"
],

"user_checks":[
"observe idle RPM fluctuations"
],

"repair_cost":{"min":2000,"max":7000},

"probability":4
},

{
"id":74,
"problem":"Fuel Pressure Regulator Fault",

"system":"fuel",
"component":"fuel pressure regulator",

"symptoms":[
"engine hard to start",
"poor fuel economy",
"engine hesitation"
],

"possible_causes":[
"fuel pressure regulator failure",
"fuel pressure imbalance"
],

"user_checks":[
"inspect fuel pressure behavior"
],

"repair_cost":{"min":3000,"max":9000},

"probability":3
},

{
"id":75,
"problem":"PCV Valve Blocked",

"system":"engine",
"component":"pcv valve",

"symptoms":[
"engine oil consumption high",
"rough idle",
"engine sludge buildup"
],

"possible_causes":[
"PCV valve clogged",
"PCV valve stuck"
],

"user_checks":[
"inspect PCV valve condition"
],

"repair_cost":{"min":800,"max":3000},

"probability":4
},

{
"id":76,
"problem":"Drive Belt Worn",

"system":"engine",
"component":"drive belt",

"symptoms":[
"squealing noise from engine",
"alternator not charging properly",
"AC not functioning properly"
],

"possible_causes":[
"drive belt worn",
"belt tension low"
],

"user_checks":[
"inspect belt condition"
],

"repair_cost":{"min":800,"max":4000},

"probability":5
},

{
"id":77,
"problem":"Serpentine Belt Slipping",

"system":"engine",
"component":"serpentine belt",

"symptoms":[
"squealing noise during acceleration",
"battery warning light",
"AC performance reduced"
],

"possible_causes":[
"serpentine belt loose",
"belt tensioner worn"
],

"user_checks":[
"check belt tension"
],

"repair_cost":{"min":1000,"max":5000},

"probability":4
},

{
"id":78,
"problem":"Transmission Fluid Low",

"system":"transmission",
"component":"transmission fluid",

"symptoms":[
"gear shifting delayed",
"gear slipping",
"transmission overheating"
],

"possible_causes":[
"transmission fluid low",
"transmission fluid leak"
],

"user_checks":[
"check transmission fluid level"
],

"repair_cost":{"min":1000,"max":5000},

"probability":4
},

{
"id":79,
"problem":"Transmission Mount Worn",

"system":"transmission",
"component":"transmission mount",

"symptoms":[
"vibration during gear shift",
"thud noise when changing gears",
"excessive drivetrain movement"
],

"possible_causes":[
"transmission mount rubber worn",
"mount broken"
],

"user_checks":[
"inspect drivetrain movement"
],

"repair_cost":{"min":3000,"max":12000},

"probability":3
},

{
"id":80,
"problem":"Knock Sensor Fault",

"system":"engine",
"component":"knock sensor",

"symptoms":[
"engine knocking sound",
"reduced engine power",
"check engine light"
],

"possible_causes":[
"knock sensor failure",
"incorrect ignition timing detection"
],

"user_checks":[
"scan OBD codes"
],

"repair_cost":{"min":3000,"max":9000},

"probability":3
},{
"id":71,
"problem":"Crankshaft Position Sensor Fault",

"system":"engine",
"component":"crankshaft position sensor",

"symptoms":[
"engine not starting",
"engine stalling suddenly",
"check engine light"
],

"possible_causes":[
"crankshaft sensor failure",
"sensor wiring fault"
],

"user_checks":[
"scan OBD codes",
"check if engine stalls randomly"
],

"repair_cost":{"min":2500,"max":8000},

"probability":4
},

{
"id":72,
"problem":"Camshaft Position Sensor Fault",

"system":"engine",
"component":"camshaft position sensor",

"symptoms":[
"engine misfire",
"poor acceleration",
"check engine light"
],

"possible_causes":[
"camshaft sensor failure",
"sensor signal incorrect"
],

"user_checks":[
"scan OBD codes"
],

"repair_cost":{"min":2500,"max":9000},

"probability":4
},

{
"id":73,
"problem":"Idle Air Control Valve Fault",

"system":"engine",
"component":"idle air control valve",

"symptoms":[
"engine idle unstable",
"engine stalling at idle",
"RPM fluctuating"
],

"possible_causes":[
"IAC valve dirty",
"IAC valve failure"
],

"user_checks":[
"observe idle RPM fluctuations"
],

"repair_cost":{"min":2000,"max":7000},

"probability":4
},

{
"id":74,
"problem":"Fuel Pressure Regulator Fault",

"system":"fuel",
"component":"fuel pressure regulator",

"symptoms":[
"engine hard to start",
"poor fuel economy",
"engine hesitation"
],

"possible_causes":[
"fuel pressure regulator failure",
"fuel pressure imbalance"
],

"user_checks":[
"inspect fuel pressure behavior"
],

"repair_cost":{"min":3000,"max":9000},

"probability":3
},

{
"id":75,
"problem":"PCV Valve Blocked",

"system":"engine",
"component":"pcv valve",

"symptoms":[
"engine oil consumption high",
"rough idle",
"engine sludge buildup"
],

"possible_causes":[
"PCV valve clogged",
"PCV valve stuck"
],

"user_checks":[
"inspect PCV valve condition"
],

"repair_cost":{"min":800,"max":3000},

"probability":4
},

{
"id":76,
"problem":"Drive Belt Worn",

"system":"engine",
"component":"drive belt",

"symptoms":[
"squealing noise from engine",
"alternator not charging properly",
"AC not functioning properly"
],

"possible_causes":[
"drive belt worn",
"belt tension low"
],

"user_checks":[
"inspect belt condition"
],

"repair_cost":{"min":800,"max":4000},

"probability":5
},

{
"id":77,
"problem":"Serpentine Belt Slipping",

"system":"engine",
"component":"serpentine belt",

"symptoms":[
"squealing noise during acceleration",
"battery warning light",
"AC performance reduced"
],

"possible_causes":[
"serpentine belt loose",
"belt tensioner worn"
],

"user_checks":[
"check belt tension"
],

"repair_cost":{"min":1000,"max":5000},

"probability":4
},

{
"id":78,
"problem":"Transmission Fluid Low",

"system":"transmission",
"component":"transmission fluid",

"symptoms":[
"gear shifting delayed",
"gear slipping",
"transmission overheating"
],

"possible_causes":[
"transmission fluid low",
"transmission fluid leak"
],

"user_checks":[
"check transmission fluid level"
],

"repair_cost":{"min":1000,"max":5000},

"probability":4
},

{
"id":79,
"problem":"Transmission Mount Worn",

"system":"transmission",
"component":"transmission mount",

"symptoms":[
"vibration during gear shift",
"thud noise when changing gears",
"excessive drivetrain movement"
],

"possible_causes":[
"transmission mount rubber worn",
"mount broken"
],

"user_checks":[
"inspect drivetrain movement"
],

"repair_cost":{"min":3000,"max":12000},

"probability":3
},

{
"id":80,
"problem":"Knock Sensor Fault",

"system":"engine",
"component":"knock sensor",

"symptoms":[
"engine knocking sound",
"reduced engine power",
"check engine light"
],

"possible_causes":[
"knock sensor failure",
"incorrect ignition timing detection"
],

"user_checks":[
"scan OBD codes"
],

"repair_cost":{"min":3000,"max":9000},

"probability":3
},{
"id":91,
"problem":"Fuel Tank Vent Blocked",

"system":"fuel",
"component":"fuel tank vent",

"symptoms":[
"difficulty refueling",
"fuel smell near vehicle",
"engine hesitation"
],

"possible_causes":[
"fuel tank vent blocked",
"EVAP vent valve stuck"
],

"user_checks":[
"observe fuel filling behavior"
],

"repair_cost":{"min":1500,"max":6000},

"probability":3
},

{
"id":92,
"problem":"EVAP Purge Valve Fault",

"system":"fuel",
"component":"evap purge valve",

"symptoms":[
"check engine light",
"engine rough idle",
"fuel smell near engine"
],

"possible_causes":[
"purge valve stuck",
"evap system malfunction"
],

"user_checks":[
"scan OBD codes"
],

"repair_cost":{"min":2500,"max":8000},

"probability":4
},

{
"id":93,
"problem":"Throttle Cable Loose",

"system":"engine",
"component":"throttle cable",

"symptoms":[
"delayed acceleration",
"throttle response slow",
"engine RPM not increasing properly"
],

"possible_causes":[
"throttle cable loose",
"throttle linkage worn"
],

"user_checks":[
"inspect throttle cable movement"
],

"repair_cost":{"min":500,"max":2500},

"probability":4
},

{
"id":94,
"problem":"Clutch Release Bearing Worn",

"system":"transmission",
"component":"clutch release bearing",

"symptoms":[
"whining noise when clutch pressed",
"noise during gear change",
"vibration in clutch pedal"
],

"possible_causes":[
"release bearing worn",
"bearing lubrication failure"
],

"user_checks":[
"listen for noise when clutch pedal pressed"
],

"repair_cost":{"min":5000,"max":15000},

"probability":4
},

{
"id":95,
"problem":"Wheel Balancing Incorrect",

"system":"suspension",
"component":"wheel balancing",

"symptoms":[
"steering vibration at high speed",
"vehicle shaking at certain speeds",
"uneven tire wear"
],

"possible_causes":[
"wheel balancing incorrect",
"wheel weight missing"
],

"user_checks":[
"observe vibration around 80-100 km/h"
],

"repair_cost":{"min":500,"max":2000},

"probability":5
},

{
"id":96,
"problem":"Sunroof Drain Blocked",

"system":"body",
"component":"sunroof drain",

"symptoms":[
"water leakage inside cabin",
"wet roof lining",
"water dripping inside car"
],

"possible_causes":[
"sunroof drain pipe blocked",
"dirt blocking drain channel"
],

"user_checks":[
"inspect sunroof drain outlets"
],

"repair_cost":{"min":1000,"max":4000},

"probability":4
},

{
"id":97,
"problem":"Horn Not Working",

"system":"electrical",
"component":"horn system",

"symptoms":[
"horn not producing sound",
"horn works intermittently",
"no response when pressing horn"
],

"possible_causes":[
"horn fuse blown",
"horn relay failure"
],

"user_checks":[
"check horn fuse"
],

"repair_cost":{"min":500,"max":3000},

"probability":4
},

{
"id":98,
"problem":"Wiper Motor Failure",

"system":"electrical",
"component":"wiper motor",

"symptoms":[
"wipers not moving",
"wipers move slowly",
"wipers stop midway"
],

"possible_causes":[
"wiper motor failure",
"wiper linkage jammed"
],

"user_checks":[
"test wiper operation"
],

"repair_cost":{"min":2000,"max":7000},

"probability":4
},

{
"id":99,
"problem":"Headlight Bulb Burned",

"system":"electrical",
"component":"headlight bulb",

"symptoms":[
"headlight not working",
"one side headlight off",
"dim headlight"
],

"possible_causes":[
"bulb filament burned",
"electrical connection loose"
],

"user_checks":[
"inspect headlight bulb"
],

"repair_cost":{"min":300,"max":2000},

"probability":5
},

{
"id":100,
"problem":"Brake Light Switch Fault",

"system":"electrical",
"component":"brake light switch",

"symptoms":[
"brake lights not working",
"brake lights stay on continuously",
"cruise control not working"
],

"possible_causes":[
"brake light switch failure",
"switch contact worn"
],

"user_checks":[
"check brake lights when pedal pressed"
],

"repair_cost":{"min":800,"max":3000},

"probability":4
}]