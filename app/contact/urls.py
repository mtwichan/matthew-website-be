from . import views
from django.urls import path

urlpatterns = [
    path("v1/contact/", views.email_send, name="email_send"), # POST
]