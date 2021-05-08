# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Person
from .serializers import PersonSerializer


class PersonApi(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

