#declare what image to use

FROM python:3.11-slim

RUN python -m venv /opt/venv/

ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./src /app

CMD ["python","-m","http.server","8000"]