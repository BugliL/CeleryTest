from flask import Flask
from .celery_config import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqb://localhost/'

celery = make_celery(app)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
