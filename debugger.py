from llm import ask_llm


def debugger_agent(error_traceback, source_code):

    prompt = f"""
    You are a senior AI Debugger Agent.

    Analyze the runtime error carefully.

    Also inspect the provided source code.

    Explain:
    1. What failed
    2. Why it failed
    3. Likely fix direction

    Keep explanation short and clear.

    Runtime Error:
    {error_traceback}

    Source Code:
    {source_code}
    """

    response = ask_llm(prompt)

    return response