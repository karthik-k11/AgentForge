import os
import shutil


def apply_patch(
    target_file,
    generated_fix,
    failed_line=None
):

    try:

        backup_file = target_file + ".backup"

        # Create backup
        shutil.copy(
            target_file,
            backup_file
        )

        # Read original file
        with open(
            target_file,
            "r",
            encoding="utf-8"
        ) as file:

            original_content = file.readlines()

        # Smart patch if line number exists
        if (
            failed_line is not None
            and
            1 <= failed_line <= len(
                original_content
            )
        ):

            replacement_lines = [
                line + "\n"
                for line in generated_fix.splitlines()
            ]

            original_content[
                failed_line - 1:
                failed_line
            ] = replacement_lines

            with open(
                target_file,
                "w",
                encoding="utf-8"
            ) as file:

                file.writelines(
                    original_content
                )

        else:

            # Fallback: replace entire file
            with open(
                target_file,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    generated_fix
                )

        return {
            "success": True,
            "backup_file": backup_file
        }

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }