from django.contrib import admin
from django.urls import path,include,re_path
from . import views
import re

urlpatterns = [
    path("admin-all-packages",views.admin_all_packages,name="admin-all-packages"),
    path("admin-add-package",views.admin_add_package,name="admin-add-package"),
    path("admin_new_package_form",views.admin_new_package_form,name="admin_new_package_form"),
    path("package_update_by_get/<int:id>", views.package_update_by_get, name='package_update_by_get'),
    path("admin_package_update_form",views.admin_package_update_form,name="admin_package_update_form"),
    path("ajax_call_delete_package",views.ajax_call_delete_package,name="ajax_call_delete_package"),


    path("admin-all-industries",views.admin_all_industries,name="admin-all-industries"),
    path("admin-add-industry",views.admin_add_industry,name="admin-add-industry"),
    path("admin_new_industry_form",views.admin_new_industry_form,name="admin_new_industry_form"),
    path("industry_update_by_get/<int:id>", views.industry_update_by_get, name='industry_update_by_get'),
    path("admin_industry_update_form",views.admin_industry_update_form,name="admin_industry_update_form"),
    path("ajax_call_delete_industry",views.ajax_call_delete_industry,name="ajax_call_delete_industry"),
]