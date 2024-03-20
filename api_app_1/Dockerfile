FROM python:3.10.1-slim-buster

LABEL maintainer="Lenka Kargerova <kargerova@gmail.com>"

WORKDIR /app

COPY ./requirements.txt ./requirements.txt


RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app .

CMD ["uvicorn", "main:app", "--proxy-headers", "--forwarded-allow-ips", "*", "--host", "0.0.0.0", "--port", "8080"]
