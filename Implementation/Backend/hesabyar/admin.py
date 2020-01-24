from django.contrib import admin

# Register your models here.
from hesabyar.models import *

admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(TransactionMember)
admin.site.register(Contact)
