import os.path


def write_file(working_directory: str, file_path: str, content: str) -> str | None:
    target_file: str = os.path.normpath(os.path.join(os.path.abspath(working_directory), file_path))
    valid_target: bool = os.path.commonpath([os.path.abspath(working_directory), target_file]) == os.path.abspath(working_directory)
    if not valid_target:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if os.path.isdir(file_path):
        return f'Error: Cannot write to "{file_path}" is a directory'
    if target_file:
        target_file_parent = os.path.dirname(target_file)
        os.makedirs(target_file_parent, exist_ok=True)
        with open(target_file, "w") as f:
            f.write(content)
        if os.path.exists(target_file):
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    return None