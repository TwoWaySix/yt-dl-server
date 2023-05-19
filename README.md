```
docker build --tag yt-dl-server:latest .
docker tag yt-dl-server:latest 192.168.178.104:5000/yt-dl-server:latest
docker push 192.168.178.104:5000/yt-dl-server:latest
```