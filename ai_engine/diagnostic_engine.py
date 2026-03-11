from failure_database import FAILURE_DATABASE
from ai_engine.reasoning_engine import rank_failures
from ai_engine.component_detector import detect_components
from ai_engine.evidence_engine import adjust_scores
from ai_engine.diagnostic_question_engine import generate_questions


# ---------------------------------------
# FILTER FAILURES
# ---------------------------------------

def filter_failures(problem_text, car=None):

    components = detect_components(problem_text)
    print("Detected Components:", components)

    if not components:
        return FAILURE_DATABASE

    filtered = []

    for failure in FAILURE_DATABASE:

        component = failure.get("component", "").lower()
        system = failure.get("system", "").lower()

        symptoms = " ".join(failure.get("symptoms", []))
        causes = " ".join(failure.get("possible_causes", []))

        text = (
            failure.get("problem", "")
            + " "
            + symptoms
            + " "
            + causes
        ).lower()

        for comp in components:

            # strict system match
            if comp == system:
                filtered.append(failure)
                break

            # secondary component match
            if comp in component:
                filtered.append(failure)
                break

    if not filtered:
        return FAILURE_DATABASE

    return filtered


# ---------------------------------------
# MAIN DIAGNOSIS FUNCTION
# ---------------------------------------

def diagnose_vehicle(problem_text, answers=None, car=None):

    if answers is None:
        answers = {}

    problem_text = problem_text.strip().lower()

    # Step 1 → Detect components
    components = detect_components(problem_text)

    # Step 2 → Filter failures
    filtered_db = filter_failures(problem_text, car)

    # Step 3 → Rank failures
    results = rank_failures(problem_text, filtered_db)

    # Step 4 → Adjust confidence
    results = adjust_scores(results, answers)

    questions = []

    # Step 5 → Generate follow-up questions
    if results:

        top_issue = results[0]["issue"]

        try:
            questions = generate_questions(top_issue)
        except:
            questions = []

    return results, questions