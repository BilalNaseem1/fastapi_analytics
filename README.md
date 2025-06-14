```python
pip install pip --upgrade

uvicorn main:app --reload

hub.docker.com -> python images


# docker
docker build -t analytics-api -f Dockerfile .
docker run analytics-api:latest

# we cant run this - so we write compose for services we need
# so docker commands become
docker compose up --watch
docker compose down
#or
docker compose down -v

# to get into command line of image
- docker compose run app /bin/bash
# or
- docker compose run app python
```