# start by pulling the python image
FROM python:3.8-alpine

RUN python -m pip install --upgrade pip
# switch working directory
WORKDIR /app

COPY . .

RUN ls -la

# # copy the requirements file into the image
# COPY flash_app/requirements.txt .

RUN ls -la

# install the dependencies and packages in the requirements file
RUN pip install -r flash_app/requirements.txt

# copy every content from the local file to the image


# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py"]
