import os

def get_files_info(working_directory, directory=None):
    try:
        if working_directory == None or not os.path.isdir(working_directory):
            return f'Error: "{working_directory}" is not a directory'
        new_path = os.path.join(working_directory, directory)
        if directory == None or not os.path.isdir(new_path):
            return f'Error: "{directory}" is not a directory'
        
        abs_working_dir = os.path.abspath(working_directory)
        abs_dir = os.path.abspath(new_path)

        if not abs_dir.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            
        results = []
        for entry in os.listdir(abs_dir):
            try:
                full_path = os.path.join(abs_dir, entry)
                results.append(f"{entry}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path):}")

                # if directory recurse
            except Exception as ex:
                return f"Error: {ex}"
            
        return "\n".join(results)
    
    except Exception as ex:
        return f"Error: {ex}"