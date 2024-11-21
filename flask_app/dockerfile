# start by pulling the python image
FROM python:3.8-alpine

RUN python -m pip install --upgrade pip

# switch working directory
WORKDIR /app

# copy everything from the local directory to the image
COPY . .

# list files in the current directory
RUN ls -la

# install the dependencies and packages in the requirements file
RUN pip install -r /app/flask_app/requirements.txt

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]
CMD ["app.py"]
