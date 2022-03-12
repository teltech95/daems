from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status, viewsets
from . import serializers
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import permissions
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class UserSerializer(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer

    @swagger_auto_schema(operation_summary="Create a user account by signing Up")
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthUserLoginView(generics.GenericAPIView):
    serializer_class = serializers.UserLoginSerializer
    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny, )

    @swagger_auto_schema(operation_summary="Sign in to get access")
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'token': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'username': serializer.data['username'],
                    'email': serializer.data['email'],
                }
            }

            return Response(response, status=status_code)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
