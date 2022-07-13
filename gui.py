from threading import Thread
import tkinter as tk, os, convert

window = tk.Tk()
window.geometry("850x700")
window.title("Welcome to garbage, enjoy your stay")
window.configure(bg="black")

fileInfo = convert.conversionAndCopyData(convert.getConfig(), window)

pathmsg1 = tk.Label(text = "Enter old playlist path format", bg="black", fg="white")
pathmsg2 = tk.Label(text = "Enter new playlist path format", bg="black", fg="white")
pathmsg3 = tk.Label(text = "Enter destination playlist path", bg="black", fg="white")
pathmsg4 = tk.Label(text = "Enter destination music path", bg="black", fg="white")

chosenFile = tk.Label(
    window,
    textvariable = fileInfo.file,
    bg="black", 
    fg="white"
)

oldpathInput = tk.Entry(
    window,
    width = 100,
    textvariable = fileInfo.basePath,
    bg="black",
    fg="white"
)

newpathInput = tk.Entry(
    window,
    width = 100,
    textvariable = fileInfo.newPath,
    bg="black",
    fg="white"
)

playlistDest = tk.Entry(
    window,
    width = 100,
    textvariable = fileInfo.playlistPath,
    bg="black",
    fg="white"
)

musicDest = tk.Entry(
    window,
    width = 100,
    textvariable = fileInfo.destDirectory,
    bg="black",
    fg="white"
)

readout = tk.Text(
    window,
    height = 31, 
    width = 121,
    bg = "black",
    fg = "white",
    state="disabled"
)

addfile = tk.Button(
    window,
    text="Choose .m3u file",
    width=15,
    height=1,
    bg="black",
    fg="white",
    activebackground='black', 
    activeforeground='white',
    command = lambda: convert.chooseFile(readout, fileInfo)
)

convertPlaylist = tk.BooleanVar()
copyFiles = tk.BooleanVar()

candc = tk.Button(
    window,
    text = "Execute",
    width=15,
    height=1,
    bg="black",
    fg="white",
    activebackground='black', 
    activeforeground='white',
    command = lambda: Thread(target=lambda: convert.convertAndCopy(readout, fileInfo, copyFiles, convertPlaylist)).start()
)

convertAffirm = tk.Checkbutton(
    window, 
    text = "Convert playlist",
    variable = convertPlaylist,
    onvalue = True,
    offvalue = False,
    bg="black",
    fg="white",
    activebackground='black', 
    activeforeground='white',
    selectcolor="black"
)

copyAffirm = tk.Checkbutton(
    window,
    text = "Copy music files",
    variable = copyFiles,
    onvalue = True,
    offvalue = False,
    bg="black",
    fg="white",
    activebackground='black', 
    activeforeground='white',
    selectcolor="black"
)

addfile.place(x=0, y=0)
chosenFile.pack(expand=True, fill=tk.X)
chosenFile.place(x=120, y=0)
pathmsg1.place(x=0, y=25)
oldpathInput.pack(expand=True, fill=tk.X)
oldpathInput.place(x=0, y=50)
pathmsg2.place(x=0, y=75)
newpathInput.pack(expand=True, fill=tk.X)
newpathInput.place(x=0, y=100)
pathmsg3.place(x=0, y=125)
playlistDest.pack(expand=True, fill=tk.X)
playlistDest.place(x=0, y=150)
pathmsg4.place(x=0, y=175)
musicDest.pack(expand=True, fill=tk.X)
musicDest.place(x=0, y=200)
convertAffirm.place(x=0, y=225)
copyAffirm.place(x=0, y=250)
candc.place(x=0, y=275)
readout.pack(expand=True, fill=tk.BOTH)
readout.place(x=0, y=300)

window.mainloop()
