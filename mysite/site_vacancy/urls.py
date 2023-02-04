from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('page_vacancy', views.page_vacancy),
    path('create', views.create),
    path('<int:pk>', views.VacancyDetailView.as_view()),
    path('<int:pk>/update', views.VacancyUpdateView.as_view()),
    path('<int:pk>/delete', views.VacancyDeleteView.as_view())
]
