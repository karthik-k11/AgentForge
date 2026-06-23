import os


def explorer_agent(project_path, user_request):

    discovered_files = []

    combined_context = ""

    request_keywords = user_request.lower().split()

    for root, dirs, files in os.walk(project_path):

        for file in files:

            if file.endswith(".py"):

                full_path = os.path.join(root, file)

                try:

                    with open(full_path, "r", encoding="utf-8") as code_file:

                        code_content = code_file.read()

                    relevance_score = 0

                    for keyword in request_keywords:

                        if keyword in code_content.lower():

                            relevance_score += 1

                    discovered_files.append({
                        "file_path": full_path,
                        "content": code_content,
                        "relevance_score": relevance_score
                    })

                except Exception as error:

                    discovered_files.append({
                        "file_path": full_path,
                        "content": f"Error reading file: {error}",
                        "relevance_score": 0
                    })

    ##Sort most relevant files first
    discovered_files.sort(
        key=lambda file: file["relevance_score"],
        reverse=True
    )

    ##Select top 3 relevant files
    top_files = discovered_files[:3]

    for file in top_files:

        combined_context += f"""

# FILE: {file["file_path"]}

{file["content"]}

"""

    return {
        "files": top_files,
        "project_context": combined_context
    }