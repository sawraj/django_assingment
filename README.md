# django_assingment
Django Assignment

The project runs on http://127.0.0.1:8000.
User will see a screen asking for a number to enter. If user enters a number, 
he will get the fibonacci number at that position in the series.

We have also calculated the time taken by API to process the request.
However there exists an another method in Django i.e Django Middleware by which we can calculate request response time for 
n number of request. For that we can use below code:- 


import time
class StatsMiddleware(object):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        duration = time.time() - request.start_time
        response["X-Page-Generation-Duration-ms"] = int(duration * 1000)
        return response

and in the settings.py we can add the above class

MIDDLEWARE_CLASSES = (
    'project.stats_middleware.StatsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
)

To run the project. Create a virtual environment.
After activating the virtual env, just run below commands
 
  =====> pip install -r requirements.txt
  =====> python manage.py runserver
