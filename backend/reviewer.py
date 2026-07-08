from llm import ask_llm


def reviewer_agent(original_error, generated_fix):

    prompt = f"""
    You are a Senior Python Code Reviewer.

    Review the generated fix for the reported Python error.

    Your goal is to determine whether the fix is reasonable,
    correct and safe to apply.

    Review Checklist:

    1. Does the fix solve the reported error?
    2. Is the generated code valid Python?
    3. Does it avoid introducing obvious new errors?
    4. Does it preserve the original program as much as possible?
    5. Is the change minimal and directly related to the error?

    IMPORTANT:

    - Do NOT reject a fix simply because there are multiple possible solutions.
    - Accept reasonable fixes.
    - Reject only if the fix is clearly incorrect,
      unrelated to the error,
      invalid Python,
      or likely to break the program.

    Return ONLY one word.

    ACCEPT

    or

    RETRY

    Original Error:

    {original_error}

    Generated Fix:

    {generated_fix}
    """

    response = ask_llm(prompt)

    return response.strip().upper()