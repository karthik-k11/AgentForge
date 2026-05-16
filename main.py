from planner import planner_agent
from tasks import generate_tasks
from explorer import explorer_agent


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


if __name__ == "__main__":
    main()