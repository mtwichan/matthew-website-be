from django.views import generic

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Post
from .serializers import *

# Create your views here.
@api_view(['GET', 'POST'])
def post_list_all(request):
    if request.method == "GET":
        try:
            data = Post.objects.all()
            
            amount: int = request.query_params.get("amount")
            order: str = request.query_params.get("order")
            
            if order:
                data = data.order_by("-{order}".format(order=order))
            
            if amount:
                data = data[:int(amount)]

            serializer = PostSerializer(data, context={'request': request}, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            # TODO: add more error print statements to log errors in the console
            print("Error: ", error)
            return Response({"status":"failed", "error": str(error)}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        return Response({"status": "failed", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def post_list_single(request, slug):
    if request.method == "GET":
        data = Post.objects.filter(slug=slug)        
        if not data.exists():
            return Response({"status":"failed", "error": "slug does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PostSerializer(data, context={'request': request}, many=True)                
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response({"status":"failed", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = PostSerializer(post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"status":"failed", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        post.delete()
        return Response({"status": "success"}, status=status.HTTP_204_NO_CONTENT)