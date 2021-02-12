from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    response = Response({
        'posts': reverse('posts-list', request=request, format=format),
        'users': reverse('users-list', request=request, format=format),
    })
    return response
