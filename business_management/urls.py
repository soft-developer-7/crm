from django.urls import path
from . import views


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



    path("admin-add-industry-analysis",views.admin_add_industry_analysis,name="admin-add-industry-analysis"),
    path("admin_new_industry_analysis_form",views.admin_new_industry_analysis_form,name="admin_new_industry_analysis_form"),
    path("industry_analysis_view_by_get/<int:id>", views.industry_analysis_view_by_get, name='industry_analysis_view_by_get'),
    path("industry_analysis_update_by_get/<int:id>", views.industry_analysis_update_by_get, name='industry_analysis_update_by_get'),
    path("admin_update_industry_analysis_form", views.admin_update_industry_analysis_form, name='admin_update_industry_analysis_form'),
    path("ajax_call_delete_industry_analysis",views.ajax_call_delete_industry_analysis,name="ajax_call_delete_industry_analysis"),






    path("admin-add-industry-growth-drivers",views.admin_add_industry_growth_drivers,name="admin-add-industry-growth-drivers"),
    path("admin_new_industry_growth_drivers_form",views.admin_new_industry_growth_drivers_form,name="admin_new_industry_growth_drivers_form"),
    path("industry_growth_drivers_view_by_get/<int:id>", views.industry_growth_drivers_view_by_get, name='industry_growth_drivers_view_by_get'),
    path("industry_growth_drivers_update_by_get/<int:id>", views.industry_growth_drivers_update_by_get, name='industry_growth_drivers_update_by_get'),
    path("admin_update_industry_growth_drivers_form", views.admin_update_industry_growth_drivers_form, name='admin_update_industry_growth_drivers_form'),
    path("ajax_call_delete_industry_growth_drivers",views.ajax_call_delete_industry_growth_drivers,name="ajax_call_delete_industry_growth_drivers"),










    path("admin-all-templates",views.admin_all_templates,name="admin-all-templates"),
    path("admin-add-template",views.admin_add_template,name="admin-add-template"),
    path("admin_new_template_form",views.admin_new_template_form,name="admin_new_template_form"),
    path("template_view_by_get/<int:id>", views.template_view_by_get, name='template_view_by_get'),
    path("template_update_by_get/<int:id>", views.template_update_by_get, name='template_update_by_get'),
    path("admin_template_update_form",views.admin_template_update_form,name="admin_template_update_form"),
    path("ajax_call_delete_template",views.ajax_call_delete_template,name="ajax_call_delete_template"),


    path("admin-all-bookings",views.admin_all_bookings,name="admin-all-bookings"),
    path("ajax_call_fetch_template",views.ajax_call_fetch_template,name="ajax_call_fetch_template"),
    path("ajax_call_fetch_user",views.ajax_call_fetch_user,name="ajax_call_fetch_user"),
    path("admin-add-booking",views.admin_add_booking,name="admin-add-booking"),
    path("admin_new_booking_form",views.admin_new_booking_form,name="admin_new_booking_form"),
    path("booking_view_by_get/<int:id>", views.booking_view_by_get, name='booking_view_by_get'),
    path("booking_update_by_get/<int:id>", views.booking_update_by_get, name='booking_update_by_get'),
    path("admin_booking_update_form",views.admin_booking_update_form,name="admin_booking_update_form"),
    path("ajax_call_delete_booking",views.ajax_call_delete_booking,name="ajax_call_delete_booking"),

    path("admin-all-superplan-bookings",views.admin_all_superplan_bookings,name="admin-all-superplan-bookings"),
    path("superplan_booking_view_by_get/<int:id>", views.superplan_booking_view_by_get, name='superplan_booking_view_by_get'),

    path("ajax_call_delete_superplan_booking",views.ajax_call_delete_superplan_booking,name="ajax_call_delete_superplan_booking"),
]