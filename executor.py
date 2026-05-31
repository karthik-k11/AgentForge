import subprocess
import sys
import time


def executor_agent(file_path):

    try:
        start_time = time.time()
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        success = result.returncode == 0
        execution_time = round(
            time.time() - start_time,
            3
        )

        return {
            "success": success,
            "status": (
                "SUCCESS"
                if success
                else "ERROR"
            ),
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
            "execution_time": execution_time
        }

    except subprocess.TimeoutExpired:
        execution_time = round(
            time.time() - start_time,
            3
        )

        return {
            "success": False,
            "status": "TIMEOUT",
            "stdout": "",
            "stderr": "Process execution timed out.",
            "return_code": -1,
            "execution_time": execution_time
        }

    except Exception as error:
        execution_time = round(
            time.time() - start_time,
            3
        )
        

        return {
            "success": False,
            "status": "ERROR",
            "stdout": "",
            "stderr": str(error),
            "return_code": -1,
            "execution_time": execution_time
        }