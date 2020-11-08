FROM python:3.9

#set environment variables

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Set work directory

WORKDIR /book_store_dir

# install dependencies

COPY requirements.txt /book_store_dir/

RUN pip install -r /book_store_dir/requirements.txt

# copy project

COPY Dockerfile /book_store_dir/
COPY Book_store /book_store_dir/