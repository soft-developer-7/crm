from django.contrib import admin
from .models import User_db,Posts,Pages,Banners,super_plan_forms
# Register your models here.

admin.site.register(User_db)
admin.site.register(Posts)
admin.site.register(Pages)
admin.site.register(Banners)
admin.site.register(super_plan_forms)