from .models import *
from rest_framework.views import APIView
from .serializers import UserSerializer, ChatSerializer
from django.shortcuts import get_object_or_404
import random
from rest_framework import status
from rest_framework.response import Response
from .ai_helper import generate_ai_response

#to register user

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(tokens=4000)  # default 4000 tokens are alloted
            return Response({'message': 'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = get_object_or_404(User, username=username, password=password)
        token = generate_auth_token()
        user_tokens[token] = user.id

        return Response({'token': token}, status=status.HTTP_200_OK)

class ChatView(APIView):
    def post(self, request):
        token = request.headers.get('Authorization')
        message = request.data.get('message')

        if token not in user_tokens:
            return Response({'error': 'Not valid token'}, status=status.HTTP_401_UNAUTHORIZED)

        user_id = user_tokens[token]
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user.tokens >= 100:
            response = generate_ai_response(message)
            user.tokens -= 100
            user.save()

            # Save chat history
            Chat.objects.create(user=user, message=message, response=response)

            return Response({'response': response}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Out of Tokens'}, status=status.HTTP_400_BAD_REQUEST)


class TokenBalanceView(APIView):
    def post(self, request):
        token = request.headers.get('Authorization')
        

        if token not in user_tokens:
            return Response({'error': 'Not valid token'}, status=status.HTTP_401_UNAUTHORIZED)

        user_id = user_tokens[token]
        user = User.objects.get(id=user_id)

        return Response({'tokens': user.tokens}, status=status.HTTP_200_OK)


user_tokens={}
def generate_auth_token():  #it generates token
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=32))


