# Flask celery example
Example to use celery and rabbitmq configuring everything for testing and 


## Settings
Copy configuration to let *supervisor* access it
```bash
~$ cp supervisor.conf /etc/supervisor/conf.d/celery_flask_test.conf
```

Update supervisor
```bash
~$ sudo supervisorctl reread
~$ sudo supervisorctl update
~$ sudo supervisorctl restart celery_test_flask
```
Log should appear in *logs* folder 

## Testing example
In 2 different terminals from the folder ```flask_test```
```bash
(venv) $ celery -A main.celery -l info worker
```
```bash
(venv) $ python main.py 
```
to make calls, it's possible to use curl for example, on another terminal
```
~$ curl -i http://localhost:5000
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 12
Server: Werkzeug/0.14.1 Python/3.7.1
Date: Thu, 19 Sep 2019 15:24:56 GMT

Hello World!%                                                                       
```
