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
    path("user_profile_photo_update",views.user_profile_photo_update,name="user_profile_photo_update"),



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
    

]