import json

from llm import ask_llm
from utils import clean_json_response


def planner_agent(user_request):

    prompt = f"""
    You are a senior AI Planning Agent.

    Break the software problem into short debugging tasks.

    Return ONLY valid JSON.

    Example:

    {{
        "tasks": [
            "Check logs",
            "Run debug mode",
            "Verify dependencies"
        ]
    }}

    User Request:
    {user_request}
    """

    response = ask_llm(prompt)

    cleaned_response = clean_json_response(response)

    print("\nRAW PLANNER RESPONSE:\n")
    print(cleaned_response)

    try:

        return json.loads(cleaned_response)

    except json.JSONDecodeError:

        print("\nInvalid JSON returned by Planner Agent")

        return {
            "tasks": [
                "Fallback task: Inspect application manually"
            ]
        }