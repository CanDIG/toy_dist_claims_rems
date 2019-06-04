FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "foo.py", "-p", "5000", "-h", "0.0.0.0"]
