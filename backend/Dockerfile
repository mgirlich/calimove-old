FROM python:3.12-slim

# https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file
# ensures that the python output i.e. the stdout and stderr streams are sent straight to terminal (e.g. your container log) without being first buffered and that you can see the output of your application (e.g. django logs) in real time.
ENV PYTHONUNBUFFERED 1
# Disabling Bytecode (.pyc) Files¶
# https://python-docs.readthedocs.io/en/latest/writing/gotchas.html#disabling-bytecode-pyc-files
ENV PYTHONDONTWRITEBYTECODE 1

# Set python paths?
# ENV PATH="${PATH}:/root/.local/bin"
# ENV PYTHONPATH=.

# Expose the port 8000 in which our application runs
EXPOSE 80

# set work directory
WORKDIR  /app

# Copy requirements from host, to docker container in /app 
COPY ./requirements.txt .

# add “--no-cache-dir” as argument to avoid unnecessary creation of temp files to reduce the size of the docker image.
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /app/requirements.txt

# from https://github.com/KenMwaura1/Fast-Api-Vue/blob/main/src/Dockerfile
# # install dependencies
# RUN set -eux \
#     && apk add --no-cache --virtual .build-deps build-base \
#     libressl-dev libffi-dev gcc musl-dev python3-dev \
#     postgresql-dev \
#     && pip install --upgrade pip setuptools wheel \
#     && pip install -r /usr/src/app/requirements.txt \
#     && rm -rf /root/.cache/pip

# Copy everything from ./src directory to /app in the container
COPY ./src ./src

# Run the application in the port 8000
# If you are running your container behind a TLS Termination Proxy (load balancer) like Nginx or Traefik, add the option --proxy-headers, this will tell Uvicorn to trust the headers sent by that proxy telling it that the application is running behind HTTPS, etc.
# uvicorn src.main:app --host 0.0.0.0 --port 80 --reload

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]