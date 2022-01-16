# Fastapi with docker

## Steps
- Set environment variable
    - DB_USER
    - DB_PASSWORD
    - DB_HOST
    - DB_NAME
- Build image
- `docker build -t myimage .`
- Run container
- `docker run -e DB_USER -e DB_PASSWORD -e DB_HOST -e DB_NAME -d --name mycontainer -p 8000:80 myimage`
- Run container with network access
- `docker run --network=bridge -e DB_USER -e DB_PASSWORD -e DB_HOST -e DB_NAME -d --name mycontainer -p 8000:80 myimage`
