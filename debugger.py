from llm import ask_llm


def debugger_agent(error_traceback):

    prompt = f"""
    You are a senior AI Debugger Agent.

    Analyze the following Python traceback.

    Explain:
    1. What failed
    2. Why it failed
    3. Likely fix direction

    Keep explanation short and clear.

    Traceback:
    {error_traceback}
    """

    response = ask_llm(prompt)

    return response