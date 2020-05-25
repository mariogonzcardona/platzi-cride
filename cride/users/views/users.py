"""Users Views"""

#Django REST Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Serializers
from cride.users.serializers import (
    AccountVerificationSerializer,
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer
)

class UserLoginAPIView(APIView):
    """User login API View"""
    def post(self,request,*args,**kwargs):
        """Handle HTTP POST request."""
        serializer=UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user,token=serializer.save()
        data={
            'access_token':token,
            'user':UserModelSerializer(user).data,
        }
        return Response(data,status=status.HTTP_201_CREATED)

class UserSignupAPIView(APIView):
    """User signup API View"""
    def post(self,request,*args,**kwargs):
        """Handle HTTP POST request."""
        serializer=UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        data=UserModelSerializer(user).data
        return Response(data,status=status.HTTP_201_CREATED)

class AccountVerificationAPIView(APIView):
    """Account verification API View"""
    def post(self,request,*args,**kwargs):
        """Handle HTTP POST request."""
        serializer=AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        data={'message':'Congratulations, Now go share some rides!'}
        return Response(data,status=status.HTTP_200_OK)