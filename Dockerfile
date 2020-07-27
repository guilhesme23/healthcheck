FROM python:3.8-alpine

WORKDIR app

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD . .

CMD ["python", "main.py"]