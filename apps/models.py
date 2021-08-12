
from django.db import models

from django.db.models.deletion import CASCADE

# Create your models here.


class Customer(models.Model):
    customerid=models.CharField(primary_key=True,max_length=10)
    customername=models.CharField(max_length=100)
    fathername=models.CharField(max_length=100)
    customerprofile=models.CharField(max_length=100)
    loanaccountno=models.IntegerField()

    def __str__(self):
        return self.customerid

class BranchData(models.Model):
    customerid=models.ForeignKey(Customer,related_name='branch',on_delete=CASCADE)
    zonename=models.CharField(max_length=100)
    regionname=models.CharField(max_length=100)
    areaname=models.CharField(max_length=100)
    branchname=models.CharField(max_length=100)
    branchcode=models.CharField(max_length=100)
    

    def __str__(self):
        return self.branchcode

class CustomerHomeAddressData(models.Model):
    customerid=models.ForeignKey(Customer,related_name='custhomeadd',on_delete=CASCADE)
    pincode=models.IntegerField()
    landmark=models.CharField(max_length=100)
    address1=models.CharField(max_length=500)
    address2=models.CharField(max_length=500)
    address3=models.CharField(max_length=500)
    

    def __str__(self):
        return self.landmark

class CustomerOfficeData(models.Model):
    customerid=models.ForeignKey(Customer,related_name='custoffdata',on_delete=CASCADE)
    officepincode=models.IntegerField()
    officelandmark=models.CharField(max_length=500)
    ofcaddress1=models.CharField(max_length=500)
    ofcaddress2=models.CharField(max_length=500)
    ofcaddress3=models.CharField(max_length=500)
    

    def __str__(self):
        return self.officelandmark

class LoanAmountData(models.Model):
    customerid=models.ForeignKey(Customer,related_name='loanamt',on_delete=CASCADE)
    agreementdate=models.DateField()
    lrn=models.CharField(max_length=100)
    tenor=models.CharField(max_length=100)
    advemi=models.CharField(max_length=100)
    mob=models.CharField(max_length=100)
    

    def __str__(self):
        return self.lrn