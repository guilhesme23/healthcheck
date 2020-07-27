FROM python:3.8-alpine

WORKDIR app

RUN apt update -y && apt install gcc -y

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD . .

CMD ["python", "main.py"]