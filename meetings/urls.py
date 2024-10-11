from django.urls import path
from . import views


urlpatterns=[
    path('', views.meetings_list_view, name='meetings'),  # List of meetings
]