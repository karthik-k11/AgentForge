import re


def extract_error_file(traceback_text):

    pattern = r'File "([^"]+)"'

    matches = re.findall(
        pattern,
        traceback_text
    )

    if matches:

        return matches[-1]

    return None