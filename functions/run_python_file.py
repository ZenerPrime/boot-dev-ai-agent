import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        if working_directory == None or file_path == None:
            return 'Error: Invalid arguments passed'
        if not os.path.isdir(working_directory):
            return f'Error: "{working_directory}" is not a directory'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        new_path = os.path.join(working_directory, file_path)
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(new_path)

        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        if not os.path.isfile(new_path):
            return f'Error: File "{file_path}" is not a regular file'
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            
        completeProcess = subprocess.run(['python3', abs_file_path], capture_output=True, text=True, timeout=30, cwd=abs_working_dir)

        output = ""
        if len(completeProcess.stdout) != 0:
            output = f"STDOUT: {completeProcess.stdout}\n"

        if len(completeProcess.stderr) != 0:
            output += F"STDERR: {completeProcess.stderr}\n"

        if completeProcess.returncode != 0:
            output += f"Process exited with code {completeProcess.returncode}"
            
        return output if len(output) > 0 else "No output produced"        
    
    except Exception as ex:
        return f"Error: executing Python file: {ex}"