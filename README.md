# blog-agent

run docker-compose file

install fastapi
pip install "fastapi[standard]"

docker build -t blog-agent .

docker run -d -p 8000:8000 --name meu-blog-agent blog-agent

docker logs meu-blog-agent 