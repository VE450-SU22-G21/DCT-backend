FROM python:3.8.12
ENV PYTHONUNBUFFERED 1

WORKDIR /dct-backend
COPY requirements.txt /dct-backend/
RUN pip install -r requirements.txt
