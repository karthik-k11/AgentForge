from explorer import explorer_agent
from executor import executor_agent
from debugger import debugger_agent
from codegen import code_generator_agent
from reviewer import reviewer_agent
from patcher import apply_patch
from validator import validate_python_code

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
            "sample_project/app.py"
        )

        workflow_state["execution_result"] = result

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
            workflow_state["execution_result"]["stderr"]
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

        ##Apply patch automatically if accepted
        if "ACCEPT" in result:

            validation_result = validate_python_code(
                workflow_state["generated_fix"]
            )

            workflow_state[
                "validation_result"
            ] = validation_result

            if validation_result["valid"]:

                patch_result = apply_patch(
                    "sample_project/app.py",
                    workflow_state["generated_fix"]
                )

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

        if not workflow_state["generated_fix"]:

            print(
                "Skipping Reviewer: "
                "No generated fix available."
            )

            return None

        result = reviewer_agent(
            workflow_state["execution_result"]["stderr"],
            workflow_state["generated_fix"]
        )

        workflow_state["review_result"] = result

        return result

    else:

        print(f"Unknown agent: {agent_name}")

        return None