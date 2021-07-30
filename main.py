import os
from plyer import notification

# make a directory if doesn't exist alredy
def makeDir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# move the files from list in folder
def mover(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

# notify after clutter cleared
def notificate(title, message):
    notification.notify(
        title = title,
        message = message,
        app_name = "Clutter Remover",
        app_icon = "clutter.ico",
        timeout = 3,
        ticker = "Clutter Cleared",
        toast = False
    )  
        
if __name__ == "__main__":

# skip this files and folders 
    all_files = os.listdir()
    all_files.remove('main.py')
    all_files.remove('clutter.ico')
    all_files.remove('Folders')


    # list all the images
    imgExt = ['.jpg', '.png', '.ico']
    images = [file for file in all_files if os.path.splitext(file)[1].lower() in imgExt]

    # list all the documents
    docExt = ['.doc', '.pdf', '.docx', '.txt', '.csv']
    documents = [file for file in all_files if os.path.splitext(file)[1].lower() in docExt]

    # list all the medias
    mediaExt = ['.mp4', '.mkv', '.mp3']
    medias = [file for file in all_files if os.path.splitext(file)[1].lower() in mediaExt]

    # list all the folders
    folderExt = ['']
    folder = [file for file in all_files if os.path.splitext(file)[1].lower() in folderExt]

    # list all rest items
    others = []

    for file in all_files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExt) and (ext not in docExt) and (ext not in mediaExt) and os.path.isfile(file):
            if os.path.splitext(file)[1].lower() != '.lnk' and os.path.splitext(file)[1].lower() != '.ini': # skip the .lnk and .ini items
                others.append(file)

# checking the length of items before creating directory
    if len(images)>0:
        makeDir('Images')
    if len(medias)>0:
        makeDir('Medias')
    if len(documents)>0:
        makeDir('Files')
    if len(folder)>0:
        makeDir('Folders')
    if len(others)>0:
        makeDir('Others')       

    mover('Images', images)
    mover('Medias', medias)
    mover('Files', documents)
    mover('Folders', folder)
    mover('Others', others)

    message = f"Images : {len(images)} \n Medias : {len(medias)} \n Documents : {len(documents)} \n Others : {len(others)} \n Folders : {len(folder)}"
    
    notificate("Clutter Cleared!", message)