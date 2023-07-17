FROM python:3.11.3

RUN mkdir /insurance_calculator_app

WORKDIR /insurance_calculator_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR src

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:800