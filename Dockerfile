FROM dockerio.docker.bin.sbb.ch/python:3.13-alpine
VOLUME ["/app/generated"]
VOLUME ["/app/logs"]
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY *.py .
COPY ojp/ ojp/
COPY nova/ nova/
EXPOSE 80
CMD ["fastapi","run","/app/server.py","--port", "80"]