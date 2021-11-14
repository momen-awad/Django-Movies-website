from .serializer import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes([])
def signup(request):
    data = {'data':'','status':''}

    User_Serialized = UserSerializer(data=request.data)

    if User_Serialized.is_valid():
        User_Serialized.save()

        data['data'] = {
            'user': User_Serialized.data,
            'token': Token.objects.get(user__username=User_Serialized.data.get('username')).key,
            'message':'created'
        }
        data['status'] = status.HTTP_201_CREATED


    else:
        data['data'] = User_Serialized.errors
        data['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**data)

