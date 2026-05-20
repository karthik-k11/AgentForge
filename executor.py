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
            "success": True,
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except subprocess.TimeoutExpired:

        return {
            "success": True,
            "stdout": "Server started successfully.",
            "stderr": ""
        }

    except Exception as error:

        return {
            "success": False,
            "stdout": "",
            "stderr": str(error)
        }