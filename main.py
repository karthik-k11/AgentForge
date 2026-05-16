from planner import planner_agent
from tasks import generate_tasks
from explorer import explorer_agent
from debugger import debugger_agent


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

    print("\n=== DEBUGGER AGENT ===\n")

    sample_error = """
Traceback (most recent call last):
  File "app.py", line 10, in <module>
    print(username)
NameError: name 'username' is not defined
"""

    debug_result = debugger_agent(sample_error)

    print(debug_result)


if __name__ == "__main__":
    main()