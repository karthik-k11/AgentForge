def clean_json_response(response):

    response = response.strip()

    response = response.replace("```json", "")

    response = response.replace("```", "")

    return response.strip()


def clean_code_response(response):

    response = response.strip()

    response = response.replace("```python", "")

    response = response.replace("```", "")

    return response.strip()