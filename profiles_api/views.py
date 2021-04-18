from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializer


class HelloApiView(APIView):
    """test api view class """
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """ returns a list of apiview features"""
        an_apiview = [
            "uses http methods as function get post patch put delete",
            "Is smilar to a traditional django view.",
            "gives you the most control oveer you application logic",
            "ıs mapped manually to Urls"
        ]

        return Response({"message": "Hello!", "description": "sasasaas", "an_apiview": an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """ Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """ handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """ return hello message"""
        a_viewset = [
            'uses actions list create retrieve update partial_update',
            'automatically mapst to urls using routers',
            'provvides more functionality with less code'
        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk = None):
        """ Handle gettin an object by its ID """
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request, pk=None):
        return Response({'http_method':'DELETE'})