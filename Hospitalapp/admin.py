from django.contrib import admin
from Hospitalapp.models import Users, Product, Members, Message, Contact

# Register your models here.
admin.site.register(Users)
admin.site.register(Product)
admin.site.register(Members)
admin.site.register(Message)
admin.site.register(Contact)
