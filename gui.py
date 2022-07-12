import tkinter as tk, os, convert

window = tk.Tk()
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
    height = 10, 
    width = 100,
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
    command = lambda: convert.convertAndCopy(readout, fileInfo, copyFiles, convertPlaylist)
)

convertAffirm = tk.Checkbutton(
    window, 
    text = "Convert playlist",
    variable = convertPlaylist,
    onvalue = True,
    offvalue = False,
    bg="black",
    fg="white"
)

copyAffirm = tk.Checkbutton(
    window,
    text = "Copy music files",
    variable = copyFiles,
    onvalue = True,
    offvalue = False,
    bg="black",
    fg="white"
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
convertAffirm.pack()
copyAffirm.pack()
candc.pack()
readout.pack(expand=True, fill=tk.BOTH)

window.mainloop()
