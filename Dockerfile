FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 8888

CMD ["uvicorn", "main:app","--host","0.0.0.0", "--port", "8888"]
