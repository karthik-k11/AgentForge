import re


def extract_error_file(traceback_text):

    pattern = r'File "([^"]+)"'

    matches = re.findall(
        pattern,
        traceback_text
    )

    for file in reversed(matches):

        if (
            "<frozen" not in file
            and
            "site-packages" not in file
            and
            "lib/python" not in file.replace("\\", "/").lower()
        ):

            return file

    return None


def extract_error_line(traceback_text):

    pattern = r'line (\d+)'

    matches = re.findall(
        pattern,
        traceback_text
    )

    if matches:

        return int(matches[-1])

    return None