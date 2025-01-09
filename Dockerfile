#syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Step 6: Expose port 5000 for the Flask app
EXPOSE 5000

COPY . .

CMD [ "python", "app.py"]