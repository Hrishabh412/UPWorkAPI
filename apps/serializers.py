from rest_framework import serializers
from .models import Customer,BranchData,CustomerHomeAddressData,LoanAmountData, CustomerOfficeData


#serializers are just like Forms


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #fields = ['id','firstname', 'lastname', 'email', 'age', 'dateofbirth', 'mobileno']
        fields='__all__'

class BranchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchData
        #fields = ['id','firstname', 'lastname', 'email', 'age', 'dateofbirth', 'mobileno']
        fields='__all__'

class CustomerHomeAddressDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerHomeAddressData
        #fields = ['id','firstname', 'lastname', 'email', 'age', 'dateofbirth', 'mobileno']
        fields='__all__'
class LoanAmountDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanAmountData
        #fields = ['id','firstname', 'lastname', 'email', 'age', 'dateofbirth', 'mobileno']
        fields='__all__'
class CustomerOfficeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOfficeData
        #fields = ['id','firstname', 'lastname', 'email', 'age', 'dateofbirth', 'mobileno']
        fields='__all__'