FROM python:3.8 -slim
EXPOSE 30001
WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py .
CMD ["python", "./app.py"]