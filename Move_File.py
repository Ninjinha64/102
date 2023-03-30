import os
import shutil

from_dir = "/Users/Este computador//Dowloads//"
to_dir = "/Users/Este computador//Dowloads//Projeto 102"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    
    if ext == "":
        continue
    # tipos de documentos 
    elif ext in [".txt", ".doc", ".docx", ".pdf"]:
        
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + ext[1:].upper()
        path3 = to_dir + '/' + ext[1:].upper() + '/' + file_name
       
        if os.path.exists(path2):
            print("Movendo:", file_name)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo:", file_name)
            shutil.move(path1, path3)
