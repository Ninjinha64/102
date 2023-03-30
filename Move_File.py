import os
import shutil

from_dir = "/caminho/da/pasta/de/origem"
to_dir = "/caminho/da/pasta/de/destino/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, ext = os.path.splitext(file_name)
    # Se a extensão estiver em branco, pule para o próximo arquivo
    if ext == "":
        continue
    # Se a extensão não estiver em branco e estiver em uma lista de extensões
    elif ext in [".txt", ".doc", ".docx", ".pdf"]:
        # Crie os caminhos de origem e destino
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + ext[1:].upper()
        path3 = to_dir + '/' + ext[1:].upper() + '/' + file_name
        # Verifique se o caminho de destino existe e mova o arquivo
        if os.path.exists(path2):
            print("Movendo:", file_name)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo:", file_name)
            shutil.move(path1, path3)
