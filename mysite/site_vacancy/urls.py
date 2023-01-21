from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('page_vacancy', views.page_vacancy)
]
