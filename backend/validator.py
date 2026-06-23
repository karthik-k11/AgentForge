import ast


def validate_python_code(code):

    try:

        ast.parse(code)

        return {
            "valid": True,
            "error": None
        }

    except SyntaxError as error:

        return {
            "valid": False,
            "error": str(error)
        }