import os,shutil, json, tkinter as tk
from tkinter.filedialog import askopenfilename

def chooseFile(readout, fileInfo):
    filename = askopenfilename(filetype=[("Playlist file", "*.m3u")])
    if filename != "":
        fileInfo.file.set(filename)
        readout.configure(state="normal")
        readout.insert("1.0", "Playlist file set to " + filename + "\n")
        readout.configure(state="disabled")
    elif fileInfo.file.get() != "":
        pass
    else:
        readout.configure(state="normal")
        readout.insert("1.0", "No file chosen\n")
        readout.configure(state="disabled")

def convertAndCopy(readout, fileInfo, copyFiles, convertPlaylist):
    storeConfig(fileInfo)
    if convertPlaylist.get():
        convert(fileInfo.basePath.get().strip(), fileInfo.newPath.get().strip(), fileInfo.file.get(), fileInfo.playlistPath.get().strip())
        readout.configure(state="normal")
        readout.insert("1.0", "Playlist converted and written to " + fileInfo.playlistPath.get().strip() + " \n")
        readout.configure(state="disabled")
    if copyFiles.get():
        copy(fileInfo.file.get(), fileInfo.destDirectory.get().strip())
        readout.configure(state="normal")
        readout.insert("1.0", "Files copied to " + fileInfo.destDirectory.get().strip() + " \n")
        readout.configure(state="disabled")

def storeConfig(fileInfo):
    with open(os.path.join(os.getcwd(), "data.json"), "w") as datafile:
        filedict = {
            "basePath": fileInfo.basePath.get(),
            "newPath": fileInfo.newPath.get(),
            "playlistPath": fileInfo.playlistPath.get(),
            "file": fileInfo.file.get(),
            "destDirectory": fileInfo.destDirectory.get()
        }
        json.dump(filedict, datafile)

def getConfig():
    try:
        with open(os.path.join(os.getcwd(), "data.json"), "r") as datafile:
            lastdata = json.load(datafile)
            print(lastdata['basePath'])
            return[lastdata['basePath'], lastdata['newPath'], lastdata['playlistPath'], lastdata['file'], lastdata['destDirectory']]
    except:
        return["","","","",""]

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

class conversionAndCopyData:
    def __init__(self, config, window):
        self.basePath = tk.StringVar()
        self.basePath.set(config[0])
        self.newPath = tk.StringVar()
        self.newPath.set(config[1])
        self.playlistPath = tk.StringVar()
        self.playlistPath.set(config[2])
        self.file = tk.StringVar()
        self.file.set(config[3])
        self.destDirectory = tk.StringVar()
        self.destDirectory.set(config[4])