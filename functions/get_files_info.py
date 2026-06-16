import os.path


def get_files_info(working_directory: str, directory: str = ".") -> str | None:
    target_dir = os.path.normpath(os.path.join(os.path.abspath(working_directory), directory))
    valid_target = os.path.commonpath([os.path.abspath(working_directory), target_dir]) == os.path.abspath(working_directory)
    if not valid_target:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    if valid_target:
        if os.path.isdir(target_dir):
            files_info = []
            for file in os.listdir(target_dir):
                file_path = os.path.join(target_dir, file)
                file_size = (os.path.getsize(file_path))
                is_a_file = (os.path.isdir(file_path))
                formated_info = f"- {file}: file_size={file_size}, is_dir={is_a_file}"
                files_info.append(formated_info)
            return "\n".join(files_info)
    return None
