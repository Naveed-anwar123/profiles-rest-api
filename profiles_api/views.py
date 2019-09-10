from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Return a list of APIViews"""
        an_api_view = [
            'APIViews functions are (get, post, put, patch)',
            'It is similar to traditional django view',
            'Gives you most control over application login',
            'Is mapped to urls manually'
        ]

        return Response({'message':'Hello!','an_apiview':an_api_view})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            messsage = f'Hello {name}'

            return Response({'message': messsage})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST 
                )

    def put(self, request, pk=None):
        """Handle updating an oboject"""
        return Response({'method': 'PUT'})  #Replacing and object

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        """Handle deleting of an object"""
        return Response({'method': 'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """"Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns a hello message"""
        a_view_set = [
            'ViewSet functions are (list, create, retrieve, update, partial update)',
            'It is similar to traditional django view',
            'Gives you most control over application login',
            'Is mapped to urls manually'
        ]
        return Response({'message':'Hello','a_view_set':a_view_set})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    #which method to use for authentication
    authentications_classes = (TokenAuthentication,)
    #what permissions a specific user have
    permission_classes = (permissions.UpdateOwnProfile,)
