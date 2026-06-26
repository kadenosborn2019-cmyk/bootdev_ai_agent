import os.path
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str | None:
    try:
        target_file: str = os.path.normpath(os.path.join(os.path.abspath(working_directory), file_path))
        valid_target: bool = os.path.abspath(working_directory) == os.path.commonpath([os.path.abspath(working_directory), target_file])
        if not valid_target:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", os.path.abspath(target_file)]
        if args is not None:
            command.extend(args)
        result = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=working_directory)
        exit_code = result.returncode
        output: str = ""
        if exit_code > 0:
            output += f'Process exited with code {exit_code}'
        if not result.stdout and not result.stderr:
            output += f'No output produced'
        else:
            output += f'STDOUT:\n{result.stdout}'
            output += f'STDERR:\n{result.stderr}'
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"

