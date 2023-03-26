

# RUN

## run on docker

```
cd ./myproject/docker/docker-compose.yml
docker-compose build 
docker-compose up -d

```
now porject is up on localhost:8081

## run on server
1- go to project
```
cd myproject
```

2- setUP venv
```
virtualenv venv
source venv/bin/activate
```
3- install dependencies

```
pip install -r requirements.txt
```
4- run project
```
python3 ./manage.py runserver
```

now porject is up on localhost:8000



# source 
https://gitlab.com/mtarif/django-course-source 
