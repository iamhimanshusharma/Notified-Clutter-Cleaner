import os
from plyer import notification

def makeDir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def mover(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

def notificate(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\pc\\Desktop\\python\\clutter.ico",
        timeout = 3
    )
    
        
if __name__ == "__main__":

    lister = os.listdir()
    lister.remove('main.py')

    makeDir('Images')
    makeDir('Medias')
    makeDir('Files')
    makeDir('Others')


    imgExt = ['.jpg', '.png', '.ico']
    images = [file for file in lister if os.path.splitext(file)[1].lower() in imgExt]

    docExt = ['.doc', '.pdf', '.docx', '.txt', '.csv']
    documents = [file for file in lister if os.path.splitext(file)[1].lower() in docExt]

    mediaExt = ['.mp4', '.mkv', '.mp3']
    medias = [file for file in lister if os.path.splitext(file)[1].lower() in mediaExt]

    others = []

    for file in lister:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in imgExt) and (ext not in docExt) and (ext not in mediaExt) and os.path.isfile(file):
            if os.path.splitext(file)[1].lower() != '.lnk' and os.path.splitext(file)[1].lower() != '.ini':
                others.append(file)
            

    mover('Images', images)
    mover('Medias', medias)
    mover('Files', documents)
    mover('Others', others)

    message = f"Images : {len(images)} \n Medias : {len(medias)} \n Documents : {len(documents)} \n Others : {len(others)}"
    
    notificate("Clutter Cleared", message)