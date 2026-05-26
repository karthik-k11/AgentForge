from explorer import explorer_agent
from executor import executor_agent
from debugger import debugger_agent
from codegen import code_generator_agent
from reviewer import reviewer_agent


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

        result = reviewer_agent(
            workflow_state["execution_result"]["stderr"],
            workflow_state["generated_fix"]
        )

        workflow_state["review_result"] = result

        return result

    else:

        print(f"Unknown agent: {agent_name}")

        return None