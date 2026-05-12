from planner import planner_agent


def main():

    print("\n=== AgentForge ===\n")

    user_request = input("Describe your software problem:\n\n> ")

    print("\nGenerating plan...\n")

    plan = planner_agent(user_request)

    print("=== EXECUTION PLAN ===\n")
    print(plan)


if __name__ == "__main__":
    main()