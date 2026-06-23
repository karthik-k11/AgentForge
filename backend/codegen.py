from llm import ask_llm
from utils import clean_code_response


def code_generator_agent(
    error_traceback,
    retry_memory=None
):

    if retry_memory is None:

        retry_memory = []

    prompt = f"""
    You are a senior AI Software Engineer.

    A Python application failed.

    Analyze the traceback and generate corrected Python code.

    Previous Retry Attempts:
    {retry_memory}

    Return ONLY raw Python code.

    No markdown.
    No explanations.

    Traceback:
    {error_traceback}
    """

    response = ask_llm(prompt)

    cleaned_code = clean_code_response(response)

    return cleaned_code