FROM python:3.10-slim 

WORKDIR /Second 

COPY . .

RUN apt-get update
RUN apt-get install vim
RUN pip install fastapi uvicorn 
RUN pip install python-multipart

EXPOSE 800

CMD ["python","api.py"]
