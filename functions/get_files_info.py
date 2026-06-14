import os.path


def get_files_info(working_directory: str, directory: str = ".") -> str | None:
    target_dir = os.path.normpath(os.path.join(os.path.abspath(working_directory), directory))
    valid_target = os.path.commonpath([os.path.abspath(working_directory), target_dir]) == os.path.abspath(working_directory)
    if not valid_target:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    if valid_target:
        return f'Success: "{directory}" is within the working directory'
    return None
