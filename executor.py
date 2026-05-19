import subprocess
import sys


def executor_agent(file_path):

    try:

        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except subprocess.TimeoutExpired:

        return {
            "stdout": "",
            "stderr": "Process execution timed out."
        }

    except Exception as error:

        return {
            "stdout": "",
            "stderr": str(error)
        }