# Chapter 4: Communication

## Lab Sessions: AMQP with RabbitMQ and Python

This document provides an overview of the steps and setup required to build a simple "Hello World" and chat application using AMQP, RabbitMQ, and Python. It also includes Docker setup and configurations for seamless deployment and execution.

---

## **Getting Started**

### **Prerequisites**

Before we begin, ensure you have the following:
- **Python 2.6 or higher**
- **pip, pip3 or conda**  
- **Pika 0.9.6 or higher**
- **Docker** and **Docker Compose**

---

## **Step 1: Setting Up Your Environment**

1. Install `pip`:
   - macOS: `brew install pip`
   - Ubuntu: `sudo apt-get install python3-pip`
2. Install `Pika` using `pip install pika`.
3. Install Docker and Docker Compose:
   - Follow the [Docker Installation Guide](https://docs.docker.com/get-docker/).
   - Follow the [Docker Compose Installation Guide](https://docs.docker.com/compose/install/).

---

## **Step 2: Configuring RabbitMQ**

1. Start the RabbitMQ server:
   - Use the command: `sudo systemctl start rabbitmq-server`.
2. Access the RabbitMQ web management interface at [http://localhost:15672](http://localhost:15672).
3. Create and manage queues, exchanges, and bindings as needed.

---

## **Step 3: Publisher and Consumer Setup**

1. **Publisher**:
   - Configure the script to connect to RabbitMQ, send a message, and close the connection.
   - Ensure the RabbitMQ host and queue name are correctly specified.

2. **Consumer**:
   - Configure the script to connect to RabbitMQ, listen to the specified queue, and process incoming messages.
   - Ensure the same queue name is used as in the publisher.

---

## **Step 4: Docker Integration**

1. **Create a `Dockerfile`**:
   - Set up the environment for running Python scripts for the producer and consumer.
   - Include necessary dependencies and default commands.

2. **Create `docker-compose.yml`**:
   - Define services for RabbitMQ, publisher, and consumer.
   - Configure network settings and environment variables for RabbitMQ.

3. **Build and Start Services**:
   - Build images and start services using `docker-compose up --build`.

---

## **Step 5: Running the Application**

1. Ensure RabbitMQ is running and accessible.
2. Use `docker-compose` to start the producer and consumer services.
3. Monitor the interaction between the publisher and consumer through logs or RabbitMQ's web interface.

---

## **References**

- [RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)
- [Pika Library](https://pika.readthedocs.io/en/stable/)
- [Docker Documentation](https://docs.docker.com/)
