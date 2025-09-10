FROM python:3.13

WORKDIR /app


COPY ./services/wavinfo/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./libs/elasticsearch /app/libs/elasticsearch

COPY ./services/processor /app/services/processor

COPY ./log /app/log

CMD ["python", "-m", "services.wavinfo.main"]