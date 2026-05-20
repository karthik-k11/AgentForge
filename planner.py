import json

from llm import ask_llm


def planner_agent(user_request):

    prompt = f"""
    You are a senior AI Planning Agent.

    Break the software problem into short debugging tasks.

    Return ONLY valid JSON.

    Example format:

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

    return json.loads(response)