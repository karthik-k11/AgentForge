from planner import planner_agent
from router import execute_step
from state import create_workflow_state


def main():

    print("\n=== AgentForge ===\n")

    user_request = input(
        "Describe your software problem:\n\n> "
    )

    print("\nGenerating plan...\n")

    workflow_state = create_workflow_state()

    workflow_state["user_request"] = user_request

    plan = planner_agent(user_request)

    steps = plan["steps"]

    print("=== EXECUTION PLAN ===\n")

    for index, step in enumerate(steps, start=1):

        print(
            f"{index}. "
            f"[{step['agent']}] "
            f"{step['action']}"
        )

    print("\n=== EXECUTING PLAN ===\n")

    for step in steps:

        agent_name = step["agent"]

        execute_step(
            step,
            workflow_state
        )

        ##Explorer Output
        if agent_name == "Explorer":

            print("\n=== EXPLORER AGENT ===\n")

            for file in workflow_state["files"]:

                print(file["file_path"])

        ##Executor Output
        elif agent_name == "Executor":

            print("\n=== EXECUTOR AGENT ===\n")

            print("STDOUT:\n")

            print(
                workflow_state["execution_result"]["stdout"]
            )

            print("STDERR:\n")

            print(
                workflow_state["execution_result"]["stderr"]
            )
            print("\nFAILED FILE:\n")

            print(
                workflow_state["failed_file"]
            )

            print("\nEXECUTION STATUS:\n")

            print(
                workflow_state["execution_result"]["status"]
            )
            print("\nEXECUTION TIME:\n")

            print(
                workflow_state["execution_result"][
                    "execution_time"
                ],
                "seconds"
            )
            print("\nEXECUTION METADATA:\n")

            print(
                workflow_state["execution_metadata"]
            )

            ##Success condition
            if workflow_state["execution_result"]["success"]:

                print(
                    "\nApplication executed "
                    "successfully"
                )

                break

        ##Debugger Output
        elif agent_name == "Debugger":

            print("\n=== DEBUGGER AGENT ===\n")

            print(
                workflow_state["debug_analysis"]
            )

        ##Code Generator Output
        elif agent_name == "CodeGenerator":

            print(
                "\n=== CODE GENERATOR AGENT ===\n"
            )

            print(
                workflow_state["generated_fix"]
            )

        ##Reviewer Output
        elif agent_name == "Reviewer":

            print("\n=== REVIEWER AGENT ===\n")

            print(
                workflow_state["review_result"]
            )
            
            print("\n=== VALIDATOR AGENT ===\n")

            if workflow_state["validation_result"]["valid"]:

                print("Generated code is valid")

            else:

                print("Generated code is invalid")

                print(
                    workflow_state["validation_result"]["error"]
                )
            ##Patch result display
            if workflow_state["patch_result"]:

                print("\n=== PATCHER AGENT ===\n")

                if workflow_state["patch_result"]["success"]:

                    print("Patch applied successfully")

                    print(
                        "Backup created:",
                        workflow_state["patch_result"][
                            "backup_file"
                        ]
                    )

                else:

                    print("Patch failed")

                    print(
                        workflow_state["patch_result"]["error"]
                    )

    print("\n=== AGENTFORGE FINISHED ===\n")


if __name__ == "__main__":
    main()