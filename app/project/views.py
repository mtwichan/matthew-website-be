from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Project
from .serializers import *

# Create your views here.
# TODO: add error handling
@api_view(['GET', 'POST'])
def project_list_all(request):
    if request.method == "GET":
        data = Project.objects.filter(status=1)

        amount: int = request.query_params.get("amount")
        order: str = request.query_params.get("order")
        search: str = request.query_params.get("search")
        page: int = request.query_params.get("page")

        if order:
            data = data.order_by("-{order}".format(order=order))

        if search:
            data = data.filter(description__contains=search)
        
        if page:
            paginator = Paginator(data, 6)
            if paginator.num_pages < int(page):
                data = []
            else:
                data = paginator.page(page)
        elif amount:
            data = data[:int(amount)]
        serializer = ProjectSerializer(data, context={'request': request}, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        return Response({"status": "failed", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def project_list_single(request, slug):
    if request.method == "GET":
        data = Project.objects.filter(slug=slug)        
        if not data.exists():
            return Response({"status":"failed", "error": "slug does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProjectSerializer(data, context={'request': request}, many=True)                
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({"status":"failed", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ProjectSerializer(project, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"status":"failed", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        project.delete()
        return Response({"status": "success"}, status=status.HTTP_204_NO_CONTENT)