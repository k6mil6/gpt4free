FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8888

CMD ["uvicorn", "main:app", "--port", "8888"]
