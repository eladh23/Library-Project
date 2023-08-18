from django.contrib import admin
from .models import Books, CustomerUser, Loan
from library.models import CustomerUser

admin.site.register(Books)
admin.site.register(CustomerUser)
admin.site.register(Loan)
