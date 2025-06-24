import os
from google.genai import types

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
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to a file specified by the file path and is constrined to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to the file that will be written relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to be written to the file specified by the relative file path.",
            )
        },
        required=["file_path", "content"],
    ),
)