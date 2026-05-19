import shutil


def write_fix_to_file(file_path, generated_code):

    backup_path = file_path + ".backup"

    ##Create backup
    shutil.copy(file_path, backup_path)

    ##Write new code
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(generated_code)

    return backup_path