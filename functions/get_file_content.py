import os

def get_file_content(working_directory, file_path):
    try:
        if working_directory == None or file_path == None:
            return 'Error: Invalid arguments passed'
        if not os.path.isdir(working_directory):
            return f'Error: "{working_directory}" is not a directory'
        new_path = os.path.join(working_directory, file_path)
        if not os.path.isfile(new_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(new_path)

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            
        MAX_CHARS = 10000

        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if os.path.getsize(abs_file_path) > MAX_CHARS:
            file_content_string += f'\n[...File "{file_path}" truncated at 10000 characters]'
        
        return file_content_string
    
    except Exception as ex:
        return f"Error: {ex}"