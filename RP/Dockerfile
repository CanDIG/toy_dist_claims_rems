FROM python:3.6-alpine
RUN apk add build-base \
    && apk add libffi-dev \
    && apk add openssl-dev
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3", "src/rp.py", "settings.yaml", "-p", "8000", "-b", "https://rp"]
