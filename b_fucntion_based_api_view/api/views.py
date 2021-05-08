# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Person
from .serializers import PersonSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt  # it's for POST REQUEST
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def person_api(request, id=None):
    if request.method == "GET":
        if id is not None:  # Get Single Person
            person = Person.objects.get(id=id)  # Get  Person
            serializer = PersonSerializer(person)  # serializer the python data
            return Response(serializer.data)  # return json data

        else:  # Get All Person
            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many=True)
            return Response(serializer.data)  # return json data

    if request.method == "POST":

        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Data Inserted."}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PUT":
        if id is not None:
            person = Person.objects.get(id=id)
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
    if request.method == "DELETE":
        if id is not None:
            person = Person.objects.get(id=id)
            person.delete()
            response = {"message": "Data Deleted."}
            return Response(response)
        else:
            return Response({"message": "Url Incorrect"})
