FROM python:3.10

WORKDIR /planner

ADD requirements.txt /planner/requirements.txt

RUN pip install --upgrade pip && pip install -r /planner/requirements.txt

EXPOSE 8080

COPY ./ /planner

CMD ["python", "main.py"]
