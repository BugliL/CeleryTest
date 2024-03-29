from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend='rpc://',
        broker=app.config['CELERY_BROKER_URL'],
        timezone='Europe/London',
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    # Mokey patching with added behavior
    celery.Task = ContextTask
    return celery
