def generate_tasks(plan_text):

    lines = plan_text.split("\n")

    tasks = []

    for line in lines:

        line = line.strip()

        if line:

            ##Remove numbering like:
            ##1. Task
            cleaned = line.split(". ", 1)

            if len(cleaned) > 1:
                task = cleaned[1]
            else:
                task = line

            tasks.append(task)

    return tasks