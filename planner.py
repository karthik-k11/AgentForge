import json

from llm import ask_llm


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

    print("\nRAW PLANNER RESPONSE:\n")
    print(response)

    try:

        return json.loads(response)

    except json.JSONDecodeError:

        print("\nInvalid JSON returned by Planner Agent ⚠️")

        return {
            "tasks": [
                "Fallback task: Inspect application manually"
            ]
        }