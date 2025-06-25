FROM python:3.8
EXPOSE 30001
WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py .
CMD ["python", "./app.py"]