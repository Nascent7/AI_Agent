from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_files_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file


# creates a list of available functions for the LLM to call
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_files_content,
        schema_run_python_file,
        schema_write_file
    ]
)

def call_function(function_call_part, verbose=False):
    if verbose == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"Calling function: {function_call_part.name}")

    allowed_funcs = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    args = dict(function_call_part.args)
    args["working_directory"] = "./calculator"
    func = allowed_funcs.get(function_call_part.name)
    if func is None:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    else:
        function_result = func(**args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result},
                )
            ],
        )
    