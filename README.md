# Musique

๐ง Last.fm ็ต็ฑใงๆ่ฟๅ็ใใใใฉใใฏๆๅ ฑใชใฉใ่ฟใใ ใใฎ API ใตใผใ

## Endpoints

- `GET /recent_track/<username>`  
  ๆใๆ่ฟใซ่ใใ1ๆฒใ่ฟใใพใใ  
  [user.getRecentTracks](https://www.last.fm/api/show/user.getRecentTracks) API ใไฝฟ็จใใฆใใพใใ

- `GET /top_tracks/<username>`  
  ใใใใใฉใใฏใฎ้ๅใ่ฟใใพใใ  
  [user.getTopTracks](https://www.last.fm/api/show/user.getTopTracks) API ใไฝฟ็จใใฆใใพใใ

- `GET /top_artists/<username>`  
  ใใใใขใผใใฃในใใฎ้ๅใ่ฟใใพใใ  
  [user.getTopArtists](https://www.last.fm/api/show/user.getTopArtists) API ใไฝฟ็จใใฆใใพใใ

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
