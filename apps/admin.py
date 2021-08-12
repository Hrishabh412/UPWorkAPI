
from django.contrib import admin

from .models import Customer,BranchData,CustomerHomeAddressData,LoanAmountData, CustomerOfficeData
# Register your models here.


admin.site.register(Customer)
admin.site.register(BranchData)
admin.site.register(CustomerHomeAddressData)
admin.site.register(CustomerOfficeData)
admin.site.register(LoanAmountData)