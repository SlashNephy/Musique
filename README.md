# Musique

🎧 Last.fm 経由で最近再生したトラック情報などを返すだけの API サーバ

## Endpoints

- `GET /recent_track/<username>`  
  最も最近に聞いた1曲を返します。  
  [user.getRecentTracks](https://www.last.fm/api/show/user.getRecentTracks) API を使用しています。

- `GET /top_tracks/<username>`  
  トップトラックの配列を返します。  
  [user.getTopTracks](https://www.last.fm/api/show/user.getTopTracks) API を使用しています。

- `GET /top_artists/<username>`  
  トップアーティストの配列を返します。  
  [user.getTopArtists](https://www.last.fm/api/show/user.getTopArtists) API を使用しています。

## docker-compose

```yml
version: '3.8'

services:
  musique:
    container_name: Musique
    image: slashnephy/musique
    restart: always
    ports:
      - 5000:5000/tcp
    environment:
      LASTFM_API_KEY: xxx
```
