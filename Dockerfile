FROM dockerio.docker.bin.sbb.ch/python:3.13-alpine
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY *.py .
COPY ojp/ ojp/
COPY ojp2/ ojp2/
COPY nova/ nova/
COPY api/ api/
EXPOSE 8000
ENV LOG_LEVEL=INFO
ENV XML_LOG_ENABLED=false
ENV LOG_FILE_HANDLER_ENABLED=false
CMD ["fastapi","run","/app/server.py","--port", "8000"]
