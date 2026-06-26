import json

from llm import ask_llm
from utils import clean_json_response


def planner_agent(user_request):

    prompt = f"""
You are an AI Workflow Planner.

Your job is ONLY to generate the execution plan.

You MUST use ONLY these agents and in this exact order:

1. Explorer
2. Executor
3. Debugger
4. CodeGenerator
5. Reviewer

Rules:

- Do NOT add extra agents.
- Do NOT repeat any agent.
- Do NOT skip any agent.
- Do NOT invent new agent names.
- Always return exactly 5 steps.
- Return ONLY valid JSON.
- No markdown.
- No explanations.

Return this schema exactly:

{{
    "steps":[
        {{
            "agent":"Explorer",
            "action":"Inspect project files"
        }},
        {{
            "agent":"Executor",
            "action":"Run target application"
        }},
        {{
            "agent":"Debugger",
            "action":"Analyze runtime errors"
        }},
        {{
            "agent":"CodeGenerator",
            "action":"Generate corrected code"
        }},
        {{
            "agent":"Reviewer",
            "action":"Review generated fix"
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