# 🎬 YouTube Video Downloader
 
A simple Python-based YouTube video downloader with **two modes** — standard quality and high quality (1080p) — using `yt-dlp`.
 
---
 
## 📋 Requirements
 
Before using this script, make sure you have the following installed:
 
- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://www.gyan.dev/ffmpeg/builds/) *(only required for High Quality Downloader)*
---
 
## ⚙️ Installation
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
 
### 2. Install yt-dlp
 
```bash
pip install yt-dlp
```
 
### 3. Install FFmpeg *(For High Quality Downloader only)*
 
FFmpeg is required to merge video and audio into a single file.
 
#### Windows:
1. Download FFmpeg from: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip
2. Extract the ZIP file (e.g., to `C:\ffmpeg-8.1.1-essentials_build`)
3. Add the `bin` folder to your System PATH:
   - Press `Win + R` → type `sysdm.cpl` → Enter
   - Go to **Advanced** → **Environment Variables**
   - Under **System variables**, select `Path` → **Edit** → **New**
   - Add the path to the `bin` folder, e.g.: `C:\ffmpeg-8.1.1-essentials_build\bin`
   - Click **OK → OK → OK**
4. Restart your terminal and verify:
```bash
ffmpeg -version
```
 
#### Linux / macOS:
```bash
# Ubuntu/Debian
sudo apt install ffmpeg
 
# macOS (Homebrew)
brew install ffmpeg
```
 
---
 
## 📁 Project Structure
 
```
your-repo-name/
│
├── YouTube_Video_Downloader.py               # Standard quality downloader
├── High_Quality_YouTube_Video_Downloader.py  # 1080p high quality downloader
└── README.md                                 # Project documentation
```
 
---
 
## 🚀 Usage
 
### ▶️ Option 1 — Standard Downloader (`YouTube_Video_Downloader.py`)
 
Downloads the best available single-stream quality (usually up to 720p). **FFmpeg not required.**
 
1. Open `YouTube_Video_Downloader.py`
2. Replace `YOUTUBE_VIDEO_URL` with your desired video link:
```python
yt_dlp.YoutubeDL({'format': 'best', 'outtmpl': '%(title)s.%(ext)s'}).download(['YOUR_URL_HERE'])
```
3. Run the script:
```bash
python YouTube_Video_Downloader.py
```
 
---
 
### ▶️ Option 2 — High Quality Downloader (`High_Quality_YouTube_Video_Downloader.py`)
 
Downloads video and audio separately and merges them into a **1080p MP4** file. **FFmpeg required.**
 
1. Open `High_Quality_YouTube_Video_Downloader.py`
2. Replace `YOUTUBE_VIDEO_URL` with your desired video link:
```python
yt_dlp.YoutubeDL(ydl_opts).download(['YOUR_URL_HERE'])
```
3. Run the script:
```bash
python High_Quality_YouTube_Video_Downloader.py
```
 
---
 
## 🔧 Quality Comparison
 
| Feature | Standard Downloader | High Quality Downloader |
|---|---|---|
| Max Quality | ~720p | Up to 1080p |
| Output Format | Varies | MP4 |
| FFmpeg Required | ❌ No | ✅ Yes |
| File Size | Smaller | Larger |
 
---
 
## 🛠️ Customize Quality
 
In `High_Quality_YouTube_Video_Downloader.py`, you can change `1080` to your preferred resolution:
 
```python
'format': 'bestvideo[height<=720]...'   # For 720p
'format': 'bestvideo[height<=480]...'   # For 480p
```
 
---
 
## ⚠️ Disclaimer
 
This tool is intended for **personal use only**. Please respect YouTube's [Terms of Service](https://www.youtube.com/t/terms) and only download videos you have permission to download.
 
---
 
## 📄 License
 
This project is open-source and available under the [MIT License](LICENSE).