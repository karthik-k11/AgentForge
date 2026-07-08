from llm import ask_llm
from utils import clean_code_response


def code_generator_agent(
    error_traceback,
    retry_memory=None
):

    if retry_memory is None:

        retry_memory = []

    prompt = f"""
    You are a Senior Python Software Engineer.

    A Python application failed.

    Analyze the traceback carefully and generate the corrected Python code.

    STRICT RULES:

    1. Fix ONLY the reported error.
    2. Preserve all unrelated code.
    3. Do NOT rewrite the entire application.
    4. Make the smallest possible change.
    5. Keep the original program structure.
    6. Do not add unnecessary functions, classes, or comments.
    7. Do not generate example programs.
    8. If an import is incorrect, replace ONLY that import.
    9. If a variable is missing, define ONLY that variable.
    10. If a syntax error exists, correct ONLY the syntax.
    11. Return executable Python code.
    12. Return ONLY raw Python code.

    Previous Retry Attempts:
    {retry_memory}

    Traceback:
    {error_traceback}
    """

    response = ask_llm(prompt)

    cleaned_code = clean_code_response(response)

    return cleaned_code