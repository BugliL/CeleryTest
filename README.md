# Celery + RabbitMQ

Repository to try a basic configuration for test and production of rabbitmq and celery.

## Requirements
```bash
sudo apt-get install rabbitmq-server supervisor
```


## Documentations - [Source](https://www.linode.com/docs/development/python/task-queue-celery-rabbitmq/#write-a-celery-application)
A Celery application is composed of three parts:
 - **Workers** that wait for messages from RabbitMQ and execute the tasks.
 - **Client** that submit messages to RabbitMQ to trigger task execution, and eventually retrieve the result at a later time
 - **Message broker**. The client communicates with the the workers through a message queue, and Celery supports several ways to implement these queues. The most commonly used brokers are RabbitMQ and Redis.


The tasks are defined in a module that will be used both by the workers and the client. Workers will run the code to execute tasks, and clients will only use function definitions to expose them and hide the RabbitMQ publishing complexity.

Sample code 
```python
# This line of code create a celery application
app = Celery('application_name', backend='rpc://', broker='pyamqp://guest@localhost//')


@app.task
def async_function():
    # Do async stuff
```
Where:
 - A Celery application named *application_name*
 - A broker on the localhost that will accept message via Advanced Message Queuing Protocol (AMQP), the protocol used by RabbitMQ
 - A response backend where workers will store the return value of the task so that clients can retrieve it later (remember that task execution is asynchronous). If you omit backend, the task will still run, but the return value will be lost. rpc means the response will be sent to a RabbitMQ queue in a Remote Procedure Call pattern.
 - @app.task tells celery that this function will not be run on the client, but sent to the workers via RabbitMQ
 
To execute the function asynchronously it's possible to call the **delay** function

```python
>>> async_function()  # Synchronous call, it waits the end
>>> async_function.delay()  # Asynchronous call, execution continues
```

## Settings
Setting user, virtual host and permissions
```bash
sudo rabbitmqctl add_user myuser mypassword
sudo rabbitmqctl add_vhost myvhost
sudo rabbitmqctl set_user_tags myuser mytag
sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
```

Celery configuration for rabbitmq
```python
BROKER_URL = 'amqp://myuser:mypassword@localhost:5672/myvhost'
```

