from django.shortcuts import redirect
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dotenv import load_dotenv
import os

load_dotenv()
github_client_id = os.getenv('github_client_id')
github_client_secret = os.getenv('github_client_secret')

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def github_auth(request):
    github_auth_url = f'https://github.com/login/oauth/authorize?client_id={github_client_id}'
    return redirect(github_auth_url)

@api_view(['GET'])
def github_auth_callback(request):
    code = request.GET.get('code')
    try:
        response = requests.post('https://github.com/login/oauth/access_token', {
            'client_id': github_client_id,
            'client_secret': github_client_secret,
            'code': code
        }, headers={'Accept': 'application/json'})

        response_json = response.json()
        access_token = response_json['access_token']
        return redirect('/api/user?access_token=' + access_token)
    except Exception as e:
        print('Failed to exchange code for access token:', e)
        return Response({'error': 'Failed to exchange code for access token'})
    
@api_view(['GET'])
def user(request):
    access_token = request.GET.get('access_token')
    try:
        response = requests.get('https://api.github.com/user', headers={
            'Authorization': f'token {access_token}'
        })
        user = response.json()
        userName = user['login']
        return Response({'user': userName})
    except Exception as e:
        print('Failed to fetch user:', e)
        return Response({'error': 'Failed to fetch user detail'})

