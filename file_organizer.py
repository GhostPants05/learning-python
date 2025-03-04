import os
import shutil

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx','.pptx'],
    'Excel': ['.xlsx'],
    'Text': [',txt'],
    'Scripts': ['.py', '.js', '.html', '.css']
}

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()

            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    folder_path = os.path.join(directory, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path))
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(directory, 'others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                    shutil.move(file_path, os.path.join(others_folder, filename))

if __name__ == "__main__":
    directory_to_organize = r"C:\Users\croix.chada\Documents\code\test"            #  input("Enter the path of the directory you want to organize: ")
    organize_files(directory_to_organize)
    print("Files organized!")

    