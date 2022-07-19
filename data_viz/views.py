from django.http import HttpResponse
from django.shortcuts import redirect, render
from json import dumps
# Create your views here.
import mysql.connector

companyName = ''
username = ''
password = ''


def login_page(request):
    if request.method == "POST":
        companyName = request.POST.get("company_name")
        username = request.POST.get("user_name")
        password = request.POST.get("password")
        # if (username == "anurag" and password == "atto" and companyName == "help"):
        #     # data_fetch(request)
        #     return redirect('data_fetch/')
        # #print(companyName, username, password)
    return render(request, 'login.html')


def data_fetch(request):
    print("print", companyName, username, password)
    conn = mysql.connector.connect(user='ashish', password='ashish@123',
                                   host='Desktop-G3', database='sql_store', buffered=True)
    cursor = conn.cursor()

    cursor.execute('select customer_id FROM customers')
    my_result = cursor.fetchall()
    # print(type((my_result)))
    a = []
    for x in my_result:
        a.append(x)
        # print(a)

    out = [item for t in a for item in t]
    print(out)
    dataJSON = dumps(out)
    return render(request, 'index.html', context={'data': dataJSON})


def say_hello(request):
    return render(request, 'hello.html', context={
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    },)
    # return HttpResponse('hello')
