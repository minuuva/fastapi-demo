FROM python:3.11-alpine3.20

# Set working directory
WORKDIR /code

# Copy requirements and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN apk add --no-cache musl-dev mariadb-connector-c-dev gcc
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code
COPY . /code

# Expose the port
EXPOSE 80

# Run the FastAPI app with Uvicorn (change the command here as well)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]

