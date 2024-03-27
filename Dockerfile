FROM python:3.8-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir aiohttp g4f

EXPOSE 8888

CMD ["python", "./main.py"]
