import os,shutil

def convert(basePath, newPath, file, destDirectory):
    with open(file, "r") as plfile, open(os.path.join(destDirectory, os.path.basename(file)), "w") as destfile:
        destfile.write("#EXTM3U\n")
        musicfiles = [i for i in plfile if i != "#EXTM3U\n"]
        for i in musicfiles:
            destfile.write(i.replace(basePath, newPath).replace("\\", "/"))
        plfile.close()
        destfile.close()

def copy(file, destDirectory):
    with open(file, "r") as plfile:
        musicfiles = [i for i in plfile if i != "#EXTM3U\n"]
        for i in musicfiles:
            try:
                shutil.copyfile(i.rstrip(), os.path.join(destDirectory, os.path.basename(i)))
            except:
                print("Playlist file contains invalid path, and/or destination is invalid")

class fileInfo:
    def __init__(self):
        self.basePath = None
        self.newPath = None
        self.playlistPath = None
        
    def setplaylistPath(self, x):
        self.playlistPath = x
    
    def getplaylistPath(self):
        return self.playlistPath
