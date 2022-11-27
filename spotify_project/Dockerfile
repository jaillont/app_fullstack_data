# syntax=docker/dockerfile:1
FROM python:3.9.6
FROM tensorflow/tensorflow:2.10.0-gpu

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN apt update && \
    apt install -y git && \
    pip install --no-cache-dir Pillow==9.2.0 tqdm==4.64.1 \
    ftfy==6.1.1 regex==2022.9.13 tensorflow-addons==0.17.1 \
    fastapi "uvicorn[standard]" git+https://github.com/divamgupta/stable-diffusion-tensorflow.git

RUN pip install -r requirements.txt

COPY . /code/
