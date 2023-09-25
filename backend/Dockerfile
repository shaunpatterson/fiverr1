FROM python:3.11

WORKDIR /app/

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./app ./app
ENV PYTHONPATH="$PYTHONPATH:/app"

CMD ["uvicorn", "app.test.main:app", "--host", "0.0.0.0", "--port", "8080"]
