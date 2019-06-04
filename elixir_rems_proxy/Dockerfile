FROM python:3.7-slim-stretch

RUN apt-get update -y \
    && apt-get install -y git-core

WORKDIR /code

RUN git clone https://github.com/CSCfi/elixir-rems-proxy/ \
    && cd elixir-rems-proxy \
    && pip install -r requirements.txt \
    && pip install .

EXPOSE 8080

ENTRYPOINT ["elixir_api"]
