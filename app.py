import json
import os
import traceback
import urllib.request

from flask import Flask, jsonify, redirect, request
from flask_cors import CORS

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")

app = Flask(__name__)
CORS(app)

def get_api(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Musique/1.0 (+https://github.com/SlashNephy/Musique)"
        }
    )

    with urllib.request.urlopen(request) as response:
        content = response.read()
        return json.loads(content.decode())

def get_recent_tracks(username):
    return get_api(f"https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={LASTFM_API_KEY}&limit=1&extended=1&format=json")

def get_top_tracks(username, period):
    return get_api(f"https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={username}&api_key={LASTFM_API_KEY}&period={period}&format=json")

def get_top_artists(username, period):
    return get_api(f"https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={username}&api_key={LASTFM_API_KEY}&period={period}&format=json")

@app.route("/recent_track/<username>")
def recent_track(username):
    try:
        response = get_recent_tracks(username)

        track = response["recenttracks"]["track"][0]
        return jsonify(track)
    except Exception:
        traceback.print_exc()
        return jsonify({})

@app.route("/top_tracks/<username>")
def top_track(username):
    try:
        period = request.args.get("period", "overall")
        response = get_top_tracks(username, period)

        tracks = response["toptracks"]["track"]
        return jsonify(tracks)
    except Exception:
        traceback.print_exc()
        return jsonify([])

@app.route("/top_artists/<username>")
def top_artist(username):
    try:
        period = request.args.get("period", "overall")
        response = get_top_artists(username, period)

        artists = response["topartists"]["artist"]
        return jsonify(artists)
    except Exception:
        traceback.print_exc()
        return jsonify([])

@app.route("/")
def index():
    return redirect("https://github.com/SlashNephy/Musique")


if __name__ == "__main__":
    if not LASTFM_API_KEY:
        raise RuntimeError("LASTFM_API_KEY is not set.")

    app.debug = True
    app.run()
