FROM python:3.8-slim

WORKDIR /usr/src/app

COPY app/ .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["python", "./main.py"]
