from . import views
from django.urls import include, path, re_path

urlpatterns = [
    path("api/blog/", views.post_list_all, name="blog_list_all"), # POST/GET
    path("api/blog/<str:slug>", views.post_list_single, name="blog_list_single"), # POST/GET
    path("api/blog/<int:pk>", views.post_detail, name="blog_detail"), # DELETE/PUT
]