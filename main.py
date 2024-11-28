import os, shutil

path1 = r"C:/Users/mural/Downloads/"
path2 = "C:/organizer/"

file_name = os.listdir(path1)

folder_names = ['csv files', 'pdf files', 'ppt files' , 'docs files' , 'image files' , 'music files','text files']
for loop in folder_names:
    if not os.path.exists(path2 + loop):
        os.makedirs(path2 + loop)
for file in file_name:
    if ".csv" in file and not os.path.exists(path2 + "csv files/" + file):
        shutil.move(path1 + file , path2 + 'csv files/' + file )
    elif ".pdf" in file and not os.path.exists(path2 + "pdf files/" + file):
        shutil.move(path1 + file , path2 + 'pdf files/' + file )
    elif ".ppt" in file and not os.path.exists(path2 + "ppt files/" + file):
        shutil.move(path1 + file , path2 + 'ppt files/' + file )
    elif ".docx" in file and not os.path.exists(path2 + "docs files/" + file):
        shutil.move(path1 + file , path2 + 'docs files/' + file )
    elif (".png" in file  or ".jpg" in file )and not os.path.exists(path2 + "image files/" + file):
        shutil.move(path1 + file , path2 + 'image files/' + file )
    elif ".mp3" in file and not os.path.exists(path2 + "music files/" + file):
        shutil.move(path1 + file , path2 + 'music files/' + file )
    elif ".txt" in file and not os.path.exists(path2 + "text files/" + file):
        shutil.move(path1 + file, path2 + 'text files/' + file)
    else:
        continue

