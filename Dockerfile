# Use the official Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the required dependencies
RUN pip install pika

# Specify the default command to run the producer or consumer
CMD ["python", "consumer.py", "user1"]  # Default to consumer, change as needed
