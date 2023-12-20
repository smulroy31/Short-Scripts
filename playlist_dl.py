program = "yt-dlp --ignore-errors --format bestaudio --extract-audio --audio-format mp3 --audio-quality 96K --yes-playlist "
url = input('Enter Playlist URL: ')
exec(program + url)
