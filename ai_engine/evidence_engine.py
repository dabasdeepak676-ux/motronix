# ---------------------------------------
# Evidence Adjustment Engine
# ---------------------------------------

def adjust_scores(results, answers):

    if not answers:
        return results

    for result in results:

        issue = result["issue"]
        confidence = result["confidence"]

        # -----------------------------------
        # BRAKE LOGIC
        # -----------------------------------

        if "Brake Pad Wear" in issue:

            if answers.get("brake_noise") == "yes":
                confidence += 5

            if answers.get("brake_vibration") == "yes":
                confidence -= 10


        if "Brake Disc Warped" in issue:

            if answers.get("brake_vibration") == "yes":
                confidence += 15

            if answers.get("brake_noise") == "yes":
                confidence += 5


        if "Brake Dust Accumulation" in issue:

            if answers.get("brake_noise") == "yes":
                confidence += 5

            if answers.get("brake_vibration") == "yes":
                confidence -= 5


        # -----------------------------------
        # STARTING SYSTEM
        # -----------------------------------

        if "Battery Dead" in issue:

            if answers.get("dashboard_lights") == "no":
                confidence += 15

            if answers.get("clicking_sound") == "yes":
                confidence += 10


        if "Starter Motor Failure" in issue:

            if answers.get("clicking_sound") == "yes":
                confidence += 15


        if "Alternator Failure" in issue:

            if answers.get("dashboard_lights") == "yes":
                confidence += 10


        # limit
        confidence = max(5, min(confidence, 95))

        result["confidence"] = confidence

    # sort again
    results.sort(key=lambda x: x["confidence"], reverse=True)

    return results