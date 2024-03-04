from django.shortcuts import render,get_object_or_404
from goods.models import Good
from goods.serializers import GoodSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from authorization.permissions import IsSuperAdmin


class GoodList(generics.ListCreateAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    # permission_classes = [permissions.AllowAny]
    

class GoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    # permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    #permission_classes = [permissions.IsAuthenticated, IsSuperAdmin | IsCourier]
    #permission_classes = [permissions.IsAuthenticated, IsSuperAdmin & IsCourier]


class GoodView(ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer