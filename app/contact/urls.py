from . import views
from django.urls import path

urlpatterns = [
    path("api/contact/", views.email_send, name="email_send"), # POST
]