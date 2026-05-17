from llm import ask_llm


def reviewer_agent(original_error, generated_fix):

    prompt = f"""
    You are a senior AI Code Reviewer.

    Review the generated fix carefully.

    Determine:
    1. Does the fix solve the error?
    2. Is the fix reasonable?
    3. Should the system ACCEPT or RETRY?

    Return ONLY:

    ACCEPT
    or
    RETRY

    Original Error:
    {original_error}

    Generated Fix:
    {generated_fix}
    """

    response = ask_llm(prompt)

    return response.strip()