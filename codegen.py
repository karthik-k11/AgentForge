from llm import ask_llm


def code_generator_agent(error_traceback):

    prompt = f"""
    You are a senior AI Software Engineer.

    A Python application failed.

    Analyze the traceback and generate
    corrected Python code.

    Return:
    - Fixed code only
    - No explanations
    - No markdown

    Traceback:
    {error_traceback}
    """

    response = ask_llm(prompt)

    return response