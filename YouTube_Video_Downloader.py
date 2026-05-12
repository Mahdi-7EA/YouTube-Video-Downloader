import yt_dlp

yt_dlp.YoutubeDL({'format': 'best', 'outtmpl': '%(title)s.%(ext)s'}).download(['YOUTUBE_VIDEO_URL'])