from google.genai import types

from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *

def call_function(function_call_part, verbose=False): 
    functions = {
        "run_python_file": run_python_file,
        "write_file": write_file,
        "get_files_info": get_files_info,
        "get_file_content": get_file_content
    }

    if (verbose):
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_name = function_call_part.name
    args = function_call_part.args.copy()

    args["working_directory"] = "./calculator"    
    
    if function_name not in functions:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    function_result = functions[function_call_part.name](**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )