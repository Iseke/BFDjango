from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class GetTime(APIView):
    def get(self, request):
        to_print = 'Hello world'
        return Response(to_print, status=status.HTTP_200_OK)