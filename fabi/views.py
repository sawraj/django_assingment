from django.http import HttpResponse
import time
from django.shortcuts import render


def hello(request):
    return render(request, 'home.html')


def fibo(request):
    start_time = time.time()
    n = int(request.GET['original'])
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    end_time = time.time()
    time_taken = int(end_time - start_time) * 1000000
    print(end_time)
    print(start_time)
    return render(
        request,
        'end.html',
        {'n': n, 'a': a, 'time_taken': time_taken},
    )