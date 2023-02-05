
from django.urls import path
from .views import index,detail

urlpatterns = [
    path("",  index , name='medicines'),
    path("/<int:pk>", detail , name='detail'),
]
