from concurrent.futures import ThreadPoolExecutor
import os,shutil, json, hashlib, tkinter as tk
import re
from tkinter.filedialog import askopenfilename

# Produce hex md5 string for given filename; if nothing is found, return empty hash
def getHash(filename):
    fhash = hashlib.md5()
    try:
        with open(filename,"rb") as mfile:
            for chunk in iter(lambda: mfile.read(4096), b""):
                fhash.update(chunk)
    except:
        pass
    return fhash.hexdigest()

# Send line to log box
# TODO: #5 improve the way this is handled - lines no longer visible should autoprune
def sendOutput(readout, line):
    readout.configure(state="normal")
    readout.insert("1.0", line + " \n")
    readout.configure(state="disabled")

# Ask user to select playlist file
def chooseFile(readout, fileInfo):
    filename = askopenfilename(filetype=[("Playlist file", "*.m3u"),("Playlist file", "*.m3u8")])
    if filename != "":
        fileInfo.file.set(filename)
        sendOutput(readout, "Playlist file set to " + filename)
    elif fileInfo.file.get() != "":
        pass
    else:
        sendOutput(readout, "No file chosen")

# If convert flag is set, convert playlist; if copy flag is set, copy music files
def convertAndCopy(readout, fileInfo, copyFiles, convertPlaylist):
    storeConfig(fileInfo)
    if convertPlaylist.get():
        convert(fileInfo.basePath.get().strip(), fileInfo.newPath.get().strip(), fileInfo.file.get(), fileInfo.playlistPath.get().strip())
        sendOutput(readout, "Playlist converted and written to " + fileInfo.playlistPath.get().strip())
    if copyFiles.get():
        copy(fileInfo.file.get(), fileInfo.destDirectory.get().strip(), fileInfo.basePath.get().strip(), readout)
        sendOutput(readout, "Files copied to " + fileInfo.destDirectory.get().strip())

# Save last used options into data file
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

# Load last saved options from data file
def getConfig():
    try:
        with open(os.path.join(os.getcwd(), "data.json"), "r") as datafile:
            lastdata = json.load(datafile)
            return[lastdata['basePath'], lastdata['newPath'], lastdata['playlistPath'], lastdata['file'], lastdata['destDirectory']]
    except:
        return["","","","",""]

# Convert playlist to new format
def convert(basePath, newPath, file, destDirectory):
    with open(file, "r", encoding="utf-8-sig") as plfile, open(os.path.join(destDirectory, os.path.basename(file)), "w", encoding="utf-8-sig") as destfile:
        destfile.write("#EXTM3U\n")
        musicfiles = [i for i in plfile if i != "#EXTM3U\n"]
        for i in musicfiles:
            destfile.write(i.replace(basePath, newPath).replace("\\", "/"))
        plfile.close()
        destfile.close()

# Copy music files to new destination
def copy(file, destDirectory, basePath, readout):
    with open(file, "r", encoding="utf-8-sig") as plfile:
        musicfiles = [i.rstrip() for i in plfile if i != "#EXTM3U\n"]
        filecount = 1
        for i in musicfiles:
            fhash = getHash(i)
            subdir = os.path.relpath(i, basePath)
            filepath = os.path.join(destDirectory, subdir)
            dir = os.path.dirname(filepath)
            if not os.path.exists(dir):
                os.makedirs(dir)
            try:
                dhash = getHash(filepath)
                tries = 0
                if dhash == fhash:
                    sendOutput(readout, "File " + filepath + " already exists (" + str(filecount) + " of " + str(len(musicfiles)) + ")")
                while fhash != dhash and tries < 6:
                    tries += 1
                    sendOutput(readout, "Copying " + i + " to " + filepath + " (" + str(filecount) + " of " + str(len(musicfiles)) + ")")
                    shutil.copyfile(i, filepath)
                    dhash = getHash(filepath)
                    if fhash != dhash:
                        if os.path.exists(filepath):
                            os.remove(filepath)
                        if tries < 6:
                            sendOutput(readout, "Hash verification failed; recopying")
                        else:
                            sendOutput(readout, "File " + i + " failed to verify five times; aborting")
                    else:
                        sendOutput(readout, "Hash verify success")
            except Exception as e:
                print(e)
            filecount += 1

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
        