import os
import shutil

target_folder = "F:\THE-ALIGNER\mymessyfolder"

"""

all_items = os.listdir(target_folder)

print("All files inside the folder:")
print(all_items)

for item in all_items:
    full_path = os.path.join(target_folder , item)
    
    if os.path.isfile(full_path):
        file_name , extension = os.path.splitext(item)
        
        print(f"File found : {item} | Extension : {extension}")
        
"""

Extension_map = {
    '.jpg' : 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.mps3': 'Audio',
    '.wav': 'Audio',
    '.zip': 'Archives'
    
}

all_items = os.listdir(target_folder)

for item in all_items:
    full_path = os.path.join(target_folder,item)
    
    if os.path.isfile(full_path):
        file_name, extension = os.path.splitext(item)
        
        extension = extension.lower()
        
        if extension in Extension_map:
            folder_name = Extension_map[extension]
            destination_folder = os.path.join(target_folder, folder_name)
            
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                print(f"Created new Folder :{folder_name}")
                
            final_file_path = os.path.join(destination_folder,item)
            
            
            shutil.move(full_path, final_file_path)
            print(f"Moved:{item} -> {folder_name}/")
            
print("\n Cleanup complete!YOur folder is organized ")
                
                
                
                
            
