from planner import planner_agent
from explorer import explorer_agent
from executor import executor_agent
from debugger import debugger_agent
from codegen import code_generator_agent
from reviewer import reviewer_agent
from file_writer import write_fix_to_file


def main():

    print("\n=== AgentForge ===\n")

    user_request = input("Describe your software problem:\n\n> ")

    print("\nGenerating plan...\n")

    plan = planner_agent(user_request)

    tasks = plan["tasks"]

    print("=== TASK LIST ===\n")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print("\n=== EXPLORER AGENT ===\n")

    files = explorer_agent("sample_project")

    for file in files:
        print(file["file_path"])

    target_file = "sample_project/app.py"

    max_retries = 2

    retry_count = 0

    while retry_count < max_retries:

        print(f"\n=== EXECUTION ATTEMPT {retry_count + 1} ===\n")

        execution_result = executor_agent(target_file)

        print("STDOUT:\n")
        print(execution_result["stdout"])

        print("STDERR:\n")
        print(execution_result["stderr"])

        ##Success condition
        if execution_result["success"]:

            print("\nApplication executed successfully")

            break

        print("\n=== DEBUGGER AGENT ===\n")

        debug_result = debugger_agent(
            execution_result["stderr"],
            files[0]["content"]
        )

        print(debug_result)

        print("\n=== CODE GENERATOR AGENT ===\n")

        generated_fix = code_generator_agent(
            execution_result["stderr"]
        )

        print(generated_fix)

        print("\n=== REVIEWER AGENT ===\n")

        review_result = reviewer_agent(
            execution_result["stderr"],
            generated_fix
        )

        print(review_result)

        if "ACCEPT" in review_result:

            print("\n=== FILE WRITER ===\n")

            backup_file = write_fix_to_file(
                target_file,
                generated_fix
            )

            print(f"Backup created: {backup_file}")

            print("Generated fix written successfully")

        else:

            print("\nFix rejected. Retry required")

        retry_count += 1

    print("\n=== AGENTFORGE FINISHED ===\n")


if __name__ == "__main__":
    main()