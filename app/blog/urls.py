from . import views
from django.urls import path

urlpatterns = [
    path("v1/blog/", views.post_list_all, name="blog_list_all"), # POST/GET
    path("v1/blog/<str:slug>", views.post_list_single, name="blog_list_single"), # POST/GET
    path("v1/blog/<int:pk>", views.post_detail, name="blog_detail"), # DELETE/PUT
]