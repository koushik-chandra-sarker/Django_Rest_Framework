# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Person
from .serializers import PersonSerializer
from django.views.decorators.csrf import csrf_exempt


class PersonApi(APIView):
    def get(self, request, id=None, format=None):
        if id is not None:  # Get Single Person
            person = Person.objects.get(id=id)  # Get  Person
            serializer = PersonSerializer(person)  # serializer the python data
            return Response(serializer.data)  # return json data

        else:  # Get All Person
            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many=True)
            return Response(serializer.data)  # return json data

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Data Inserted."}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None, format=None):
        if id is not None:
            try:
                person = Person.objects.get(id=id)
            except Person.DoesNotExist:
                return Response({"message":"Not Found"}, status=status.HTTP_404_NOT_FOUND)

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

    def delele(self, request, id=None, format=None):
        if id is not None:
            person = Person.objects.get(id=id)
            person.delete()
            response = {"message": "Data Deleted."}
            return Response(response)
        else:
            return Response({"message": "Url Incorrect"})
