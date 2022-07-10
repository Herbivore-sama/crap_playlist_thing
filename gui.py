from tkinter.filedialog import askopenfilename
import tkinter as tk, os, convert

fileInfo = convert.fileInfo()

def chooseFile():
    filename = askopenfilename(filetype=[("Playlist file", "*.m3u")])
    if filename != "":
        fileInfo.setplaylistPath(filename)
        readout.configure(state="normal")
        readout.insert("1.0", "Playlist file set to " + filename + "\n")
        readout.configure(state="disabled")
        chosenFileText.set(filename)
    elif fileInfo.getplaylistPath != "":
        pass
    else:
        readout.configure(state="normal")
        readout.insert("1.0", "No file chosen\n")
        readout.configure(state="disabled")

def convertAndCopy():
    oldpath = oldpathInput.get().strip()
    print(oldpath)
    newpath = newpathInput.get().strip()
    print(newpath)
    pdest = playlistDest.get().strip()
    print(pdest)
    mdest = musicDest.get().strip()
    print(mdest)
    convert.convert(oldpath, newpath, fileInfo.getplaylistPath(), pdest)
    convert.copy(fileInfo.getplaylistPath(), mdest)

window = tk.Tk()
window.title("Welcome to garbage, enjoy your stay")

pathmsg1 = tk.Label(text = "Enter old playlist path format")
pathmsg2 = tk.Label(text = "Enter new playlist path format")
pathmsg3 = tk.Label(text = "Enter destination playlist path")
pathmsg4 = tk.Label(text = "Enter destination music path")

chosenFileText = tk.StringVar()

chosenFile = tk.Entry(
    window,
    width = 100,
    textvariable = chosenFileText,
    state = "disabled"
)

oldpathInput = tk.Entry(
    window,
    width = 100
)

newpathInput = tk.Entry(
    window,
    width = 100
)

playlistDest = tk.Entry(
    window,
    width = 100
)

musicDest = tk.Entry(
    window,
    width = 100
)

readout = tk.Text(
    window,
    height = 10, 
    width = 100,
    bg = "white",
    fg = "black",
    state="disabled"
)

addfile = tk.Button(
    window,
    text="Choose .m3u file",
    width=15,
    height=1,
    bg="white",
    fg="black",
    command = chooseFile
)

candc = tk.Button(
    window,
    text = "Convert and Copy",
    width=15,
    height=1,
    bg="white",
    fg="black",
    command = convertAndCopy
)

addfile.pack()
chosenFile.pack(expand=True, fill=tk.X)
pathmsg1.pack()
oldpathInput.pack(expand=True, fill=tk.X)
pathmsg2.pack()
newpathInput.pack(expand=True, fill=tk.X)
pathmsg3.pack()
playlistDest.pack(expand=True, fill=tk.X)
pathmsg4.pack()
musicDest.pack(expand=True, fill=tk.X)
candc.pack()
readout.pack(expand=True, fill=tk.BOTH)

window.mainloop()