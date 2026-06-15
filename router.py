from explorer import explorer_agent
from executor import executor_agent
from debugger import debugger_agent
from codegen import code_generator_agent
from reviewer import reviewer_agent
from patcher import apply_patch
from validator import validate_python_code
from error_parser import (
    extract_error_file,
    extract_error_line
)
from permissions import is_patch_allowed

def execute_step(step, workflow_state):

    agent_name = step["agent"]

    action = step["action"]

    print(f"\nExecuting: [{agent_name}] {action}\n")

    if agent_name == "Explorer":

        result = explorer_agent(
            "sample_project",
            workflow_state["user_request"]
        )

        workflow_state["files"] = result["files"]

        workflow_state["project_context"] = result[
            "project_context"
        ]

        return result

    elif agent_name == "Executor":

        result = executor_agent(
            "sample_project/app.py",
            workflow_state[
                "sandbox_config"
            ]["max_execution_time"]
        )

        workflow_state["execution_result"] = result

        workflow_state["execution_metadata"] = {
            "status": result["status"],
            "return_code": result["return_code"],
            "execution_time": result["execution_time"]
        }

        workflow_state[
            "execution_history"
        ].append(
            workflow_state[
                "execution_metadata"
            ]
        )

        failed_file = extract_error_file(
            result["stderr"]
        )

        failed_line = extract_error_line(
            result["stderr"]
        )

        workflow_state["failed_file"] = failed_file

        workflow_state["failed_line"] = failed_line

        return result

    elif agent_name == "Debugger":

        if not workflow_state["execution_result"]:

            print(
                "Skipping Debugger: "
                "No execution result available."
            )

            return None

        result = debugger_agent(
            workflow_state["execution_result"]["stderr"],
            workflow_state["project_context"]
        )

        workflow_state["debug_analysis"] = result

        return result

    elif agent_name == "CodeGenerator":

        if not workflow_state["execution_result"]:

            print(
                "Skipping CodeGenerator: "
                "No execution result available."
            )

            return None

        result = code_generator_agent(
            workflow_state[
                "execution_result"
            ]["stderr"],

            workflow_state[
                "retry_memory"
            ]
        )

        workflow_state["generated_fix"] = result

        return result

    elif agent_name == "Reviewer":

        if not workflow_state["generated_fix"]:

            print(
                "Skipping Reviewer: "
                "No generated fix available."
            )

            return None

        ##Run reviewer
        result = reviewer_agent(
            workflow_state["execution_result"]["stderr"],
            workflow_state["generated_fix"]
        )

        workflow_state["review_result"] = result

        workflow_state[
            "retry_memory"
        ].append({

            "error": workflow_state[
                "execution_result"
            ]["stderr"],

            "generated_fix": workflow_state[
                "generated_fix"
            ],

            "review_result": result
        })

        ##Apply patch automatically if accepted
        if result.strip().upper() == "ACCEPT":

            validation_result = validate_python_code(
                workflow_state["generated_fix"]
            )

            workflow_state[
                "validation_result"
            ] = validation_result

            if validation_result["valid"]:

                allowed = is_patch_allowed(
                    workflow_state["failed_file"],
                    workflow_state["safety_config"]
                )

                if allowed:

                    patch_result = apply_patch(
                        workflow_state["failed_file"],
                        workflow_state["generated_fix"],
                        workflow_state["failed_line"]
                    )

                else:

                    patch_result = {
                        "success": False,
                        "error":
                        "Patch blocked by safety policy"
                    }

                workflow_state["patch_result"] = patch_result

            else:

                workflow_state["patch_result"] = {
                    "success": False,
                    "error": (
                        "Generated fix failed "
                        "syntax validation"
                    )
                }

        return result

    else:

        print(f"Unknown agent: {agent_name}")

        return None