from llm import ask_llm


def reviewer_agent(original_error, generated_fix):

    prompt = f"""
    You are a senior AI Code Reviewer.

    Your job is to critically evaluate the generated fix.

    Assume the fix is incorrect unless there is sufficient evidence that it solves the original error.

    Carefully verify:

    1. Does the generated fix directly address the reported error?
    2. Could it introduce new bugs or syntax errors?
    3. Does it preserve the intended behavior of the program?
    4. Is the fix complete rather than a temporary workaround?

    Decision rules:

    - Return ACCEPT only if you are confident the fix is correct.
    - Return RETRY if you have any reasonable doubt.

    Return ONLY one word:

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