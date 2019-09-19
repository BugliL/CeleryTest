from flask import Flask
from celery_config import make_celery
from celery.schedules import crontab

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost/'
app.config['CELERYBEAT_SCHEDULE'] = {
    'test-celery': {
        'task': 'scheduled_task',
        'schedule': crontab(minute="*"),
    }
}

celery = make_celery(app)


@app.route("/")
def hello():
    example_task.delay()
    return "Hello World!"


@celery.task(name='celery_example_task')
def example_task():
    return "This is an example task"


@celery.task(name='celery_example_scheduled_task')
def scheduled_task():
    return "This is an example task of scheduled task"


if __name__ == "__main__":
    app.run(debug=True)
