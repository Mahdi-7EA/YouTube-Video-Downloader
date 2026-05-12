import yt_dlp

ydl_opts = {
    'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'outtmpl': '%(title)s.%(ext)s',
    'merge_output_format': 'mp4',
}

yt_dlp.YoutubeDL(ydl_opts).download(['YOUTUBE_VIDEO_URL'])