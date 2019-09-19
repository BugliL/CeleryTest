from flask import Flask
from celery_config import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost/'

celery = make_celery(app)


@app.route("/")
def hello():
    example_task.delay()
    return "Hello World!"


@celery.task(name='celery_example_task')
def example_task():
    return "This is an example task"


if __name__ == "__main__":
    app.run(debug=True)
