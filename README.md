# chapter4-communication

# Lab Sessions: AMQP with RabbitMQ and Python

This document provides an overview of the steps and setup required to build a simple "Hello World" application using AMQP, RabbitMQ, and Python.

---

## **Getting Started**

### **Prerequisites**

Before we begin, ensure you have the following:
- **Python 2.6 or higher**
- **easy_install**  
- **Pika 0.9.6 or higher**

---

## **Step 1: Setting Up Your Environment**

1. Install `easy_install`.  
2. Install `Pika` using `easy_install` or `pip`.

---

## **Step 2: Creating the Publisher**

The publisher performs the following tasks:
- Connects to RabbitMQ.
- Obtains a channel.
- Declares an exchange.
- Creates a message.
- Publishes the message.
- Closes the channel.
- Closes the connection.

---

## **Step 3: Creating the Consumer**

The consumer performs the following tasks:
- Connects to RabbitMQ.
- Obtains a channel.
- Declares an exchange.
- Declares a queue.
- Binds the queue with the exchange.
- Consumes the messages.
- Closes the channel.
- Closes the connection.

---

## **Step 4: Managing RabbitMQ Server**

Use the following commands to manage RabbitMQ:
- Check RabbitMQ processes:  
  `ps aux | grep rabbitmq`  
- Stop RabbitMQ:  
  `sudo systemctl stop rabbitmq-server`  
- Start RabbitMQ:  
  `sudo systemctl start rabbitmq-server`  
- Check RabbitMQ status:  
  `sudo systemctl status rabbitmq-server`  

Access the RabbitMQ web management interface at:  
[http://localhost:15672](http://localhost:15672)

---

## **Step 5: Running the Application**

1. Start the RabbitMQ server if it’s not already running.
2. Run the publisher script.
3. Run the consumer script.

---

## **References**

- [RabbitMQ Documentation](https://www.rabbitmq.com/documentation.html)
- [Pika Library](https://pika.readthedocs.io/en/stable/)

---
