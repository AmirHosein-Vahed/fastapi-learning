FROM python:3.13-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# COPY ./app /code/app
COPY ./main.py /code/

# CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "80", "--workers", "4"]
CMD ["fastapi", "run", "main.py", "--port", "80"]


# .
# ├── main.py
# ├── Dockerfile
# └── requirements.txt