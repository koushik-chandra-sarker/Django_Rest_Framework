# Create your views here.
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Function based View
@csrf_exempt  # it's for POST REQUEST
def person_api(request, id=None):
    if request.method == "GET":
        if id is not None:  # Get Single Person
            person = Person.objects.get(id=id)  # Get  Person
            serializer = PersonSerializer(person)  # serializer the python data
            # json_data = JSONRenderer().render(serializer.data)  # Convert Serialized data into json data
            # return HttpResponse(json_data, content_type='application/json')  # return json data
            # or
            return JsonResponse(serializer.data, safe=False)  # return json data

        else:  # Get All Person
            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    if request.method == "POST":
        json_data = request.body  # get Json data from request body
        stream = io.BytesIO(json_data)  # Convert Json data into stream
        python_data = JSONParser().parse(stream)  # Convert Json data into python data
        serializer = PersonSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Data Inserted."}
            return HttpResponse(JSONRenderer().render(response), content_type="application/json")
        else:
            response = JSONRenderer().render(serializer.errors)
            return HttpResponse(response, content_type="application/json")

    if request.method == "PUT":
        json_data = request.body  # get Json data from request body
        stream = io.BytesIO(json_data)  # Convert Json data into stream
        python_data = JSONParser().parse(stream)  # Convert Json data into python data
        id = python_data.get("id")
        person = Person.objects.get(id=id)
        # partial True means you can update data partially means all fields are not required
        serializer = PersonSerializer(person, data=python_data, partial=True)  # (existed_data, updated_data, partial)

        if serializer.is_valid():
            serializer.save()
            response = {"message": "Data Updated."}
            return JsonResponse(response, safe=False)
        else:
            response = JSONRenderer().render(serializer.errors)
            return JsonResponse(response, safe=False)

    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        person = Person.objects.get(id=id)
        person.delete()
        response = {"message": "Data Deleted."}
        return JsonResponse(response, safe=False)


# Class based View
'''
@method_decorator(csrf_exempt, name='dispatch')
class PersonApi(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body  # get Json data from request body
        stream = io.BytesIO(json_data)  # Convert Json data into stream
        python_data = JSONParser().parse(stream)  # Convert Json data into python data
        id = python_data.get('id', None)  # if it's don't have id then id = None
        if id is not None:  # Get Single Person
            person = Person.objects.get(id=id)  # Get  Person
            serializer = PersonSerializer(person)  # serializer the python data
            # json_data = JSONRenderer().render(serializer.data)  # Convert Serialized data into json data
            # return HttpResponse(json_data, content_type='application/json')  # return json data
            # or
            return JsonResponse(serializer.data, safe=False)  # return json data

        else:  # Get All Person
            persons = Person.objects.all()
            serializer = PersonSerializer(persons, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body  # get Json data from request body
        stream = io.BytesIO(json_data)  # Convert Json data into stream
        python_data = JSONParser().parse(stream)  # Convert Json data into python data
        serializer = PersonSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "Data Inserted."}
            return HttpResponse(JSONRenderer().render(response), content_type="application/json")
        else:
            response = JSONRenderer().render(serializer.errors)
            return HttpResponse(response, content_type="application/json")

    def put(self, request, *args, **kwargs):
        json_data = request.body  # get Json data from request body
        stream = io.BytesIO(json_data)  # Convert Json data into stream
        python_data = JSONParser().parse(stream)  # Convert Json data into python data
        id = python_data.get("id")
        person = Person.objects.get(id=id)
        # partial True means you can update data partially means all fields are not required
        serializer = PersonSerializer(person, data=python_data, partial=True)  # (existed_data, updated_data, partial)

        if serializer.is_valid():
            serializer.save()
            response = {"message": "Data Updated."}
            return JsonResponse(response, safe=False)
        else:
            response = JSONRenderer().render(serializer.errors)
            return JsonResponse(response, safe=False)

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        person = Person.objects.get(id=id)
        person.delete()
        response = {"message": "Data Deleted."}
        return JsonResponse(response, safe=False)'''
