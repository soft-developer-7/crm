from django.contrib import admin
from .models import Packs,Industries,Templates,User_bookings
# Register your models here.
admin.site.register(Packs)
admin.site.register(Industries)
admin.site.register(Templates)
admin.site.register(User_bookings)
