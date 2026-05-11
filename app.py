from flask import Flask, request, jsonify
import yt_dlp
import uuid
import os

app = Flask(__name__)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route("/download")
def download():
    url = request.args.get("url")

    file_id = str(uuid.uuid4())
    output_path = f"{DOWNLOAD_DIR}/{file_id}.mp4"

    ydl_opts = {
        "outtmpl": output_path,
        "format": "bv*+ba/best",
        "quiet": True,
        "noplaylist": True,
        "http_headers": {
            "User-Agent": "Mozilla/5.0"
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return jsonify({
        "download_url": f"https://your-server-url/{output_path}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
