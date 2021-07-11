FROM python:alpine

RUN apk add --update --no-cache tzdata
ENV TZ=Asia/Tokyo

RUN pip install --no-cache-dir flask flask_cors

COPY ./app.py /

WORKDIR /
EXPOSE 5000
ENV FLASK_APP=app.py
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
