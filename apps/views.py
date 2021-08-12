from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from apps.models import Customer,BranchData,CustomerHomeAddressData,LoanAmountData, CustomerOfficeData
from .serializers import CustomerSerializer, BranchDataSerializer, LoanAmountDataSerializer, CustomerHomeAddressDataSerializer, CustomerOfficeDataSerializer
from apps import serializers
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class CustomerGenericAPIView(mixins.ListModelMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= CustomerSerializer
    queryset=Customer.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    def delete(self, request):
        return self.destroy(request)

class BranchDataGenericAPIView(mixins.ListModelMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= BranchDataSerializer
    queryset=BranchData.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class LoanAmountDataGenericAPIView(mixins.ListModelMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= LoanAmountDataSerializer
    queryset=LoanAmountData.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
class CustomerHomeAddressDataGenericAPIView(mixins.ListModelMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= CustomerHomeAddressDataSerializer
    queryset=CustomerHomeAddressData.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class CustomerOfficeDataGenericAPIView(mixins.ListModelMixin,generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class= CustomerOfficeDataSerializer
    queryset=CustomerOfficeData.objects.all()
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)



