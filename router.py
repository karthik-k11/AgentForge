from explorer import explorer_agent
from executor import executor_agent
from debugger import debugger_agent


def execute_step(
    step,
    user_request,
    project_context,
    execution_result
):

    agent_name = step["agent"]

    action = step["action"]

    print(f"\nExecuting: [{agent_name}] {action}\n")

    if agent_name == "Explorer":

        return explorer_agent(
            "sample_project",
            user_request
        )

    elif agent_name == "Executor":

        return executor_agent(
            "sample_project/app.py"
        )

    elif agent_name == "Debugger":

        return debugger_agent(
            execution_result["stderr"],
            project_context
        )

    else:

        print(f"Unknown agent: {agent_name}")

        return None