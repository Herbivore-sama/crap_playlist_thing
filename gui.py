import tkinter as tk, os, convert

window = tk.Tk()
window.title("Welcome to garbage, enjoy your stay")

fileInfo = convert.conversionAndCopyData(convert.getConfig(), window)

pathmsg1 = tk.Label(text = "Enter old playlist path format")
pathmsg2 = tk.Label(text = "Enter new playlist path format")
pathmsg3 = tk.Label(text = "Enter destination playlist path")
pathmsg4 = tk.Label(text = "Enter destination music path")

chosenFileText = tk.StringVar()

chosenFile = tk.Entry(
    window,
    width = 100,
    textvariable = fileInfo.file,
    state = "disabled"
)

oldpathInput = tk.Entry(
    window,
    width = 100,
    textvariable = fileInfo.basePath
)

newpathInput = tk.Entry(
    window,
    width = 100,
    textvariable = fileInfo.newPath
)

playlistDest = tk.Entry(
    window,
    width = 100,
    textvariable = fileInfo.playlistPath
)

musicDest = tk.Entry(
    window,
    width = 100,
    textvariable = fileInfo.destDirectory
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
    command = lambda: convert.chooseFile(readout, fileInfo)
)

convertPlaylist = tk.BooleanVar()
copyFiles = tk.BooleanVar()

candc = tk.Button(
    window,
    text = "Execute",
    width=15,
    height=1,
    bg="white",
    fg="black",
    command = lambda: convert.convertAndCopy(readout, fileInfo, copyFiles, convertPlaylist)
)

convertAffirm = tk.Checkbutton(
    window, 
    text = "Convert playlist",
    variable = convertPlaylist,
    onvalue = True,
    offvalue = False
)

copyAffirm = tk.Checkbutton(
    window,
    text = "Copy music files",
    variable = copyFiles,
    onvalue = True,
    offvalue = False
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
