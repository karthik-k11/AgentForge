from planner import planner_agent
from tasks import generate_tasks


def main():

    print("\n=== AgentForge ===\n")

    user_request = input("Describe your software problem:\n\n> ")

    print("\nGenerating plan...\n")

    plan = planner_agent(user_request)

    tasks = generate_tasks(plan)

    print("=== TASK LIST ===\n")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


if __name__ == "__main__":
    main()