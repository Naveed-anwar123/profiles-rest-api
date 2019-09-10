from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIViews"""
        an_api_view = [
            'APIViews functions are (get, post, put, patch)',
            'It is similar to traditional django view',
            'Gives you most control over application login',
            'Is mapped to urls manually'
        ]

        return Response({'message':'Hello!','an_apiview':an_api_view})