FROM ubuntu:22.04

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt update && apt upgrade -y
RUN apt -y install git python3 python3-pip
RUN pip install --upgrade pip wheel
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

