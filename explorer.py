import os

##Scans project folders & returns file list.

def explorer_agent(project_path):

    discovered_files = []

    for root, dirs, files in os.walk(project_path):

        for file in files:

            if file.endswith(".py"):

                full_path = os.path.join(root, file)

                discovered_files.append(full_path)

    return discovered_files