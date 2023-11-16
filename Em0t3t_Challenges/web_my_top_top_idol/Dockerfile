FROM python:3-alpine3.16

WORKDIR /chall1

ADD . /chall1

# Upgrade pip
RUN pip3 install --upgrade pip
RUN pip3 install requests
RUN pip3 install -r requirements.txt

CMD ["python3","main.py"]