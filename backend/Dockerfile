#declare what image to use

FROM python:3.11-slim

#curl -X post -d '{"message":"hello world"}' -H Content-Type:application.json http:host.docker.internal:8080/api/chats/
RUN apt-get update && apt-get install -y curl

RUN python -m venv /opt/venv/

ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

#CMD ["docker","model","pull","ai/smollm2:135M-Q2-K"]

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./src /app

CMD ["python","-m","http.server","8000"]