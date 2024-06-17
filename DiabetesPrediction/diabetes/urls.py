from django.urls import path, re_path
from diabetes import views

app_name =  'diabetes'

urlpatterns = [  
    path("", views.home, name="home"),
    path("predict/", views.predict, name="predict"),
     path("predict/result/", views.result, name="result")
]