FROM python:3
ENV PYTHONUNBUFFERED=1

COPY . /src/
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
ARG URl=0.0.0.0:8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver $URL"]
