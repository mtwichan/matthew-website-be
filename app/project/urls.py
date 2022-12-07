from . import views
from django.urls import path

urlpatterns = [
    path("v1/project/", views.project_list_all, name="project_list_all"), # POST/GET
    path("v1/project/<str:slug>", views.project_list_single, name="project_list_single"), # POST/GET
    path("v1/project/<int:pk>", views.project_detail, name="project_detail"), # DELETE/PUT
]