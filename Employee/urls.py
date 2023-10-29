from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    # path("add", views.add, name='Add'),
    # path("evenodd", views.evenodd, name='EvenOdd'),
    # path("multiply", views.multiply, name='Multiply'),
    # path("gender", views.gender, name='Gender'),
    # path("high", views.high, name='High'),
    # path("age", views.age, name='age')
    # path("factorial", views.factorial, name='factorial')
    # path("fibonaci", views.fibonaci, name='fibonaci')
    path("calculator", views.fibonnaci, name='calculator')
]

