# Importing required module
import os
program = "sudo yt-dlp --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 96K --yes-playlist "
url = input('Enter Playlist URL: ')
print("...Running Program...")
os.system(program+url)