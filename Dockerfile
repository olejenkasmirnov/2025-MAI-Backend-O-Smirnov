FROM python:3.10.12
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "myproject/manage.py", "runserver", "0.0.0.0:8000"]