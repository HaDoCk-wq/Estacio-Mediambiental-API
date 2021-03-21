from django.shortcuts import render
from django.views.generic.base import View
from django.http import JsonResponse
from rest_framework import viewsets
import json
from estaciOmediambiental.models import Client, Sensor, Registre
from estaciOmediambiental.serializers import ClientSerializer, SensorSerializer, RegistreSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.core import serializers
from rest_framework.renderers import JSONRenderer


# class test(View):
#     def get(self, request):
#         context = {
#             'reservas': "reservas",
#             'user': "request"
#         }
#         return render(request, 'test.html', context)


# class xhr(View):
#     def post(self, request):
#         dades = json.loads(request.body.decode("utf-8"))
#         data = {
#             'like': dades["like"],
#             'post': dades["post"],
#         }
#         return JsonResponse(data)


# class dades(View):
#     def get(self, request):
#         context = {
#             'reservas': "reservas",
#             'user': "request"
#         }
#         return render(request, 'dades.html', context)


################### API #####################

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class RegistreViewSet(viewsets.ModelViewSet):
    queryset = Registre.objects.all()
    serializer_class = RegistreSerializer


class ListRegistres(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    #authentication_classes = [authentication.TokenAuthentication]
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        #valors = [Registre.valor for Registre in Registre.objects.all()]

        serializer = RegistreSerializer(Registre.objects.filter(), many=True)

        return Response(serializer.data)
