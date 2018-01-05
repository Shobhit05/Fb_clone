FROM ubuntu
#FROM python:2-onbuild

RUN apt-get update

# COPY startup script into known file location in container
COPY . /app

WORKDIR /app/django2/clone/

RUN apt-get install -y python-pip

RUN pip install -r requirements.txt

# EXPOSE port 8000 to allow communication to/from server

EXPOSE 8000

# CMD specifcies the command to execute to start the server running.

RUN ls
CMD ["/app/django2/clone/start.sh"]
# done!

