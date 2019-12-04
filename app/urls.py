from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.Indexpage,name="indexpage"),
   path("registeruser/",views.registeruser,name="register"),
   path("alldetail/",views.alldetail,name="alldetail1"),
   path("sucess/",views.sucess,name="sucess"),
]

