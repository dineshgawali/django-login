from django.urls import re_path as url
from app import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]