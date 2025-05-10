FROM python:3.8-slim-buster
WORKDIR /service
COPY requirements.txt .
RUN pip install -r requirments.txt
COPY . ./
ENTRYPOINT [ "python3", "app.py" ]
