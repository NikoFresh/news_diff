FROM python:3.9.1-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY install-packages.sh .
RUN ./install-packages.sh

COPY . .

CMD [ "python3", "-m", "main"]