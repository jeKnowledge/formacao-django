from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


# Create your views here.



class TokenObtainPairView(TokenObtainPairView):
    
    def post( self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return JsonResponse({'error': 'Invalid credentials'}, status=400)

class TokenRefreshView(APIView):
    def post(self, request):
        refresh = request.data.get('refresh')
        token = RefreshToken(refresh)

        return JsonResponse({
            'access': str(token.access_token)
        })  