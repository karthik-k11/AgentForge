from planner import planner_agent
from router import execute_step
from state import create_workflow_state


MAX_RETRIES = 3


def run_workflow(
    user_request,
    project_path="sample_project",
    entry_file="sample_project/app.py"
):

    workflow_state = create_workflow_state()

    workflow_state["user_request"] = user_request

    workflow_state["project_path"] = project_path

    workflow_state["entry_file"] = entry_file

    plan = planner_agent(user_request)

    steps = plan["steps"]

    for step in steps:

        execute_step(
            step,
            workflow_state
        )

        if step["agent"] == "Reviewer":

            retries = 0

            while (
                workflow_state[
                    "review_result"
                ].strip().upper()
                != "ACCEPT"
            ):

                if retries >= MAX_RETRIES:

                    print(
                        "Max retries reached."
                    )

                    break

                execute_step(
                    {
                        "agent": "CodeGenerator",
                        "action": "Retry fix"
                    },
                    workflow_state
                )

                execute_step(
                    {
                        "agent": "Reviewer",
                        "action": "Re-review fix"
                    },
                    workflow_state
                )

                retries += 1

        if (
            step["agent"] == "Executor"
            and
            workflow_state[
                "execution_result"
            ]["success"]
        ):
            break

    return {

        "status": workflow_state[
            "execution_result"
        ].get(
            "status",
            "UNKNOWN"
        ),

        "agent_count": len(
            plan["steps"]
        ),

        "execution_history": len(
            workflow_state[
                "execution_history"
            ]
        ),

        "failed_file": workflow_state[
            "failed_file"
        ],

        "generated_fix": workflow_state[
            "generated_fix"
        ],

        "debug_analysis": workflow_state[
            "debug_analysis"
        ],

        "review_result": workflow_state[
            "review_result"
        ],

        "patch_result": workflow_state[
            "patch_result"
        ],

        "patch_success":
        workflow_state[
            "patch_result"
        ].get(
            "success",
            False
        ),

        "backup_file":
        workflow_state[
            "patch_result"
        ].get(
            "backup_file"
        ),

        "validation_passed":
        workflow_state[
            "validation_result"
        ].get(
            "valid"
        ),

        "validation_required":
        not workflow_state[
            "execution_result"
        ].get(
            "success",
            False
        ),

        "execution_time":
        workflow_state[
            "execution_result"
        ].get(
            "execution_time",
            0
        ),

        "plan": plan
    }