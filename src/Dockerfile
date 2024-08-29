FROM python:3.12-slim
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
COPY ./index.html /code/static/index.html
CMD ["python3", "app/main.py"]
EXPOSE 80
EXPOSE 8000

