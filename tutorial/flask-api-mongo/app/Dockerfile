FROM python:3.9.5

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
COPY .env ./
COPY database* database/
COPY resources* resources/
COPY services* services/
COPY templates* templates/ 
ENV ENV_FILE_LOCATION=./.env

CMD [ "python", "./app.py" ]
