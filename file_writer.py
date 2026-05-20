import shutil


def write_fix_to_file(file_path, generated_code):

    backup_path = file_path + ".backup"

    ##Create backup
    shutil.copy(file_path, backup_path)

    ##Read original file
    with open(file_path, "r", encoding="utf-8") as file:
        original_code = file.read()

    ##Append generated fix safely
    updated_code = (
        original_code
        + "\n\n# ===== AI GENERATED PATCH =====\n\n"
        + generated_code
    )

    ##Write updated code
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_code)

    return backup_path