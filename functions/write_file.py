import os

def write_file(working_directory, file_path, content):
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    directory = os.path.dirname(target_path)
    try:
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(target_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'