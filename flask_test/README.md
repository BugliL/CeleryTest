# Flask celery example
Example to use celery and rabbitmq configuring everything for testing and 


## Testing example
In 2 different terminals from the folder ```flask_test```
```bash
~$ celery -A main.celery -l info worker
```
```bash
~$ python main.py
```
