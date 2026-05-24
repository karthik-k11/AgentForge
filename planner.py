import json

from llm import ask_llm
from utils import clean_json_response


def planner_agent(user_request):

    prompt = f"""
    You are a senior AI Orchestrator Agent.

    Create a structured execution plan.

    Available Agents:
    - Explorer
    - Executor
    - Debugger
    - CodeGenerator
    - Reviewer

    Return ONLY valid JSON.

    Example:

    {{
        "steps": [
            {{
                "agent": "Explorer",
                "action": "Inspect project files"
            }},
            {{
                "agent": "Executor",
                "action": "Run Flask application"
            }},
            {{
                "agent": "Debugger",
                "action": "Analyze runtime errors"
            }}
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

        print("\nInvalid JSON returned by Planner Agent ⚠️")

        return {
            "steps": [
                {
                    "agent": "Explorer",
                    "action": "Inspect project manually"
                }
            ]
        }