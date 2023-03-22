FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 3000

CMD ["flask", "run", "--host", "0.0.0.0"]