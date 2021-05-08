# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView

from .models import Person
from .serializers import PersonSerializer


# All Operation done by automatically

class ListPersonApi(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CreatePersonApi(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class RetrievePersonApi(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class UpdatePersonApi(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DeletePersonApi(DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# You can perform 2 operation in one class
class ListCreatePersonApi(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class RetrieveUpdatePersonApi(RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class RetrieveDeletePersonApi(RetrieveDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class RetrieveUpdateDeletePersonApi(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
