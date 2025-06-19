import os

def write_file(working_directory, file_path, content):
    try:
        if working_directory == None or file_path == None or content == None:
            return 'Error: Invalid arguments passed'
        if not os.path.isdir(working_directory):
            return f'Error: "{working_directory}" is not a directory'
        new_path = os.path.join(working_directory, file_path)
        
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(new_path)

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        dirname = os.path.dirname(abs_file_path)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(abs_file_path, "w") as f:
            f.write(content)
                
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as ex:
        return f"Error: {ex}"