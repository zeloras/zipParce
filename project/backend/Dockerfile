FROM python:3.7-alpine3.12
RUN apk update
RUN apk add --update --no-cache p7zip
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/

EXPOSE 8082

CMD ["python", "app.py"]
