import os.path

def get_file_content(working_directory: str, file_path: str) -> str | None:
    target_file: str = os.path.normpath(os.path.join(os.path.abspath(working_directory), file_path))
    valid_target: bool = os.path.commonpath([os.path.abspath(working_directory), target_file]) == os.path.abspath(working_directory)
    character_maximum = 10000
    if not valid_target:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if valid_target:
        with open(target_file) as f:
            file_content :str = f.read(character_maximum)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {character_maximum} characters]'
                return file_content
        return file_content
    return None