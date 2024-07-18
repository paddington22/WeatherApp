FROM python:3.12-slim

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["bash", "-c"]
CMD ["./docker-entrypoint.sh"]