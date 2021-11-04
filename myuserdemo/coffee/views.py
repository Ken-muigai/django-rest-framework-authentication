from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#
from .serializers import RegistrationSerializer


@api_view(['POST',])
def registrationView(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully created"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors

        return Response(data)


