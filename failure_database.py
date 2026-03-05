# failure_database.py
FAILURE_DATABASE = [

{
"id":1,
"problem":"Battery Dead",
"system":"electrical",
"component":"battery",
"severity":"medium",
"urgency":"service_soon",

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
"id":6,
"problem":"Clutch Slipping",
"system":"transmission",
"component":"clutch",
"severity":"high",
"urgency":"service_soon",

"symptoms":[
"engine revs increase but speed not increasing",
"burning smell",
"poor acceleration"
],

"possible_causes":[
"clutch plate worn",
"pressure plate weak",
"oil on clutch plate"
],

"user_checks":[
"check if RPM increases without speed",
"check for burning smell"
],

"user_actions":[
"avoid aggressive driving",
"visit service center"
],

"mechanic_checks":[
"check clutch free play",
"inspect clutch plate"
],

"repair_cost":{
"min":5000,
"max":20000
}
},

{
"id":7,
"problem":"Hard Gear Shifting",
"system":"transmission",
"component":"gearbox",
"severity":"medium",
"urgency":"service_soon",

"symptoms":[
"gear difficult to engage",
"gear grinding"
],

"possible_causes":[
"low gearbox oil",
"clutch not disengaging",
"gear synchronizer worn"
],

"user_checks":[
"check if gear shifting is hard when engine cold"
],

"user_actions":[
"avoid forcing gear shift",
"visit mechanic"
],

"mechanic_checks":[
"check gearbox oil level",
"inspect clutch operation"
],

"repair_cost":{
"min":1500,
"max":12000
}
},

{
"id":8,
"problem":"Engine Misfire",
"system":"engine",
"component":"ignition system",
"severity":"high",
"urgency":"service_soon",

"symptoms":[
"engine shaking",
"loss of power",
"rough idle"
],

"possible_causes":[
"spark plug worn",
"ignition coil faulty",
"fuel injector clogged"
],

"user_checks":[
"check if engine vibrates while idling"
],

"user_actions":[
"avoid high acceleration",
"visit mechanic"
],

"mechanic_checks":[
"inspect spark plugs",
"scan obd codes"
],

"repair_cost":{
"min":2000,
"max":10000
}
},

{
"id":9,
"problem":"Fuel Pump Failure",
"system":"fuel",
"component":"fuel pump",
"severity":"high",
"urgency":"service_soon",

"symptoms":[
"engine cranks but not starting",
"loss of power while driving"
],

"possible_causes":[
"fuel pump failure",
"fuel filter blocked"
],

"user_checks":[
"check if engine cranks but does not start"
],

"user_actions":[
"avoid repeated starting attempts",
"call mechanic"
],

"mechanic_checks":[
"check fuel pressure",
"listen fuel pump sound"
],

"repair_cost":{
"min":4000,
"max":12000
}
},

{
"id":10,
"problem":"AC Not Cooling",
"system":"ac",
"component":"ac system",
"severity":"low",
"urgency":"service_soon",

"symptoms":[
"AC blowing warm air",
"weak cooling"
],

"possible_causes":[
"low refrigerant",
"compressor failure",
"AC condenser blocked"
],

"user_checks":[
"check if AC airflow is weak"
],

"user_actions":[
"avoid using AC continuously"
],

"mechanic_checks":[
"check refrigerant pressure",
"inspect compressor clutch"
],

"repair_cost":{
"min":1500,
"max":8000
}
},

{
"id":11,
"problem":"Engine Oil Leak",
"system":"engine",
"component":"engine seals",
"severity":"medium",
"urgency":"service_soon",

"symptoms":[
"oil spots under car",
"burning oil smell",
"low engine oil level"
],

"possible_causes":[
"oil seal worn",
"valve cover gasket leak",
"oil filter loose"
],

"user_checks":[
"check for oil drops under car",
"check engine oil level"
],

"user_actions":[
"avoid long driving",
"visit service center"
],

"mechanic_checks":[
"inspect under engine",
"check oil filter tightness"
],

"repair_cost":{
"min":2000,
"max":7000
}
},

{
"id":12,
"problem":"Coolant Leak",
"system":"cooling",
"component":"cooling system",
"severity":"high",
"urgency":"service_soon",

"symptoms":[
"coolant level dropping",
"sweet smell from engine bay",
"engine overheating"
],

"possible_causes":[
"radiator leak",
"coolant hose cracked",
"water pump seal leak"
],

"user_checks":[
"check coolant level in reservoir"
],

"user_actions":[
"avoid driving long distance"
],

"mechanic_checks":[
"inspect radiator",
"check coolant hoses"
],

"repair_cost":{
"min":2000,
"max":10000
}
},

{
"id":13,
"problem":"Radiator Fan Not Working",
"system":"cooling",
"component":"radiator fan",
"severity":"high",
"urgency":"service_soon",

"symptoms":[
"engine overheating in traffic",
"AC cooling weak in traffic"
],

"possible_causes":[
"radiator fan motor failure",
"fan relay fault"
],

"user_checks":[
"check if fan runs when engine hot"
],

"user_actions":[
"avoid traffic driving"
],

"mechanic_checks":[
"check fan relay",
"inspect fan motor"
],

"repair_cost":{
"min":2500,
"max":8000
}
},

{
"id":14,
"problem":"Spark Plug Failure",
"system":"engine",
"component":"spark plug",
"severity":"medium",
"urgency":"service_soon",

"symptoms":[
"engine misfire",
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

"symptoms":[
"engine misfire",
"engine shaking",
"check engine light"
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
}]