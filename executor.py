import subprocess
import sys


def executor_agent(file_path):

    try:

        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        success = result.returncode == 0

        return {
            "success": success,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode
        }

    except subprocess.TimeoutExpired:

        return {
            "success": False,
            "stdout": "",
            "stderr": "Process execution timed out.",
            "return_code": -1
        }

    except Exception as error:

        return {
            "success": False,
            "stdout": "",
            "stderr": str(error),
            "return_code": -1
        }