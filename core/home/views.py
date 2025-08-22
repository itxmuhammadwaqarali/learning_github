from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import PeopleSerializer

@api_view(['GET', 'POST', 'PUT',])
def index(request):
    courses = [
        {'id': 1, 'name': 'Python Basics', 'description': 'Learn the fundamentals of Python programming.'},
        {'id': 2, 'name': 'Django Web Framework', 'description': 'Build web applications using Django.'},
        {'id': 3, 'name': 'Data Science with Python', 'description': 'Explore data analysis and visualization techniques.'},
    ]
    if request.method == 'GET':
        print("*********")
        print(request.GET.get('search'))
        print("*********")
        print("GET request received")
    elif request.method == 'POST': 
        data = request.data
        print("POST request received with data:", data) 
        print("POST request received")
    elif request.method == 'PUT':
        print("PUT request received")
    # For simplicity, we are returning the courses list for all methods
    return Response(courses)  # Return the courses list as JSON response


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        object = Person.objects.all()
        serializer = PeopleSerializer(object, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)  # Return validation errors if any 
    elif request.method == 'PUT':
        data = request.data
        person_id = data.get('id')
        try:
            person_instance = Person.objects.get(id=person_id)
            serializer = PeopleSerializer(person_instance, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)
    elif request.method == 'PATCH':
        data = request.data
        person_id = data.get('id')
        try:
            person_instance = Person.objects.get(id=person_id)
            serializer = PeopleSerializer(person_instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)
    elif request.method == 'DELETE':
        person_id = request.data.get('id')
        try:
            person_instance = Person.objects.get(id=person_id)
            person_instance.delete()
            return Response({'message': 'Person deleted successfully'}, status=204)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)
