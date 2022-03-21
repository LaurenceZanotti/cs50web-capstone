FROM python:3
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]