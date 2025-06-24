import os
from google.genai import types


def get_file_content(working_directory, file_path):
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    abspath_working_dir = os.path.abspath(working_directory)

    if not target_path.startswith(abspath_working_dir):
        return f'Error: Cannot read "{target_path}" as it is outside the permitted working directory'
    
    if os.path.isfile(target_path) == False:
        return f'Error: File not found or is not a regular file: "{target_path}"'
    
    MAX_CHARS = 10000
    result_string = ""
    try:
        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= 10000:
                result_string = file_content_string + f'...File "{target_path}" truncated at 10000 characters'
            else:
                result_string = file_content_string
        return result_string
    except Exception as e:
        return f"Error: {e}"

schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of a file at the end of a file path with a character count cap of 10000, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file relative to the working directory, from which contents will be read.",
            ),
        },
    ),
)