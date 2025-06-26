import os 
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    target_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_path):
        return f'Error: File "{file_path}" not found.'
    
    if not target_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(
            ["python3", file_path], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
            cwd=working_directory, 
            timeout=30,
        )
    except Exception as e:
        return f'Error: executing Python file: {e}'
    
    out = result.stdout.decode()
    err = result.stderr.decode()
    if out == "" and err == "":
        return "No output produced."
    else:
        result_str = f'STDOUT: {out}\nSTDERR: {err}'
        if result.returncode != 0:
            result_str = result_str + (f"\nProcess exited with code {result.returncode}")
        return result_str
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Exucutes the content of the file designated by the provided file path, and constrained by the working directory. Returns the STDOUT and STDERR if applicable.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path desginating the file to exucute relative to the working directory.",
            ),
        },
    ),
)