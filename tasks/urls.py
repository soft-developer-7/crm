from django.contrib import admin
from django.urls import path,include,re_path
from . import views
import re

urlpatterns = [
    path("",views.home,name="home"),
    path("home",views.home,name="home"),

    path("contactus",views.contactus,name="contactus"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("faq",views.faq,name="faq"),
    path("keyteam",views.keyteam,name="keyteam"),


    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("registration",views.registration,name="registration"),
    path("reg_form",views.reg_form,name="reg_form"),
    path("login_form",views.login_form,name="login_form"),
    path("success",views.success,name="success"),


    path("auth_admin",views.auth_admin,name="authadmin"),

    path("admin-dashboard",views.admin_dashboard,name="admin-dashboard"),
    path("admin-add-user",views.admin_add_user,name="admin-add-user"),
    path("admin-all-users",views.admin_all_users,name="admin-all-users"),
    path("admin-profile-update",views.admin_profile_update,name="admin-profile-update"),
 
    path("admin_profile_update_form",views.admin_profile_update_form,name="admin_profile_update_form"),
    path("admin_profile_photo_update",views.admin_profile_photo_update,name="admin_profile_photo_update"),
    path("ajax_call_delete_user",views.ajax_call_delete_user,name="ajax_call_delete_user"),
    path("profile_edit_by_get/<int:id>", views.profile_edit_by_get, name='profile_edit_by_get'),
    path("admin_user_profile_update_form",views.admin_user_profile_update_form,name="admin_user_profile_update_form"),
    path("admin_user_profile_photo_update",views.admin_user_profile_photo_update,name="admin_user_profile_photo_update"),
    path("admin_new_user_profile_form",views.admin_new_user_profile_form,name="admin_new_user_profile_form"),
    path("admin-login",views.admin_login,name="admin-login"),
    path("admin_login_form",views.admin_login_form,name="admin_login_form"),


    path("auth_user",views.auth_user,name="auth_user"),

    path("user-dashboard",views.user_dashboard,name="user-dashboard"),
    path("user-profile-update",views.user_profile_update,name="user-profile-update"),
    


    path("user_profile_update_form",views.user_profile_update_form,name="user_profile_update_form"),



    path("admin-add-page",views.admin_add_page,name="admin-add-page"),
    path("admin_new_page_form",views.admin_new_page_form,name="admin_new_page_form"),

    path("admin-all-pages",views.admin_all_pages,name="admin-all-pages"),
    path("page_update_by_get/<int:id>",views.page_update_by_get,name="page_update_by_get"),
    path("admin_page_update_form",views.admin_page_update_form,name="admin_page_update_form"),
    path("ajax_call_delete_page",views.ajax_call_delete_page,name="ajax_call_delete_page"),



    path("admin-add-post",views.admin_add_post,name="admin-add-post"),
    path("admin_new_post_form",views.admin_new_post_form,name="admin_new_post_form"),

    path("admin-all-posts",views.admin_all_posts,name="admin-all-posts"),
    path("post_update_by_get/<int:id>",views.post_update_by_get,name="post_update_by_get"),
    path("admin_post_update_form",views.admin_post_update_form,name="admin_post_update_form"),
    path("ajax_call_delete_post",views.ajax_call_delete_post,name="ajax_call_delete_post"),



    path("admin-add-banner",views.admin_add_banner,name="admin-add-banner"),
    path("admin_new_banner_form",views.admin_new_banner_form,name="admin_new_banner_form"),

    path("admin-all-banners",views.admin_all_banners,name="admin-all-banners"),
    path("banner_update_by_get/<int:id>",views.banner_update_by_get,name="banner_update_by_get"),
    path("admin_banner_update_form",views.admin_banner_update_form,name="admin_banner_update_form"),
    path("ajax_call_delete_banner",views.ajax_call_delete_banner,name="ajax_call_delete_banner"),


    path("successful-purchased",views.successful_purchased,name="successful_purchased"),
    #-------------------------- Forms ------------------------

   
    path("user_form_1",views.user_form_1,name="user_form_1"),
    path("user_form_1_submit",views.user_form_1_submit,name="user_form_1_submit"),
    path("user_form_2_submit",views.user_form_2_submit,name="user_form_2_submit"),
    path("user_form_3_submit",views.user_form_3_submit,name="user_form_3_submit"),
    path("user_form_4_submit",views.user_form_4_submit,name="user_form_4_submit"),
    path("user_form_5_submit",views.user_form_5_submit,name="user_form_5_submit"),
    path("user_form_6_submit",views.user_form_6_submit,name="user_form_6_submit"),
    path("user_form_7_submit",views.user_form_7_submit,name="user_form_7_submit"),
    path("user_form_8_submit",views.user_form_8_submit,name="user_form_8_submit"),
    path("user_form_9_submit",views.user_form_9_submit,name="user_form_9_submit"),
    path("user_form_9_1_submit",views.user_form_9_1_submit,name="user_form_9_1_submit"),
    path("user_form_9_1_historical_submit",views.user_form_9_1_historical_submit,name="user_form_9_1_historical_submit"),
    path("user_form_10_submit",views.user_form_10_submit,name="user_form_10_submit"),
    path("user_form_11_submit",views.user_form_11_submit,name="user_form_11_submit"),
    path("user_form_12_submit",views.user_form_12_submit,name="user_form_12_submit"),


    path("view_income_statement",views.cal_income_statement,name="view_income_statement"),
    

    path("user-all-superplan-bookings",views.user_all_superplan_bookings,name="user-all-superplan-bookings"),
    path("user_template_view_by_get/<int:id>",views.user_template_view_by_get,name="user_template_view_by_get"),

    path("incomplete-superplan-bookings-check",views.incomplete_superplan_bookings_check,name="incomplete-superplan-bookings-check"),
    path("user-all-incomplete-superplan-bookings",views.user_all_incomplete_superplan_bookings,name="user-all-incomplete-superplan-bookings"),
    path("user_incomplete_superplan_by_get/<int:id>",views.user_incomplete_superplan_by_get,name="user_incomplete_superplan_by_get"),
    path("ajax_call_delete_incomplete_booking",views.ajax_call_delete_incomplete_booking,name="ajax_call_delete_incomplete_booking"),




    path("superplan_form_number/<str:id>",views.superplan_form_number,name="superplan_form_number"),
    








    path("user_template_view_1",views.user_template_view_1,name="user_template_view_1"),
    path("test",views.test,name="test"), # print all multi input data
    path("test_xl",views.test_xl,name="test_xl"), # print all multi input xl data
    path("test_image",views.test_image,name="test_image"), # print all multi image data
    path("reset_db",views.reset_db,name="reset_db"), #reset_db

    path("xl_file_find",views.xl_file_find,name="xl_file_find"), #XL file found
    path("new_xl_get/<int:id>",views.new_xl_get,name="new_xl_get"), #New xl found
    
    

]