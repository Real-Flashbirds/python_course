from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_1', views.personal_test, name='A test not like the others'),

]