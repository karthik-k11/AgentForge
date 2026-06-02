import os


def is_patch_allowed(
    file_path,
    safety_config
):

    normalized_path = os.path.normpath(
        file_path
    )

    for protected in safety_config[
        "protected_paths"
    ]:

        if protected in normalized_path:

            return False

    for directory in safety_config[
        "allowed_directories"
    ]:

        if directory in normalized_path:

            return True

    return False