# blog-agent

run docker-compose file

install fastapi
pip install "fastapi[standard]"

psql -h localhost --port 5434 -U postgres

docker-compose up --build

docker build -t blog-agent .

docker run -d -p 8000:8000 --name meu-blog-agent blog-agent

docker logs meu-blog-agent

http://127.0.0.1:8000/?segment=travel

http://localhost:8000/?segment=tech&topic=python