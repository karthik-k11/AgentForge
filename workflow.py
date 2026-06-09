from planner import planner_agent
from router import execute_step
from state import create_workflow_state


def run_workflow(user_request):

    workflow_state = create_workflow_state()

    workflow_state["user_request"] = user_request

    plan = planner_agent(user_request)

    steps = plan["steps"]

    for step in steps:

        execute_step(
            step,
            workflow_state
        )

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

        "review_result": workflow_state[
            "review_result"
        ],

        "patch_result": workflow_state[
            "patch_result"
        ],

        "validation_passed":
        workflow_state[
            "validation_result"
        ].get(
            "valid",
            False
        ),

        "execution_time": workflow_state[
            "execution_result"
        ].get(
            "execution_time",
            0
        ),

        "plan": plan
    }