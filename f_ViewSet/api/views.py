# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Person
from .serializers import PersonSerializer


class PersonApi(ViewSet):
    # get all
    def list(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)  # return json data

    # Create One
    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Data Inserted."}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # get One
    def retrieve(self, request, pk=None):
        if pk is not None:  # Get Single Person
            person = Person.objects.get(id=pk)  # Get  Person
            serializer = PersonSerializer(person)  # serializer the python data
            return Response(serializer.data)  # return json data

    # update one
    def update(self, request, pk=None):
        if pk is not None:
            try:
                person = Person.objects.get(id=pk)
            except Person.DoesNotExist:
                return Response({"message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

            # partial True means you can update data partially means all fields are not required
            serializer = PersonSerializer(person, data=request.data)  # (existed_data, updated_data, partial)
            if serializer.is_valid():
                serializer.save()
                response = {"message": "Data Updated."}
                return Response(response)
            else:
                return Response(serializer.errors)
        else:
            return Response({"message": "Url Incorrect"})

    # update one partially
    def partial_update(self, request, pk=None):
        if pk is not None:
            try:
                person = Person.objects.get(id=pk)
            except Person.DoesNotExist:
                return Response({"message": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

            # partial True means you can update data partially means all fields are not required
            serializer = PersonSerializer(person, data=request.data,
                                          partial=True)  # (existed_data, updated_data, partial)
            if serializer.is_valid():
                serializer.save()
                response = {"message": "Data Updated."}
                return Response(response)
            else:
                return Response(serializer.errors)
        else:
            return Response({"message": "Url Incorrect"})

    # Delete one
    def destroy(self, request, pk=None):
        if pk is not None:
            person = Person.objects.get(id=pk)
            person.delete()
            response = {"message": "Data Deleted."}
            return Response(response)
        else:
            return Response({"message": "Url Incorrect"})
