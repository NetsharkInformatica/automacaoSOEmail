import os

#diretorio raiz do SO
base_path= os.path.expanduser('~')
#print(base_path)

#navega até o diretorio download

path = os.path.join(base_path, 'Downloads')
#print(path)

work_dir = os.chdir(path)

#lista arquivos do diretorio

list_files= os.listdir(work_dir)
#print(list_files)

#4 organização dos arquivos

#4.1 criar pastas

type_files= ['exe','txt','pdf','docx','iso','jpeg',
              'png','mp4','pptx','rar','xlsx','7z',
              'zip','csv','avif','gz','jpg','apk','py','pem','.env','xfc']
for tipos in type_files:
    if tipos not in os.listdir():
        os.mkdir(tipos)
        
 #5 organizando arquivos
 
for file in list_files:
    for tipo in type_files:
        if '.' + tipo in file:
            old_path = os.path.join(path,file)
            new_path= os.path.join(path,tipo,file)
            os.replace(old_path,new_path)
     



