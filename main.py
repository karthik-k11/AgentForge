from planner import planner_agent
from tasks import generate_tasks
from explorer import explorer_agent
from debugger import debugger_agent
from codegen import code_generator_agent
from executor import executor_agent


def main():

    print("\n=== AgentForge ===\n")

    user_request = input("Describe your software problem:\n\n> ")

    print("\nGenerating plan...\n")

    plan = planner_agent(user_request)

    tasks = generate_tasks(plan)

    print("=== TASK LIST ===\n")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print("\n=== EXPLORER AGENT ===\n")

    files = explorer_agent("sample_project")

    for file in files:
        print(file)

    print("\n=== EXECUTOR AGENT ===\n")

    execution_result = executor_agent(
        "sample_project/broken_script.py"
    )

    print("STDOUT:\n")
    print(execution_result["stdout"])

    print("STDERR:\n")
    print(execution_result["stderr"])

    print("\n=== DEBUGGER AGENT ===\n")

    debug_result = debugger_agent(
        execution_result["stderr"]
    )

    print(debug_result)

    print("\n=== CODE GENERATOR AGENT ===\n")

    generated_fix = code_generator_agent(
        execution_result["stderr"]
    )

    print(generated_fix)


if __name__ == "__main__":
    main()