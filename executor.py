import subprocess
import sys


def executor_agent(file_path):

    try:

        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True
        )

        return {
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except Exception as error:

        return {
            "stdout": "",
            "stderr": str(error)
        }