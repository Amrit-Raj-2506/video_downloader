from pytube import Playlist
playlist=Playlist("https://www.youtube.com/watch?v=j6muwUGdvXw&list=RDj6muwUGdvXw&start_radio=1&t=0")
for video in playlist:
    video.streams.get_highest_resolution().download("F:/")
