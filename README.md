# Musique

Last.fm 経由で最近再生したトラック情報を返すだけの API サーバ

Last.fm の [user.getRecentTracks](https://www.last.fm/api/show/user.getRecentTracks) API を使用しています。



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
