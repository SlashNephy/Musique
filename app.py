import os
import json
import urllib.request
from flask import Flask, jsonify
from flask_cors import CORS

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")

app = Flask(__name__)
CORS(app)

def get_recent_tracks(username):
    request = urllib.request.Request(
        f"https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={username}&api_key={LASTFM_API_KEY}&format=json",
        headers={
            "User-Agent": "Musique/1.0 (+https://github.com/SlashNephy/Musique)"
        }
    )

    with urllib.request.urlopen(request) as response:
        content = response.read()
        return json.loads(content.decode())

@app.route("/<username>")
def api(username):
    try:
        response = get_recent_tracks(username)

        track = next(iter(response["track"]), None)
        return jsonify(track)
    except Exception as e:
        print(e)
        return jsonify({})


if __name__ == "__main__":
    if not LASTFM_API_KEY:
        raise RuntimeError("LASTFM_API_KEY is not set.")

    app.run()
