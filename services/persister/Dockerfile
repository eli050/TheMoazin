FROM python:3.13

WORKDIR /app

VOLUME ["/app/data"]


COPY ./services/persister/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./libs /app/libs

COPY ./services/persister /app/services/persister

COPY ./log /app/log

CMD ["python", "-m", "services.persister.main"]