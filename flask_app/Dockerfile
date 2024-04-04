# start by pulling the python image
FROM python:3.8-alpine

RUN python -m pip install --upgrade pip

WORKDIR /app/flask_app

COPY . .

RUN ls -la
RUN cd flask_app
RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["app.py" ]