import json
import os
import traceback
import urllib.request

from flask import Flask, jsonify, redirect
from flask_cors import CORS

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")

app = Flask(__name__)
CORS(app)

def get_recent_tracks(username):
    request = urllib.request.Request(
        f"https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={LASTFM_API_KEY}&limit=1&extended=1&format=json",
        headers={
            "User-Agent": "Musique/1.0 (+https://github.com/SlashNephy/Musique)"
        }
    )

    with urllib.request.urlopen(request) as response:
        content = response.read()
        return json.loads(content.decode())

@app.route("/recent_track/<username>")
def recent_track(username):
    try:
        response = get_recent_tracks(username)

        track = response["recenttracks"]["track"][0]
        return jsonify(track)
    except Exception:
        traceback.print_exc()
        return jsonify({})

@app.route("/")
def index():
    return redirect("/AsteriaNocturna")


if __name__ == "__main__":
    if not LASTFM_API_KEY:
        raise RuntimeError("LASTFM_API_KEY is not set.")

    app.debug = True
    app.run()
