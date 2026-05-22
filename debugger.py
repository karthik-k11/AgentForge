from llm import ask_llm


def debugger_agent(error_traceback, project_context):

    prompt = f"""
    You are a senior AI Debugger Agent.

    Analyze the runtime error carefully.

    Also inspect the FULL project source code.

    Explain:
    1. What failed
    2. Why it failed
    3. Likely fix direction

    Keep explanation short and clear.

    Runtime Error:
    {error_traceback}

    Full Project Context:
    {project_context}
    """

    response = ask_llm(prompt)

    return response