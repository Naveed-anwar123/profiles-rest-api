from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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



