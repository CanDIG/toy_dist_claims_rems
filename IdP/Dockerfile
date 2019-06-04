FROM python:3.6-alpine
RUN apk add build-base \
    && apk add libffi-dev \
    && apk add openssl-dev
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 443
CMD ["python3", "src/run.py", "settings.yaml", "-p", "443", "-b", "https://idp"]
