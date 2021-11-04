from django.urls import path
from .views import registrationView

app_name = "coffee"
urlpatterns = [
    path('register', registrationView),
]
