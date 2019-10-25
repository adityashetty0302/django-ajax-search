from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name="home"),
    path('ajax/check-username', views.check_username, name="check_username")
]
