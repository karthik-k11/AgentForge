from llm import ask_llm


def planner_agent(user_request):

    prompt = f"""
    You are a senior AI Planning Agent.

    Your job is to break software problems
    into clear execution steps.

    User Request:
    {user_request}

    Create a numbered execution plan.
    """

    response = ask_llm(prompt)

    return response