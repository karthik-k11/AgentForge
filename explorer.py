import os


def explorer_agent(project_path):

    discovered_files = []

    for root, dirs, files in os.walk(project_path):

        for file in files:

            if file.endswith(".py"):

                full_path = os.path.join(root, file)

                try:

                    with open(full_path, "r", encoding="utf-8") as code_file:

                        code_content = code_file.read()

                    discovered_files.append({
                        "file_path": full_path,
                        "content": code_content
                    })

                except Exception as error:

                    discovered_files.append({
                        "file_path": full_path,
                        "content": f"Error reading file: {error}"
                    })

    return discovered_files