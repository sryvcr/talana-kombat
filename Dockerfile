FROM python:3.10.13-alpine

WORKDIR /app
ADD requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
