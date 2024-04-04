# start by pulling the python image
FROM python:3.8-alpine

RUN python -m pip install --upgrade pip
# switch working directory
WORKDIR /app

# copy the requirements file into the image
COPY requirements.txt .

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . .

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py"]
