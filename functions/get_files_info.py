import os

def get_files_info(working_directory, directory=None):

    target_path = os.path.abspath(os.path.join(working_directory, directory))
    if not target_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if os.path.isdir(target_path) == False:
        return f'Error: "{directory}" is not a directory'
    
    try:
        file_list = os.listdir(path=target_path)
        all_files = []
        for file in file_list:
            full_file_path = os.path.join(target_path, file)
            if os.path.isfile(full_file_path) == True:
                size = os.path.getsize(full_file_path)
                all_files.append(f"- {file}: file_size={size} bytes, is_dir={os.path.isdir(full_file_path)}")
            else:
                dir_size = os.path.getsize(full_file_path)
                all_files.append(f"- {file}: file_size={dir_size} bytes, is_dir={os.path.isdir(full_file_path)}")
        single_string = "\n".join(all_files)
        return single_string
    except Exception as e:
        return f"Error: {e}"
