from flask import Flask, render_template, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

# যে ফোল্ডারে ভিডিও সেভ হবে
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def home():
    # ফ্রন্টএন্ড পেজ লোড করবে
    return render_template('index.html')

@app.route('/api/download', methods=['POST'])
def download_video():
    data = request.get_json()
    video_url = data.get('url')

    if not video_url:
        return jsonify({'success': False, 'message': 'দয়া করে ইউটিউব ভিডিওর লিঙ্ক দিন!'}), 400

    # আপনার দেওয়া yt-dlp কনফিগারেশন
    ydl_opts = {
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'), # downloads ফোল্ডারে সেভ হবে
        'merge_output_format': 'mp4',
        'noplaylist': True # প্লেলিস্ট ডাউনলোড বন্ধ করতে
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return jsonify({'success': True, 'message': 'ভিডিওটি সফলভাবে "downloads" ফোল্ডারে সেভ হয়েছে!'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'এরর: {str(e)}'}), 500

if __name__ == '__main__':
    # Localhost এ অ্যাপটি রান করবে
    app.run(debug=True, port=5000)