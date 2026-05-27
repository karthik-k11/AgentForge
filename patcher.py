import os
import shutil


def apply_patch(target_file, generated_fix):

    try:

        backup_file = target_file + ".backup"

        # Create backup
        shutil.copy(target_file, backup_file)

        # Write generated fix
        with open(
            target_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(generated_fix)

        return {
            "success": True,
            "backup_file": backup_file
        }

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }