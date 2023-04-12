from django.contrib import admin
from .models import Puppy, Feeding, Toy

# Register your models here
admin.site.register(Puppy)

# register the new Feeding Model 
admin.site.register(Feeding)
 #register the new Toy model
admin.site.register(Toy)
