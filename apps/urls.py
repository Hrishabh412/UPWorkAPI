from django.shortcuts import render
from django.urls import path

# Create your views here.
from .views import  CustomerGenericAPIView, BranchDataGenericAPIView, LoanAmountDataGenericAPIView, CustomerHomeAddressDataGenericAPIView, CustomerOfficeDataGenericAPIView

urlpatterns = [
    #path('student_details/<int:pk>', student_detail),
    path('customer/', CustomerGenericAPIView.as_view()),
    path('branch/', BranchDataGenericAPIView.as_view()),
    path('loanamount/', LoanAmountDataGenericAPIView.as_view()),
    path('customerhome/', CustomerHomeAddressDataGenericAPIView.as_view()),
    path('customeroffice/', CustomerOfficeDataGenericAPIView.as_view()),
]