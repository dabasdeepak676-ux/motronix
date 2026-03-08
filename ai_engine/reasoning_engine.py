from ai_engine.component_detector import detect_components
from ai_engine.synonym_engine import expand_words
from ai_engine.diagnostic_tree import detect_system, detect_component
from ai_engine.explanation_engine import generate_explanation

# ------------------------------------------------
# SCORE CALCULATION
# ------------------------------------------------

def calculate_match_score(problem_text, failure):

    words = expand_words(problem_text)
    text = " ".join(words)

    score = 0

    # -------------------------
    # PROBABILITY BOOST
    # -------------------------

    prob = failure.get("probability", 3)
    score += prob * 3

    # -------------------------
    # SYMPTOM MATCHING
    # -------------------------

    for symptom in failure["symptoms"]:

        symptom_text = symptom.lower()

        # exact phrase match
        if symptom_text in text:
            score += 25

        for word in symptom_text.split():

            if len(word) < 4:
                continue

            if word in text:
                score += 5

    # -------------------------
    # CAUSE MATCHING
    # -------------------------

    for cause in failure["possible_causes"]:

        for word in cause.lower().split():

            if len(word) < 4:
                continue

            if word in text:
                score += 2

    return score


# ------------------------------------------------
# MAIN RANKING ENGINE
# ------------------------------------------------

def rank_failures(problem_text, failure_database):

    matches = []

    detected_system = detect_system(problem_text)
    detected_component = detect_component(problem_text)

    components = detect_components(problem_text)

    # ---------------------------------
    # CALCULATE RAW SCORES
    # ---------------------------------

    for failure in failure_database:

        score = calculate_match_score(problem_text, failure)

        # -------------------------
        # SYSTEM BOOST
        # -------------------------

        if detected_system:
            if failure.get("system") == detected_system:
                score += 10

        # -------------------------
        # COMPONENT BOOST
        # -------------------------

        if detected_component:

            ccomponent = failure.get("component", "").lower()

            if detected_component and detected_component in component:
               score += 15

        # -------------------------
        # EXTRA COMPONENT BOOST
        # -------------------------

        component = failure.get("component", "").lower()

        for comp in components:

            if comp and comp in component:
              score += 10

        if score <= 5:
            continue

        matches.append({
    "issue": failure["problem"],
    "raw_score": score,
    "severity": failure.get("severity"),
    "repair_cost": failure.get("repair_cost"),
    "user_checks": failure.get("user_checks"),
    "explanation": generate_explanation(problem_text, failure, None)
})

    if not matches:
        return []

    # ---------------------------------
    # FIND TOP SCORE
    # ---------------------------------

    top_score = max(item["raw_score"] for item in matches)

    # ---------------------------------
    # NORMALIZE CONFIDENCE
    # ---------------------------------

    for item in matches:

        confidence = (item["raw_score"] / top_score) * 95
        item["confidence"] = round(confidence)

        del item["raw_score"]

    # ---------------------------------
    # SORT RESULTS
    # ---------------------------------

    matches.sort(key=lambda x: x["confidence"], reverse=True)

    # ---------------------------------
    # REMOVE DUPLICATES
    # ---------------------------------

    unique = []
    seen = set()

    for item in matches:

        if item["issue"] not in seen:

            unique.append(item)
            seen.add(item["issue"])

    return unique[:3]