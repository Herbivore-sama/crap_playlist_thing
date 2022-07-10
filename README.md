# Crap Playlist Thing

I got sick of how awful most Android music apps are at sorting files, so I started using Syncthing and building the .m3u via Foobar2000. This is going to be just a simple Python script to automatically copy files to your chosen sync folder, convert the given playlist to the appropriate Android directory format, and then copy that as well. Who knows if I'll ever bother to actually complete it or push it up, I'm only using this account because I'm too embarrassed to put this anywhere where people who know me might recognize it as mine.

Run gui.py with convert.py in the same folder, you'll be asked for five inputs:

1. Source .m3u
2. Path to trim from the source
3. Destination folder path (basically the path to your music folder within the Android file system)
4. Music folder (the folder that Syncthing is offering for those files)
5. Playlist folder (same idea as 4, if you intend to use a different folder for playlists, which I do)

Once those are input and the user clicks on "Convert and Copy":

-All of the music files in the source .m3u are copied to the chosen directory  
-The source .m3u is also copied to its respective destination  
-The copied .m3u is then converted based on the paths specified in 2. and 3. above  

For an example of points 2. and 3., say you're using Windows, and your music is all stored in C:\Users\Me\Music - the source .m3u is going to look something like:

#EXTM3U  
C:\Users\Me\Music\01 - Turandot, Act 3_ Nessun Dorma.mp3  
C:\Users\Me\Music\02 - Les pecheurs de perles (The Pearl Fishers), Act 1_ Au f.mp3  
etc.

And then your Android music folder is located under ../../../sdcard/music - you give both of these paths to the GUI, and the output file becomes:

#EXTM3U  
../../../sdcard/music/01 - Turandot, Act 3_ Nessun Dorma.mp3  
../../../sdcard/music/02 - Les pecheurs de perles (The Pearl Fishers), Act 1_ Au f.mp3  
etc.

Riveting, and extremely useful, I know. Why am I even bothering to type all this out, it's not like anyone other than myself is ever going to read it. 1AM on a Sunday morning is a magical time. 
