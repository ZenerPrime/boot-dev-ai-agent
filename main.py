import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function


def main():
    argsLen = len(sys.argv)
    if argsLen < 2:
        print("Invalid input. Try again.")
        sys.exit(1)
    
    user_prompt = sys.argv[1]
    verbose = False

    if "--verbose" in sys.argv:
        verbose = True

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    messages = [
        types.Content(role= "user", parts=[types.Part(text= user_prompt)])
    ]

    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )

    schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads the contents of files, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to read, relative to the working directory.",
                ),
            },
        ),
    )

    schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Write or overwrite files, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The file to write, relative to the working directory. If it exists it will be over-written",
                ),
                "content": types.Schema(
                    type=types.Type.STRING,
                    description="The content to write to the file",
                )
            },
        ),
    )

    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Execute Python files with optional arguments, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The script file to execute, relative to the working directory.",
                )
            },
        ),
    )

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_write_file,
            schema_run_python_file,
        ]
    )

    for i in range(20):
        response = client.models.generate_content(
            model= "gemini-2.0-flash-001",
            contents= messages,
            config= types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction= system_prompt))
        
        for candidate in response.candidates:
            messages.append(candidate.content)

        if verbose:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count }")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count }")
            print("\n")

        if response.function_calls:
            for function_call_part in response.function_calls:
                messages.append(call_function(function_call_part, verbose))
        else:
            break
    
    print("Final Reaponse:\n")
    print(response.text)

main()