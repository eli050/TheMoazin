FROM python:3.13

WORKDIR /app

VOLUME ["/app/data"]


COPY ./services/wavinfo/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./libs/kafka_obj /app/libs/kafka_obj

COPY ./services/wavinfo /app/services/wavinfo

COPY ./log /app/log

CMD ["python", "-m", "services.wavinfo.main"]




