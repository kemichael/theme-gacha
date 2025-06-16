FROM python:3.11-slim

WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /app
WORKDIR /app
RUN chmod +x /app/wait-for-it.sh
CMD ["./wait-for-it.sh", "db:3306", "--", "flask", "run", "--host=0.0.0.0", "--port=8000"]