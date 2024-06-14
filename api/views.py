from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FirstTodo
from .serializers import TodoSerializer

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def todo_all(request, pk=None):
    # GET Data
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = FirstTodo.objects.get(id=id)
            serializer = TodoSerializer(stu)
            return Response(serializer.data)

        stu = FirstTodo.objects.all()
        serializer = TodoSerializer(stu, many=True)
        return Response(serializer.data)

    # POST Data
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'})
        return Response(serializer.errors)

    # PUT Data
    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        stu = FirstTodo.objects.get(pk=id)
        serializer = TodoSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors)

    # PATCH Data
    if request.method == 'PUTCH':
        # id = request.data.get('id')
        id = pk
        stu = FirstTodo.objects.get(pk=id)
        serializer = TodoSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)

    # DELETE Data
    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        stu = FirstTodo.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'})
