from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Contact
from .serializers import *

# Create your views here.
@api_view(['POST'])
def email_send(request):
    serializer = ContactSerializer(data=request.data)
    try:
        if serializer.is_valid():
            name = serializer.data.get("name", "Empty name")
            email = serializer.data.get("email", "Empty email")
            affiliation = serializer.data.get("affiliation", "Empty affiliation")
            subject = f"{affiliation} - {name} - {email}"
            message = serializer.data.get("message", "Empty message")
            host_email = settings.EMAIL_HOST_USER
            recipient_list = [settings.EMAIL_RECIPIENT]

            send_mail(subject, message, host_email, recipient_list, fail_silently=False)
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "failed", "error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return Response({"status": "failed", "error": str(error)}, status=status.HTTP_400_BAD_REQUEST)