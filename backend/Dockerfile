FROM python:3.9.5-slim-buster
WORKDIR /usr/src

COPY requirements.txt /usr/src
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app", "--reload", "--reload-engine", "poll"]