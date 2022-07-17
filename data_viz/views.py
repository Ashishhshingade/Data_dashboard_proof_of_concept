from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import mysql.connector

def data_fetch(request):
     conn = mysql.connector.connect(user='ashish', password='ashish@123',
                               host='Desktop-G3', database='sql_store', buffered=True)
     cursor = conn.cursor()

     cursor.execute('select * FROM customers')
     my_result = cursor.fetchall()
     for x in my_result:
          print(x)
     return HttpResponse('hello')


def say_hello(request):
     # return render(request,'hello.html')
     return HttpResponse('hello')