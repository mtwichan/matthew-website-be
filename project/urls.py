from . import views
from django.urls import path

urlpatterns = [
    path("api/project/", views.project_list_all, name="project_list_all"), # POST/GET
    path("api/project/<str:slug>", views.project_list_single, name="project_list_single"), # POST/GET
    path("api/project/<int:pk>", views.project_detail, name="project_detail"), # DELETE/PUT
]