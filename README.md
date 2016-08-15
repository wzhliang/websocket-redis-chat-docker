Simple scalable websocket chat server with:

* Python3
* autobahn with asyncio
* redis for pub/sub
* docker compose setup for load balancing 3 server

How to run

* `docker-compose build`
* `docker-compose run -d`
* enter `ui` directory and serve the directory through an http server
* point your browser at the website and start chatting
