FROM python:alpine

EXPOSE 8080

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["gunicorn"]
CMD ["-w" ,"1" ,"--log-level=debug","--timeout" ,"1000" ,"--bind","0.0.0.0:8080","wsgi:app"]