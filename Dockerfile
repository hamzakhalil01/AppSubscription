FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt
COPY . /app/

EXPOSE 8000

# Specify the command to run on container start
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app_subscription.wsgi:application"]
