FROM python:3.13-alpine
WORKDIR /app
RUN mkdir /app/logs
# RUN chmod 777 /app
ADD requirements.txt .
RUN pip install -r ./requirements.txt
COPY *.py .
COPY ojp/ ojp/
COPY nova/ nova/
EXPOSE 8000
ENTRYPOINT ["python","/app/server.py"]