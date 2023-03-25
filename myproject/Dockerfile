FROM python:3.8-slim-buster

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

CMD ["python3","manage.py","runserver" ,"0.0.0.0:8000"]
