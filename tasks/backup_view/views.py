from django.shortcuts import render,redirect
from django.core.serializers import serialize
from django.http import HttpResponse,request,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
import json
from datetime import date
import datetime
from django.http import JsonResponse
from .models import User_db,Pages,Posts,Banners,super_plan_forms,super_plan_forms_multiple_inputs,super_plan_forms_multiple_images,super_plan_forms_multiple_files,super_plan_forms_multiple_inputs_xl,super_plan_form_xl_input,super_plan_projection
from django.core.paginator import Paginator
from business_management.models import Packs,Industries,User_bookings,Templates,Industries, Industry_analysis,Industry_growth_drivers
from pyexcel_xlsx import get_data
from openpyxl import load_workbook
import os
from django.conf import settings
from shutil import copyfile

from math import ceil





#--------- custom functions--------------
def multi_input_insert(request,name):
    user = User_db.objects.filter(id=request.session['user']).get()
    form_id = request.session['form']
    values = request.POST.getlist(name)
    multi = super_plan_forms_multiple_inputs()
    multi.user = user
    multi.form_id = form_id

    for i in range(0,len(values)):
        if(values[i]):
            val = values[i]
            if i==0:
                multi.f_1 = val
            elif i==1:
                multi.f_2 = val
            elif i==2:
                multi.f_3 = val
            elif i==3:
                multi.f_4 = val
            elif i==4:
                multi.f_5 = val
            elif i==5:
                multi.f_6 = val
            elif i==6:
                multi.f_7 = val
            elif i==7:
                multi.f_8 = val
            elif i==8:
                multi.f_9 = val
            elif i==9:
                multi.f_10 = val
    multi.save()
    return multi







def multi_input_insert_projection(request,name):
    user = User_db.objects.filter(id=request.session['user']).get()
    form_id = request.session['form']
    values = request.POST.getlist(name)
    multi = super_plan_forms_multiple_inputs()
    multi.user = user
    multi.form_id = form_id
    
    for i in range(0,len(values)):
        if(values[i]):
            val = values[i]
            if i==0:
                multi.f_1 = val
            elif i==1:
                multi.f_2 = val
            elif i==2:
                multi.f_3 = val
            elif i==3:
                multi.f_4 = val
            elif i==4:
                multi.f_5 = val

    multi.save()
    return multi



def multi_input_blank(request):                                     # Blank multi
    user = User_db.objects.filter(id=request.session['user']).get()
    form_id = request.session['form']
    multi = super_plan_forms_multiple_inputs()
    multi.user = user
    multi.form_id = form_id
    multi.save()
    return multi


def multi_input_insert_xl(request,data,row):


    multi = super_plan_forms_multiple_inputs_xl()
    multi.form_id = request.session['form']

    multi.f_1 = data["Historicals"][row][2]
    multi.f_2 = data["Historicals"][row][3]
    multi.f_3 = data["Historicals"][row][4]

    multi.save()
    return multi



def multi_image_insert(request,name,r_id=None):
    user = User_db.objects.filter(id=request.session['user']).get()
    form_id = request.session['form']

    values = request.FILES.getlist(name)




    if(r_id):
        i_name=name.replace("[]","")
        multi = super_plan_forms_multiple_images.objects.filter(id=r_id).get()
        c=0
        if(multi):
            for i in range(1,7):
                if(request.POST.get(i_name+'_'+str(i)) and request.POST[i_name+'_'+str(i)]=="1"):

                    val = values[c]
                    if i==1:
                        multi.i_1 = val

                    elif i==2:
                        multi.i_2 = val

                    elif i==3:
                        multi.i_3 = val

                    elif i==4:
                        multi.i_4 = val

                    elif i==5:
                        multi.i_5 = val

                    elif i==6:
                        multi.i_6 = val
                    c+=1

                multi.save()


    else:
        multi = super_plan_forms_multiple_images()
        multi.user = user
        multi.form_id = form_id
        for i in range(0,len(values)):
            if(values[i]):
                val = values[i]
                if i==0:
                    multi.i_1 = val

                elif i==1:
                    multi.i_2 = val

                elif i==2:
                    multi.i_3 = val

                elif i==3:
                    multi.i_4 = val

                elif i==4:
                    multi.i_5 = val

                elif i==5:
                    multi.i_6 = val


        multi.save()
        return multi













def competitor_analysis_input(request,name):                   # Competitor Analysis table
    user = User_db.objects.filter(id=request.session['user']).get()
    form_id = request.session['form']
    values = request.POST.getlist(name)
    multi = super_plan_forms_multiple_inputs()
    multi.user = user
    multi.form_id = form_id

    if "1" in values:
        multi.f_1 = 1
    if "2" in values:
        multi.f_2 = 2
    if "3" in values:
        multi.f_3 = 3
    if "4" in values:
        multi.f_4 = 4
    if "5" in values:
        multi.f_5 = 5

    multi.save()
    return multi


# Create your views here.


# -------------------------------------- Static pages -----------------------------------------



                                # Home page
def home(request):
    return render(request,'home.html')


                                # Contact Us page
def contactus(request):
    return render(request,'contactus.html')



                                # About Us page
def aboutus(request):
    return render(request,'aboutus.html')


                                # FAQ page
def faq(request):
    return render(request,'faq.html')


                                # Keyteam page
def keyteam(request):
    return render(request,'keyteam.html')


                                # Success page
def success(request):
    return render(request,'success.html')





                                # Login page
def login(request):
    return render(request,'login.html')





                                # Registration page
def registration(request):
    return render(request,'registration.html')







# -------------------------------------- Outer Forms --------------------------------------------



                                # Registration Form Submit
def reg_form(request):

    if(request.method=="POST"):
        name = request.POST['name']
        mobile = request.POST['phone']
        role ="user"
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['confirm_password']

        if(password==password_confirmation):
            user = User_db.objects.filter(email=email).count()
            if(user):
                messages.info(request,"Email id already exists !")
                return render(request,'registration.html')

            else:
                password = make_password(password)
                user=User_db(name=name,mobile=mobile,email=email,password=password,role=role,address=address)
                user.save()
                return redirect('/success')



        else:
            messages.info(request,"Password not same !")
            return render(request,'registration.html')

    else:
        messages.info(request,"Method is not POST !")
        return render(request,'registration.html')










                                # Login Form Submit
def login_form(request):

    if(request.method=="POST"):
        email = request.POST['email']
        user = User_db.objects.filter(email=email).count()
        if(user):
            user =  User_db.objects.get(email=email)
            password = request.POST['password']

            if(check_password(password,user.password) and user.role!="admin"):
                request.session['user']=user.id
                request.session['role']=user.role
                request.session['name']=user.name
                request.session['photo']=user.photo.url

                return redirect('/user-dashboard')


            else:

                messages.info(request,"Invalid user id or password !")
                return redirect('/login')

        else:

            messages.info(request,"Invalid user id or password !")
            return redirect('/login')









# -------------------------------------- Admin pages --------------------------------------------


def auth_admin(request):                                # Admin authentication
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role=="admin"):
            return True
        else:
            return False
    else:
        return False




                                # Admin Login page
def admin_login(request):
    return render(request,'admin-login.html')






                                # Admin dashboard page
def admin_dashboard(request):

    if(auth_admin(request)):
        users = User_db.objects.all().count()
        pages = Pages.objects.all().count()
        posts = Posts.objects.all().count()
        banners = Banners.objects.all().count()
        packs = Packs.objects.all().count()
        inds = Industries.objects.all().count()
        tmps = Templates.objects.all().count()
        bookings = User_bookings.objects.all().count()

        return render(request,'admin-dashboard.html',{'total_users':users,'total_pages':pages,
        'total_posts':posts,'total_banners':banners,'total_packs':packs,'total_inds':inds,'total_tmps':tmps,
        'total_bookings':bookings})
    else:
        return redirect('/login')





                                # Logout
def logout(request):
    request.session.clear()
    return redirect('/login')



                                # Admin Add user page
def admin_add_user(request):
    if(auth_admin(request)):
        return render(request,'admin-add-user.html')
    else:
        return redirect('/login')




                                # Admin All users page
def admin_all_users(request):
    if(auth_admin(request)):
        users = User_db.objects.exclude(role="admin").all()
        return render(request,'admin-all-users.html',{'users':users})
    else:
        return redirect('/login')



                                # Admin profile update page
def admin_profile_update(request):
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role=="admin"):
            return render(request,'admin-profile-update.html',{'name':user.name,'mobile':user.mobile,
            'email':user.email,'address':user.address,'photo':user.photo.url})
        else:
            return redirect('/login')
    else:
        return redirect('/login')





                                # Admin Add PAGE page
def admin_add_page(request):
    if(auth_admin(request)):
        return render(request,'admin-add-page.html')
    else:
        return redirect('/login')





                                # Admin all PAGES page
def admin_all_pages(request):
    if(auth_admin(request)):
        pages = Pages.objects.all()
        return render(request,'admin-all-pages.html',{"pages":pages})
    else:
        return redirect('/login')






                                # Admin Add Post page
def admin_add_post(request):
    if(auth_admin(request)):
        return render(request,'admin-add-post.html')
    else:
        return redirect('/login')




                                # Admin all Posts page
def admin_all_posts(request):
    if(auth_admin(request)):
        posts = Posts.objects.order_by('-pub_date')
        return render(request,'admin-all-posts.html',{"posts":posts})
    else:
        return redirect('/login')







                                # Admin Add Banner page
def admin_add_banner(request):
    if(auth_admin(request)):
        return render(request,'admin-add-banner.html')
    else:
        return redirect('/login')




                                # Admin all Banners page
def admin_all_banners(request):
    if(auth_admin(request)):
        banners = Banners.objects.order_by('-date')
        return render(request,'admin-all-banners.html',{"banners":banners})
    else:
        return redirect('/login')






# -------------------------------------- Admin tasks -----------------------------------------------------------------









                                # Admin Login Form Submit
def admin_login_form(request):

    if(request.method=="POST"):
        email = request.POST['email']
        user = User_db.objects.filter(email=email).count()
        if(user):
            user = User_db.objects.get(email=email)
            password = request.POST['password']

            if(user.role=="admin" and check_password(password,user.password)):
                request.session['user']=user.id
                request.session['role']=user.role
                request.session['name']=user.name
                request.session['photo']=user.photo.url

                return redirect('/admin-dashboard')


            else:

                messages.info(request,"Invalid user id or password !")
                return render(request,'admin-login.html')

        else:

            messages.info(request,"Invalid user id or password !")
            return render(request,'admin-login.html')









def admin_profile_update_form(request):                                # Admin Profile Update Form

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role=="admin" and request.method=="POST"):
            user =  User_db.objects.get(id=request.session['user'])

            user.name=request.POST["name"]
            user.mobile=request.POST["mobile"]
            user.address=request.POST["address"]

            if(request.POST['password']!=""):
                user.password = make_password(request.POST['password'])
            user.save()
            return redirect("/admin-profile-update")
        else:
            return redirect('/login')
    else:
        return redirect('/login')








def admin_profile_photo_update(request):                                # Admin Profile Photo Update Form

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role=="admin" and request.method=="POST"):

            photo = request.FILES["photo"]
            user.photo = photo
            user.save()
            return redirect("/admin-profile-update")
        else:
            return redirect('/login')
    else:
        return redirect('/login')








def ajax_call_delete_user(request):                                # AJAX - Delete User by Admin
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role=="admin" and request.method=="POST"):
            user = User_db.objects.filter(id=request.POST['id']).get()
            if(user and user.role !="admin"):
                id = request.POST['id']
                User_db.objects.filter(id=id).delete()
                return JsonResponse({"value":id},status=200)
            else:
                return JsonResponse({"value":0})
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})










def profile_edit_by_get(request,id):                                # Profile Edit by GET method
    if(auth_admin(request)):
        user =  User_db.objects.get(id=id)
        if(user.role !="admin"):
            return render(request,'admin-update-user.html',{'id':id,'name':user.name,'mobile':user.mobile,'email':user.email,'address':user.address,'role':user.role,'photo':user.photo.url})
        else:
            return redirect('/login')
    else:
        return redirect('/login')










def admin_user_profile_update_form(request):                                # Admin USER profile update Form
    inp_user = User_db.objects.filter(id=request.POST['id']).count()
    if(auth_admin(request) and inp_user and request.method=="POST"):

        user =  User_db.objects.get(id=request.POST['id'])

        user.name=request.POST["name"]
        user.mobile=request.POST["mobile"]
        user.address=request.POST["address"]
        user.role=request.POST["role"]

        if(request.POST['password']!=""):
            user.password = make_password(request.POST['password'])
        user.save()
        return redirect("/admin-all-users")
    else:
        return redirect('/login')








def admin_user_profile_photo_update(request):                               # Admin USER profile PHOTO update Form

    inp_user = User_db.objects.filter(id=request.POST['id']).count()
    if(auth_admin(request) and inp_user and request.method=="POST"):
        user =  User_db.objects.get(id=request.POST['id'])
        photo = request.FILES["photo"]
        user.photo = photo
        user.save()
        return redirect("/admin-all-users")
    else:
        return redirect('/login')















def admin_new_user_profile_form(request):                                   # Admin NEW USER Form
    user2 = User_db.objects.filter(email=request.POST["email"]).count()

    if(user2):
        messages.info(request,"Email id already exists !")
        return redirect('/admin-add-user')

    if(auth_admin(request) and request.method=="POST"):
        user =  User_db()
        user.email=request.POST["email"]
        user.name=request.POST["name"]
        user.mobile=request.POST["mobile"]
        user.address=request.POST["address"]
        user.role=request.POST["role"]
        user.password = make_password(request.POST['password'])

        if(request.FILES):
            user.photo = request.FILES["photo"]

        user.save()

        return redirect("/admin-all-users")
    else:
        return redirect('/login')










def admin_new_page_form(request):                                   # Admin New Page Form

    page = Pages.objects.filter(slug=request.POST["slug"]).count()
    if(page):
        messages.info(request,"Slug is already exists !")
        return redirect('/admin-add-page')

    if(auth_admin(request) and request.method=="POST"):
        new_page =  Pages()

        new_page.title=request.POST["title"]
        new_page.meta=request.POST["meta"]
        new_page.slug=request.POST["slug"]
        new_page.keywords=request.POST["keywords"]
        new_page.post=request.POST["post"]

        if(request.FILES):
            new_page.body_photo = request.FILES["photo"]

        new_page.save()

        return redirect("/admin-all-pages")

    else:
        return redirect('/login')






def page_update_by_get(request,id):                                   # page by GET method by Admin
    if(auth_admin(request)):
        page =  Pages.objects.get(id=id)
        if(page):
            if(page.body_photo):
                return render(request,'admin-page-update.html',{'id':id,'title':page.title,'meta':page.meta,
                'slug':page.slug,'keywords':page.keywords,'post':page.post,'photo':page.body_photo.url})
            else:
                return render(request,'admin-page-update.html',{'id':id,'title':page.title,'meta':page.meta,
                'slug':page.slug,'keywords':page.keywords,'post':page.post})

        else:
            return redirect('/login')
    else:
        return redirect('/login')








def admin_page_update_form(request):                                   # Admin PAGE update Form

    page = Pages.objects.filter(id=request.POST['id']).get()
    if(page.slug!=request.POST["slug"]):
        c = Pages.objects.filter(slug=request.POST["slug"]).count()
        if(c):
            messages.info(request,"Slug is already exists !")
            return redirect('/page_update_by_get/'+str(request.POST['id']))


    if(auth_admin(request) and page and request.method=="POST"):
        page.title=request.POST["title"]
        page.meta=request.POST["meta"]
        page.slug=request.POST["slug"]
        page.keywords=request.POST["keywords"]
        page.post=request.POST["post"]

        if(request.FILES):
            page.body_photo = request.FILES["photo"]
        page.save()
        return redirect("/admin-all-pages")
    else:
        return redirect('/login')





def ajax_call_delete_page(request):                                   # AJAX call DELETE Page - By Admin
    if(auth_admin(request) and request.method=="POST"):
        page = Pages.objects.filter(id=request.POST['id']).count()
        if(page):
            page = Pages.objects.filter(id=request.POST['id']).get()
            page.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})












def admin_new_post_form(request):                                   # Admin New Post Form

    post = Posts.objects.filter(slug=request.POST["slug"]).count()
    if(post):
        messages.info(request,"Slug is already exists !")
        return redirect('/admin-add-post')

    if(auth_admin(request) and request.method=="POST"):
        new_post =  Posts()

        new_post.title=request.POST["title"]
        new_post.meta=request.POST["meta"]
        new_post.slug=request.POST["slug"]
        new_post.keywords=request.POST["keywords"]
        new_post.post=request.POST["post"]

        if(request.FILES.get("banner_photo")):
            new_post.banner_photo = request.FILES["banner_photo"]

        if(request.FILES.get("body_photo")):
            new_post.body_photo = request.FILES["body_photo"]

        new_post.author_id = request.session["user"]
        new_post.save()

        return redirect("/admin-all-posts")

    else:
        return redirect('/login')








def post_update_by_get(request,id):                                   # Post by GET method by Admin
    if(auth_admin(request)):
        post =  Posts.objects.get(id=id)
        if(post):
            if(post.body_photo):
                return render(request,'admin-post-update.html',{'id':id,'title':post.title,'meta':post.meta,
                'slug':post.slug,'keywords':post.keywords,'post':post.post,'banner_photo':post.banner_photo.url,
                'body_photo':post.body_photo.url})
            else:
                 return render(request,'admin-post-update.html',{'id':id,'title':post.title,'meta':post.meta,
                'slug':post.slug,'keywords':post.keywords,'post':post.post,'banner_photo':post.banner_photo.url})

        else:
            return redirect('/login')
    else:
        return redirect('/login')






def admin_post_update_form(request):                                   # Admin Post update Form

    post = Posts.objects.filter(id=request.POST['id']).get()
    if(post.slug!=request.POST["slug"]):
        c = Posts.objects.filter(slug=request.POST["slug"]).count()
        if(c):
            messages.info(request,"Slug is already exists !")
            return redirect('/post_update_by_get/'+str(request.POST['id']))


    if(auth_admin(request) and post and request.method=="POST"):
        post.title=request.POST["title"]
        post.meta=request.POST["meta"]
        post.slug=request.POST["slug"]
        post.keywords=request.POST["keywords"]
        post.post=request.POST["post"]

        if(request.FILES.get("banner_photo")):
            post.banner_photo = request.FILES["banner_photo"]

        if(request.FILES.get("body_photo")):
            post.body_photo = request.FILES["body_photo"]

        post.save()
        return redirect("/admin-all-posts")
    else:
        return redirect('/login')




def ajax_call_delete_post(request):                                   # AJAX call DELETE Post - By Admin
    if(auth_admin(request) and request.method=="POST"):
        post = Posts.objects.filter(id=request.POST['id']).count()
        if(post):
            post = Posts.objects.filter(id=request.POST['id']).get()
            post.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})









def admin_new_banner_form(request):                                   # Admin New Banner Form

    banner = Banners.objects.filter(title=request.POST["title"]).count()
    if(banner):
        messages.info(request,"Title is already exists !")
        return redirect('/admin-add-banner')

    if(auth_admin(request) and request.method=="POST"):
        new_banner =  Banners()

        new_banner.title=request.POST["title"]

        if(request.POST.get("desc")):
            new_banner.desc=request.POST["desc"]

        new_banner.alt=request.POST["alt"]

        if(request.POST.get("category")):
            new_banner.category=request.POST["category"]

        new_banner.photo = request.FILES["photo"]

        new_banner.save()

        return redirect("/admin-all-banners")

    else:
        return redirect('/login')






def banner_update_by_get(request,id):                                   # Banner by GET method by Admin
    if(auth_admin(request)):
        banner =  Banners.objects.get(id=id)
        if(banner):
            return render(request,'admin-banner-update.html',{'id':id,'title':banner.title,'desc':banner.desc,
            'alt':banner.alt,'category':banner.category,'photo':banner.photo.url})
        else:
            return redirect('/login')
    else:
        return redirect('/login')





def admin_banner_update_form(request):                                   # Admin Banner update Form
    banner = Banners.objects.filter(id=request.POST['id']).get()
    if(banner and auth_admin(request) and request.method=="POST"):
        banner.title=request.POST["title"]
        if(request.POST.get("desc")):
            banner.desc=request.POST["desc"]
        banner.alt=request.POST["alt"]
        if(request.POST.get("category")):
            banner.category=request.POST["category"]
        if(request.FILES):
            banner.photo = request.FILES["photo"]
        banner.save()
        return redirect("/admin-all-banners")
    else:
        return redirect('/login')











def ajax_call_delete_banner(request):                                   # AJAX call DELETE Banner - By Admin
    if(auth_admin(request) and request.method=="POST"):
        banner = Banners.objects.filter(id=request.POST['id']).count()
        if(banner):
            banner = Banners.objects.filter(id=request.POST['id']).get()
            banner.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})










#----------------------------------------- USER's Page and Tasks---------------


def auth_user(request):                                   # User authentication
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role!="admin"):
            return True
        else:
            return False
    else:
        return False




def user_dashboard(request):                                # User Dashboard

    if(auth_user(request)):
        return render(request,'user-dashboard.html')
    else:
        return redirect('/login')




def user_profile_update(request):                                # User Profile Update Page

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role!="admin"):
            user =  User_db.objects.get(id=request.session['user'])

            return render(request,'user-profile-update.html',{'name':user.name,'countrycode':user.countrycode,'mobile':user.mobile,
            'email':user.email,'address':user.address,'photo':user.photo.url})
        else:
            return redirect('/login')
    else:
        return redirect('/login')











def user_profile_update_form(request):                                # User Profile Update Form

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()

        if(user and user.role!="admin" and request.method=="POST"):

            user.name=request.POST["name"]
            user.mobile=request.POST["mobile"]
            user.address=request.POST["address"]



            if(request.POST['password']!=""):
                user.password = make_password(request.POST['password'])

            if(request.POST.get('countrycode')):
                print(request.POST['countrycode'])
                user.countrycode = request.POST['countrycode']


            if(request.FILES.get("photo")):
                photo = request.FILES["photo"]
                user.photo = photo

            user.save()


            request.session['name']=user.name
            request.session['photo']=user.photo.url

            return redirect("/user-profile-update")
        else:
            return redirect('/login')
    else:
        return redirect('/login')












def successful_purchased(request):                                # User Successful Purchased

    if(auth_user(request)):
        book = super_plan_forms.objects.filter(id=request.session['form']).get()
        book.current_fillup_position = 13
        book.save()
        return render(request,'successful-purchased.html')
    else:
        return redirect('/login')



#------------------------------------------ Projection Table works --------------------



def projection_table_init(request):

    projection_table=super_plan_projection()
    projection_table.form_id=request.session['form']

    projection_table.ins_particulars_stream_1 = multi_input_blank(request)
    projection_table.ins_particulars_stream_2 = multi_input_blank(request)
    projection_table.ins_particulars_stream_3 = multi_input_blank(request)
    projection_table.ins_particulars_stream_4 = multi_input_blank(request)
    projection_table.ins_particulars_total_revenue_from_operations_services = multi_input_blank(request)
    projection_table.ins_particulars_product_development_expenses_operating_expenses_raw_material = multi_input_blank(request)
    projection_table.ins_particulars_employee_cost = multi_input_blank(request)
    projection_table.ins_particulars_general_administrative_expenses = multi_input_blank(request)
    projection_table.ins_particulars_selling_marketing_expenses = multi_input_blank(request)
    projection_table.ins_particulars_other_expenses_1 = multi_input_blank(request)
    projection_table.ins_particulars_other_expenses_2 = multi_input_blank(request)
    projection_table.ins_particulars_total_operating_expenses = multi_input_blank(request)
    projection_table.ins_particulars_ebitda_operating_profit = multi_input_blank(request)
    projection_table.ins_particulars_depreciation = multi_input_blank(request)
    projection_table.ins_particulars_other_income = multi_input_blank(request)
    projection_table.ins_particulars_realised_foreign_exchange_gain_loss = multi_input_blank(request)
    projection_table.ins_particulars_ebit = multi_input_blank(request)
    projection_table.ins_particulars_interest_including_finance_charges = multi_input_blank(request)
    projection_table.ins_particulars_earnings_before_tax_ebt = multi_input_blank(request)
    projection_table.ins_particulars_provision_for_income_tax = multi_input_blank(request)
    projection_table.ins_particulars_profit_after_tax = multi_input_blank(request)
    projection_table.ins_particulars_ebitda_perc = multi_input_blank(request)
    projection_table.ins_particulars_pat_perc = multi_input_blank(request)
    projection_table.ins_particulars_interest_cover = multi_input_blank(request)
    projection_table.ins_particulars_financial_leverage = multi_input_blank(request)

    projection_table.ins_growth_analysis_yoy_stream_1 = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_stream_2 = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_stream_3 = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_stream_4 = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_total_revenue_from_operations_services = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_employee_cost = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_general_administrative_expenses = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_selling_marketing_expenses = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_other_expenses_1 = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_other_expenses_2 = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_total_operating_expenses = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_ebitda_operating_profit = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_depreciation = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_other_income = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_foreign_exchange_gain_loss = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_ebit = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_interest_including_finance_charges = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_earnings_before_tax_ebt = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_provision_for_income_tax = multi_input_blank(request)
    projection_table.ins_growth_analysis_yoy_profit_after_tax = multi_input_blank(request)

    projection_table.ins_analysis_as_of_revenue_stream_1 = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_stream_2 = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_stream_3 = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_stream_4 = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_total_revenue_from_operations_services = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_employee_cost = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_general_administrative_expenses = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_selling_marketing_expenses = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_other_expenses_1 = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_other_expenses_2 = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_total_operating_expenses = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_ebitda_operating_profit = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_depreciation = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_other_income = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_ebit = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_interest_including_finance_charges = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_earnings_before_tax_ebt = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_provision_for_income_tax = multi_input_blank(request)
    projection_table.ins_analysis_as_of_revenue_profit_after_tax = multi_input_blank(request)

    projection_table.save()
    return projection_table.id
    






def calculate_income_statement(request):                                      # Calculate the income statement

    if(auth_user(request)):
        book = super_plan_forms.objects.filter(id=request.session['form']).get()
        if(auth_user(request) and book ):

            projection_table1 = super_plan_projection.objects.filter(id=book.projection_table).get()

            projection_table1.ins_particulars_stream_1.f_1 = projection_table1.p_revenue_growth_or_amount_1.f_1
            projection_table1.ins_particulars_stream_1.f_2 = projection_table1.p_revenue_growth_or_amount_1.f_2
            projection_table1.ins_particulars_stream_1.f_3 = projection_table1.p_revenue_growth_or_amount_1.f_3
            projection_table1.ins_particulars_stream_1.f_4 = projection_table1.p_revenue_growth_or_amount_1.f_4
            projection_table1.ins_particulars_stream_1.f_5 = projection_table1.p_revenue_growth_or_amount_1.f_5
            





            projection_table1.ins_particulars_stream_2.f_1 = projection_table1.p_revenue_growth_or_amount_2.f_1
            projection_table1.ins_particulars_stream_2.f_2 = projection_table1.p_revenue_growth_or_amount_2.f_2
            projection_table1.ins_particulars_stream_2.f_3 = projection_table1.p_revenue_growth_or_amount_2.f_3
            projection_table1.ins_particulars_stream_2.f_4 = projection_table1.p_revenue_growth_or_amount_2.f_4
            projection_table1.ins_particulars_stream_2.f_5 = projection_table1.p_revenue_growth_or_amount_2.f_5
            





            projection_table1.ins_particulars_stream_3.f_1 = projection_table1.p_revenue_growth_or_amount_3.f_1
            projection_table1.ins_particulars_stream_3.f_2 = projection_table1.p_revenue_growth_or_amount_3.f_2
            projection_table1.ins_particulars_stream_3.f_3 = projection_table1.p_revenue_growth_or_amount_3.f_3
            projection_table1.ins_particulars_stream_3.f_4 = projection_table1.p_revenue_growth_or_amount_3.f_4
            projection_table1.ins_particulars_stream_3.f_5 = projection_table1.p_revenue_growth_or_amount_3.f_5
            


            projection_table1.ins_particulars_stream_4.f_1 = projection_table1.p_revenue_growth_or_amount_4.f_1
            projection_table1.ins_particulars_stream_4.f_2 = projection_table1.p_revenue_growth_or_amount_4.f_2
            projection_table1.ins_particulars_stream_4.f_3 = projection_table1.p_revenue_growth_or_amount_4.f_3
            projection_table1.ins_particulars_stream_4.f_4 = projection_table1.p_revenue_growth_or_amount_4.f_4
            projection_table1.ins_particulars_stream_4.f_5 = projection_table1.p_revenue_growth_or_amount_4.f_5
            

            projection_table1.ins_particulars_total_revenue_from_operations_services.f_1 = projection_table1.p_total_revenue_from_operations_services.f_1
            projection_table1.ins_particulars_total_revenue_from_operations_services.f_2 = projection_table1.p_total_revenue_from_operations_services.f_2
            projection_table1.ins_particulars_total_revenue_from_operations_services.f_3 = projection_table1.p_total_revenue_from_operations_services.f_3
            projection_table1.ins_particulars_total_revenue_from_operations_services.f_4 = projection_table1.p_total_revenue_from_operations_services.f_4
            projection_table1.ins_particulars_total_revenue_from_operations_services.f_5 = projection_table1.p_total_revenue_from_operations_services.f_5
            
            
            





            projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_1 = projection_table1.p_total_product_development_expenses_operating_expenses.f_1
            projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_2 = projection_table1.p_total_product_development_expenses_operating_expenses.f_2
            projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_3 = projection_table1.p_total_product_development_expenses_operating_expenses.f_3
            projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_4 = projection_table1.p_total_product_development_expenses_operating_expenses.f_4
            projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_5 = projection_table1.p_total_product_development_expenses_operating_expenses.f_5







            projection_table1.ins_particulars_employee_cost.f_1 =projection_table1.p_total_employee_expenses.f_1
            projection_table1.ins_particulars_employee_cost.f_2 =projection_table1.p_total_employee_expenses.f_2
            projection_table1.ins_particulars_employee_cost.f_3 =projection_table1.p_total_employee_expenses.f_3
            projection_table1.ins_particulars_employee_cost.f_4 =projection_table1.p_total_employee_expenses.f_4
            projection_table1.ins_particulars_employee_cost.f_5 =projection_table1.p_total_employee_expenses.f_5





            projection_table1.ins_particulars_general_administrative_expenses.f_1 = projection_table1.p_total_general_administrative_expenses.f_1
            projection_table1.ins_particulars_general_administrative_expenses.f_2 = projection_table1.p_total_general_administrative_expenses.f_2
            projection_table1.ins_particulars_general_administrative_expenses.f_3 = projection_table1.p_total_general_administrative_expenses.f_3
            projection_table1.ins_particulars_general_administrative_expenses.f_4 = projection_table1.p_total_general_administrative_expenses.f_4
            projection_table1.ins_particulars_general_administrative_expenses.f_5 = projection_table1.p_total_general_administrative_expenses.f_5



            projection_table1.ins_particulars_selling_marketing_expenses.f_1 = projection_table1.p_total_selling_marketing_expenses.f_1
            projection_table1.ins_particulars_selling_marketing_expenses.f_2 = projection_table1.p_total_selling_marketing_expenses.f_2
            projection_table1.ins_particulars_selling_marketing_expenses.f_3 = projection_table1.p_total_selling_marketing_expenses.f_3
            projection_table1.ins_particulars_selling_marketing_expenses.f_4 = projection_table1.p_total_selling_marketing_expenses.f_4
            projection_table1.ins_particulars_selling_marketing_expenses.f_5 = projection_table1.p_total_selling_marketing_expenses.f_5


            projection_table1.ins_particulars_other_expenses_1.f_1 = projection_table1.p_other_expenses_1.f_1
            projection_table1.ins_particulars_other_expenses_1.f_2 = projection_table1.p_other_expenses_1.f_2
            projection_table1.ins_particulars_other_expenses_1.f_3 = projection_table1.p_other_expenses_1.f_3
            projection_table1.ins_particulars_other_expenses_1.f_4 = projection_table1.p_other_expenses_1.f_4
            projection_table1.ins_particulars_other_expenses_1.f_5 = projection_table1.p_other_expenses_1.f_5



            projection_table1.ins_particulars_other_expenses_2.f_1 = projection_table1.p_other_expenses_2.f_1
            projection_table1.ins_particulars_other_expenses_2.f_2 = projection_table1.p_other_expenses_2.f_2
            projection_table1.ins_particulars_other_expenses_2.f_3 = projection_table1.p_other_expenses_2.f_3
            projection_table1.ins_particulars_other_expenses_2.f_4 = projection_table1.p_other_expenses_2.f_4
            projection_table1.ins_particulars_other_expenses_2.f_5 = projection_table1.p_other_expenses_2.f_5

            


           
            try:
                projection_table1.ins_particulars_total_operating_expenses.f_1 =ceil(float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_1) + float(projection_table1.ins_particulars_employee_cost.f_1) + float(projection_table1.ins_particulars_general_administrative_expenses.f_1) + float(projection_table1.ins_particulars_selling_marketing_expenses.f_1) + float(projection_table1.ins_particulars_other_expenses_1.f_1) + float(projection_table1.ins_particulars_other_expenses_2.f_1))
            except:
                projection_table1.ins_particulars_total_operating_expenses.f_1 =None

            try:
                projection_table1.ins_particulars_total_operating_expenses.f_2 =ceil(float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_2) + float(projection_table1.ins_particulars_employee_cost.f_2) + float(projection_table1.ins_particulars_general_administrative_expenses.f_2) + float(projection_table1.ins_particulars_selling_marketing_expenses.f_2) + float(projection_table1.ins_particulars_other_expenses_1.f_2) + float(projection_table1.ins_particulars_other_expenses_2.f_2))
            except:
                projection_table1.ins_particulars_total_operating_expenses.f_2 =None

            try:
                projection_table1.ins_particulars_total_operating_expenses.f_3 =ceil(float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_3) + float(projection_table1.ins_particulars_employee_cost.f_3) + float(projection_table1.ins_particulars_general_administrative_expenses.f_3) + float(projection_table1.ins_particulars_selling_marketing_expenses.f_3) + float(projection_table1.ins_particulars_other_expenses_1.f_3) + float(projection_table1.ins_particulars_other_expenses_2.f_3))
            except:
                projection_table1.ins_particulars_total_operating_expenses.f_3 =None



            try:
                projection_table1.ins_particulars_total_operating_expenses.f_4 =ceil(float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_4) + float(projection_table1.ins_particulars_employee_cost.f_4) + float(projection_table1.ins_particulars_general_administrative_expenses.f_4) + float(projection_table1.ins_particulars_selling_marketing_expenses.f_4) + float(projection_table1.ins_particulars_other_expenses_1.f_4) + float(projection_table1.ins_particulars_other_expenses_2.f_4))
            except:
                projection_table1.ins_particulars_total_operating_expenses.f_4 =None

            try:
                projection_table1.ins_particulars_total_operating_expenses.f_5 =ceil(float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_5) + float(projection_table1.ins_particulars_employee_cost.f_5) + float(projection_table1.ins_particulars_general_administrative_expenses.f_5) + float(projection_table1.ins_particulars_selling_marketing_expenses.f_5) + float(projection_table1.ins_particulars_other_expenses_1.f_5) + float(projection_table1.ins_particulars_other_expenses_2.f_5))
            except:
                projection_table1.ins_particulars_total_operating_expenses.f_5 =None








            try:
                projection_table1.ins_particulars_ebitda_operating_profit.f_1 = ceil(float(projection_table1.ins_particulars_total_operating_expenses.f_1) - float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))
            except:
                projection_table1.ins_particulars_ebitda_operating_profit.f_1 = None

            try:
                projection_table1.ins_particulars_ebitda_operating_profit.f_2 = ceil(float(projection_table1.ins_particulars_total_operating_expenses.f_2) - float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))
            except:
                projection_table1.ins_particulars_ebitda_operating_profit.f_2 = None

            try:
                projection_table1.ins_particulars_ebitda_operating_profit.f_3 = ceil(float(projection_table1.ins_particulars_total_operating_expenses.f_3) - float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))
            except:
                projection_table1.ins_particulars_ebitda_operating_profit.f_3 = None


            try:
                projection_table1.ins_particulars_ebitda_operating_profit.f_4 = ceil(float(projection_table1.ins_particulars_total_operating_expenses.f_4) - float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))
            except:
                projection_table1.ins_particulars_ebitda_operating_profit.f_4 = None


            try:
                projection_table1.ins_particulars_ebitda_operating_profit.f_5 = ceil(float(projection_table1.ins_particulars_total_operating_expenses.f_5) - float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))
            except:
                projection_table1.ins_particulars_ebitda_operating_profit.f_5 = None



            projection_table1.ins_particulars_depreciation = projection_table1.p_current_depreciation

            projection_table1.ins_particulars_other_income = projection_table1.p_other_income_growth_or_amount

            projection_table1.ins_particulars_realised_foreign_exchange_gain_loss = projection_table1.p_realised_foreign_exchange_gain_or_loss


            try:
                projection_table1.ins_particulars_ebit.f_1 = ceil(float(projection_table1.ins_particulars_ebitda_operating_profit.f_1) - (float(projection_table1.ins_particulars_depreciation.f_1)+float(projection_table1.ins_particulars_other_income.f_1)+float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_1)))
            except:
                projection_table1.ins_particulars_ebit.f_1 = None


            try:
                projection_table1.ins_particulars_ebit.f_2 = ceil(float(projection_table1.ins_particulars_ebitda_operating_profit.f_2) - (float(projection_table1.ins_particulars_depreciation.f_2)+float(projection_table1.ins_particulars_other_income.f_2)+float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_2)))
            except:
                projection_table1.ins_particulars_ebit.f_2 = None

            try:
                projection_table1.ins_particulars_ebit.f_3 = ceil(float(projection_table1.ins_particulars_ebitda_operating_profit.f_3) - (float(projection_table1.ins_particulars_depreciation.f_3)+float(projection_table1.ins_particulars_other_income.f_3)+float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_3)))
            except:
                projection_table1.ins_particulars_ebit.f_3 = None

            try:
                projection_table1.ins_particulars_ebit.f_4 = ceil(float(projection_table1.ins_particulars_ebitda_operating_profit.f_4) - (float(projection_table1.ins_particulars_depreciation.f_4)+float(projection_table1.ins_particulars_other_income.f_4)+float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_4)))
            except:
                projection_table1.ins_particulars_ebit.f_4 = None

            try:
                projection_table1.ins_particulars_ebit.f_5 = ceil(float(projection_table1.ins_particulars_ebitda_operating_profit.f_5) - (float(projection_table1.ins_particulars_depreciation.f_5)+float(projection_table1.ins_particulars_other_income.f_5)+float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_5)))
            except:
                projection_table1.ins_particulars_ebit.f_5 = None


            projection_table1.ins_particulars_interest_including_finance_charges.f_1=0
            projection_table1.ins_particulars_interest_including_finance_charges.f_2=0
            projection_table1.ins_particulars_interest_including_finance_charges.f_3=0
            projection_table1.ins_particulars_interest_including_finance_charges.f_4=0
            projection_table1.ins_particulars_interest_including_finance_charges.f_5=0



            try:
                projection_table1.ins_particulars_earnings_before_tax_ebt.f_1 = ceil( float(projection_table1.ins_particulars_ebit.f_1)-float(projection_table1.ins_particulars_interest_including_finance_charges.f_1))
            except:
                projection_table1.ins_particulars_earnings_before_tax_ebt.f_1 = 0

            try:
                projection_table1.ins_particulars_earnings_before_tax_ebt.f_2 = ceil( float(projection_table1.ins_particulars_ebit.f_2)-float(projection_table1.ins_particulars_interest_including_finance_charges.f_2))
            except:
                projection_table1.ins_particulars_earnings_before_tax_ebt.f_2 = 0

            try:
                projection_table1.ins_particulars_earnings_before_tax_ebt.f_3 = ceil( float(projection_table1.ins_particulars_ebit.f_3)-float(projection_table1.ins_particulars_interest_including_finance_charges.f_3))
            except:
                projection_table1.ins_particulars_earnings_before_tax_ebt.f_3 = 0

            try:
                projection_table1.ins_particulars_earnings_before_tax_ebt.f_4 = ceil( float(projection_table1.ins_particulars_ebit.f_4)-float(projection_table1.ins_particulars_interest_including_finance_charges.f_4))
            except:
                projection_table1.ins_particulars_earnings_before_tax_ebt.f_4 = 0

            try:
                projection_table1.ins_particulars_earnings_before_tax_ebt.f_5 = ceil( float(projection_table1.ins_particulars_ebit.f_5)-float(projection_table1.ins_particulars_interest_including_finance_charges.f_5))
            except:
                projection_table1.ins_particulars_earnings_before_tax_ebt.f_5 = 0







            try:
                projection_table1.ins_particulars_provision_for_income_tax.f_1 = ceil(float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_1)*float(projection_table1.p_income_tax_rate.f_1))
            except:
                 projection_table1.ins_particulars_provision_for_income_tax.f_1 = 0

            try:
                projection_table1.ins_particulars_provision_for_income_tax.f_2 = ceil(float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_2)*float(projection_table1.p_income_tax_rate.f_2))
            except:
                 projection_table1.ins_particulars_provision_for_income_tax.f_2 = 0

            try:
                projection_table1.ins_particulars_provision_for_income_tax.f_3 = ceil(float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_3)*float(projection_table1.p_income_tax_rate.f_3))
            except:
                 projection_table1.ins_particulars_provision_for_income_tax.f_3 = 0


            try:
                projection_table1.ins_particulars_provision_for_income_tax.f_4 = ceil(float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_4)*float(projection_table1.p_income_tax_rate.f_4))
            except:
                 projection_table1.ins_particulars_provision_for_income_tax.f_4 = 0


            try:
                projection_table1.ins_particulars_provision_for_income_tax.f_5 = ceil(float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_5)*float(projection_table1.p_income_tax_rate.f_5))
            except:
                 projection_table1.ins_particulars_provision_for_income_tax.f_5 = 0





            



            try:
                projection_table1.ins_particulars_profit_after_tax.f_1 = ceil(float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_1)-float(projection_table1.ins_particulars_provision_for_income_tax.f_1))
            except:
                projection_table1.ins_particulars_profit_after_tax.f_1 =0


            try:
                projection_table1.ins_particulars_profit_after_tax.f_2 = ceil(float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_2)-float(projection_table1.ins_particulars_provision_for_income_tax.f_2))
            except:
                projection_table1.ins_particulars_profit_after_tax.f_2 =0


            try:
                projection_table1.ins_particulars_profit_after_tax.f_3 = ceil(float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_3)-float(projection_table1.ins_particulars_provision_for_income_tax.f_3))
            except:
                projection_table1.ins_particulars_profit_after_tax.f_3 =0

            try:
                projection_table1.ins_particulars_profit_after_tax.f_4 = ceil(float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_4)-float(projection_table1.ins_particulars_provision_for_income_tax.f_4))
            except:
                projection_table1.ins_particulars_profit_after_tax.f_4 =0

            try:
                projection_table1.ins_particulars_profit_after_tax.f_5 = ceil(float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_5)-float(projection_table1.ins_particulars_provision_for_income_tax.f_5))
            except:
                projection_table1.ins_particulars_profit_after_tax.f_5 =0







            try:
                projection_table1.ins_particulars_ebitda_perc.f_1 = ceil(float(projection_table1.ins_particulars_ebitda_operating_profit.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))
            except:
                projection_table1.ins_particulars_ebitda_perc.f_1 = 0

            try:
                projection_table1.ins_particulars_ebitda_perc.f_2 = ceil(float(projection_table1.ins_particulars_ebitda_operating_profit.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))
            except:
                projection_table1.ins_particulars_ebitda_perc.f_2 = 0

            try:
                projection_table1.ins_particulars_ebitda_perc.f_3 = ceil(float(projection_table1.ins_particulars_ebitda_operating_profit.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))
            except:
                projection_table1.ins_particulars_ebitda_perc.f_3 = 0

            try:
                projection_table1.ins_particulars_ebitda_perc.f_4 = ceil(float(projection_table1.ins_particulars_ebitda_operating_profit.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))
            except:
                projection_table1.ins_particulars_ebitda_perc.f_4 = 0

            try:
                projection_table1.ins_particulars_ebitda_perc.f_5 = ceil(float(projection_table1.ins_particulars_ebitda_operating_profit.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))
            except:
                projection_table1.ins_particulars_ebitda_perc.f_5 = 0







            try:
                projection_table1.ins_particulars_pat_perc.f_1 = ceil(float(projection_table1.ins_particulars_profit_after_tax.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))
            except:
                projection_table1.ins_particulars_pat_perc.f_1 = 0

            try:
                projection_table1.ins_particulars_pat_perc.f_2 = ceil(float(projection_table1.ins_particulars_profit_after_tax.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))
            except:
                projection_table1.ins_particulars_pat_perc.f_2 = 0

            try:
                projection_table1.ins_particulars_pat_perc.f_3 = ceil(float(projection_table1.ins_particulars_profit_after_tax.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))
            except:
                projection_table1.ins_particulars_pat_perc.f_3 = 0

            try:
                projection_table1.ins_particulars_pat_perc.f_4 = ceil(float(projection_table1.ins_particulars_profit_after_tax.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))
            except:
                projection_table1.ins_particulars_pat_perc.f_4 = 0

            try:
                projection_table1.ins_particulars_pat_perc.f_5 = ceil(float(projection_table1.ins_particulars_profit_after_tax.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))
            except:
                projection_table1.ins_particulars_pat_perc.f_5 = 0








            try:
                projection_table1.ins_particulars_interest_cover.f_1=ceil(float(projection_table1.ins_particulars_ebit.f_1)/float(projection_table1.ins_particulars_interest_including_finance_charges.f_1))
            except:
                projection_table1.ins_particulars_interest_cover.f_1=0

            try:
                projection_table1.ins_particulars_interest_cover.f_2=ceil(float(projection_table1.ins_particulars_ebit.f_2)/float(projection_table1.ins_particulars_interest_including_finance_charges.f_2))
            except:
                projection_table1.ins_particulars_interest_cover.f_2=0

            try:
                projection_table1.ins_particulars_interest_cover.f_3=ceil(float(projection_table1.ins_particulars_ebit.f_3)/float(projection_table1.ins_particulars_interest_including_finance_charges.f_3))
            except:
                projection_table1.ins_particulars_interest_cover.f_3=0

            try:
                projection_table1.ins_particulars_interest_cover.f_4=ceil(float(projection_table1.ins_particulars_ebit.f_4)/float(projection_table1.ins_particulars_interest_including_finance_charges.f_4))
            except:
                projection_table1.ins_particulars_interest_cover.f_4=0

            try:
                projection_table1.ins_particulars_interest_cover.f_5=ceil(float(projection_table1.ins_particulars_ebit.f_5)/float(projection_table1.ins_particulars_interest_including_finance_charges.f_5))
            except:
                projection_table1.ins_particulars_interest_cover.f_5=0

            











            try:
                projection_table1.ins_particulars_financial_leverage.f_1=ceil(float(projection_table1.ins_particulars_ebit.f_1)/float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_1))
            except:
                projection_table1.ins_particulars_financial_leverage.f_1=0

            try:
                projection_table1.ins_particulars_financial_leverage.f_2=ceil(float(projection_table1.ins_particulars_ebit.f_2)/float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_2))
            except:
                projection_table1.ins_particulars_financial_leverage.f_2=0


            try:
                projection_table1.ins_particulars_financial_leverage.f_3=ceil(float(projection_table1.ins_particulars_ebit.f_3)/float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_3))
            except:
                projection_table1.ins_particulars_financial_leverage.f_3=0

            try:
                projection_table1.ins_particulars_financial_leverage.f_4=ceil(float(projection_table1.ins_particulars_ebit.f_4)/float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_4))
            except:
                projection_table1.ins_particulars_financial_leverage.f_4=0

            try:
                projection_table1.ins_particulars_financial_leverage.f_5=ceil(float(projection_table1.ins_particulars_ebit.f_5)/float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_5))
            except:
                projection_table1.ins_particulars_financial_leverage.f_5=0

















                        #----------------------------
            
            try:
                projection_table1.ins_growth_analysis_yoy_stream_1.f_2=ceil(((float(projection_table1.ins_particulars_stream_1.f_2)-float(projection_table1.ins_particulars_stream_1.f_1))/float(projection_table1.ins_particulars_stream_1.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_1.f_2=0
            try:
                projection_table1.ins_growth_analysis_yoy_stream_1.f_3=ceil(((float(projection_table1.ins_particulars_stream_1.f_3)-float(projection_table1.ins_particulars_stream_1.f_2))/float(projection_table1.ins_particulars_stream_1.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_1.f_3=0
            try:
                projection_table1.ins_growth_analysis_yoy_stream_1.f_4=ceil(((float(projection_table1.ins_particulars_stream_1.f_4)-float(projection_table1.ins_particulars_stream_1.f_3))/float(projection_table1.ins_particulars_stream_1.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_1.f_4=0
            try:
                projection_table1.ins_growth_analysis_yoy_stream_1.f_5=ceil(((float(projection_table1.ins_particulars_stream_1.f_5)-float(projection_table1.ins_particulars_stream_1.f_4))/float(projection_table1.ins_particulars_stream_1.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_1.f_5=0










            try:
                projection_table1.ins_growth_analysis_yoy_stream_2.f_2=ceil(((float(projection_table1.ins_particulars_stream_2.f_2)-float(projection_table1.ins_particulars_stream_2.f_1))/float(projection_table1.ins_particulars_stream_2.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_2.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_stream_2.f_3=ceil(((float(projection_table1.ins_particulars_stream_2.f_3)-float(projection_table1.ins_particulars_stream_2.f_2))/float(projection_table1.ins_particulars_stream_2.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_2.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_stream_2.f_4=ceil(((float(projection_table1.ins_particulars_stream_2.f_4)-float(projection_table1.ins_particulars_stream_2.f_3))/float(projection_table1.ins_particulars_stream_2.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_2.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_stream_2.f_5=ceil(((float(projection_table1.ins_particulars_stream_2.f_5)-float(projection_table1.ins_particulars_stream_2.f_4))/float(projection_table1.ins_particulars_stream_2.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_2.f_5=0



            




            try:
                projection_table1.ins_growth_analysis_yoy_stream_3.f_2=ceil(((float(projection_table1.ins_particulars_stream_3.f_2)-float(projection_table1.ins_particulars_stream_3.f_1))/float(projection_table1.ins_particulars_stream_3.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_3.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_stream_3.f_3=ceil(((float(projection_table1.ins_particulars_stream_3.f_3)-float(projection_table1.ins_particulars_stream_3.f_2))/float(projection_table1.ins_particulars_stream_3.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_3.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_stream_3.f_4=ceil(((float(projection_table1.ins_particulars_stream_3.f_4)-float(projection_table1.ins_particulars_stream_3.f_3))/float(projection_table1.ins_particulars_stream_3.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_3.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_stream_3.f_5=ceil(((float(projection_table1.ins_particulars_stream_3.f_5)-float(projection_table1.ins_particulars_stream_3.f_4))/float(projection_table1.ins_particulars_stream_3.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_3.f_5=0






        


            try:
                projection_table1.ins_growth_analysis_yoy_stream_4.f_2=ceil(((float(projection_table1.ins_particulars_stream_4.f_2)-float(projection_table1.ins_particulars_stream_4.f_1))/float(projection_table1.ins_particulars_stream_4.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_4.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_stream_4.f_3=ceil(((float(projection_table1.ins_particulars_stream_4.f_3)-float(projection_table1.ins_particulars_stream_4.f_2))/float(projection_table1.ins_particulars_stream_4.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_4.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_stream_4.f_4=ceil(((float(projection_table1.ins_particulars_stream_4.f_4)-float(projection_table1.ins_particulars_stream_4.f_3))/float(projection_table1.ins_particulars_stream_4.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_4.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_stream_4.f_5=ceil(((float(projection_table1.ins_particulars_stream_4.f_5)-float(projection_table1.ins_particulars_stream_4.f_4))/float(projection_table1.ins_particulars_stream_4.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_stream_4.f_5=0
             






            try:
                projection_table1.ins_growth_analysis_yoy_total_revenue_from_operations_services.f_2=ceil(((float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2)-float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_total_revenue_from_operations_services.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_total_revenue_from_operations_services.f_3=ceil(((float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3)-float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_total_revenue_from_operations_services.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_total_revenue_from_operations_services.f_4=ceil(((float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4)-float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_total_revenue_from_operations_services.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_total_revenue_from_operations_services.f_5=ceil(((float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5)-float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_total_revenue_from_operations_services.f_5=0
             
            

















            try:
                projection_table1.ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material.f_2=ceil(((float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_2)-float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_1))/float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material.f_3=ceil(((float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_3)-float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_2))/float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material.f_4=ceil(((float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_4)-float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_3))/float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material.f_5=ceil(((float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_5)-float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_4))/float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_product_development_expenses_operating_expenses_raw_material.f_5=0
             









            try:
                projection_table1.ins_growth_analysis_yoy_employee_cost.f_2=ceil(((float(projection_table1.ins_particulars_employee_cost.f_2)-float(projection_table1.ins_particulars_employee_cost.f_1))/float(projection_table1.ins_particulars_employee_cost.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_employee_cost.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_employee_cost.f_3=ceil(((float(projection_table1.ins_particulars_employee_cost.f_3)-float(projection_table1.ins_particulars_employee_cost.f_2))/float(projection_table1.ins_particulars_employee_cost.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_employee_cost.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_employee_cost.f_4=ceil(((float(projection_table1.ins_particulars_employee_cost.f_4)-float(projection_table1.ins_particulars_employee_cost.f_3))/float(projection_table1.ins_particulars_employee_cost.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_employee_cost.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_employee_cost.f_5=ceil(((float(projection_table1.ins_particulars_employee_cost.f_5)-float(projection_table1.ins_particulars_employee_cost.f_4))/float(projection_table1.ins_particulars_employee_cost.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_employee_cost.f_5=0
             








            try:
                projection_table1.ins_growth_analysis_yoy_general_administrative_expenses.f_2=ceil(((float(projection_table1.ins_particulars_general_administrative_expenses.f_2)-float(projection_table1.ins_particulars_general_administrative_expenses.f_1))/float(projection_table1.ins_particulars_general_administrative_expenses.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_general_administrative_expenses.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_general_administrative_expenses.f_3=ceil(((float(projection_table1.ins_particulars_general_administrative_expenses.f_3)-float(projection_table1.ins_particulars_general_administrative_expenses.f_2))/float(projection_table1.ins_particulars_general_administrative_expenses.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_general_administrative_expenses.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_general_administrative_expenses.f_4=ceil(((float(projection_table1.ins_particulars_general_administrative_expenses.f_4)-float(projection_table1.ins_particulars_general_administrative_expenses.f_3))/float(projection_table1.ins_particulars_general_administrative_expenses.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_general_administrative_expenses.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_general_administrative_expenses.f_5=ceil(((float(projection_table1.ins_particulars_general_administrative_expenses.f_5)-float(projection_table1.ins_particulars_general_administrative_expenses.f_4))/float(projection_table1.ins_particulars_general_administrative_expenses.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_general_administrative_expenses.f_5=0









            try:
                projection_table1.ins_growth_analysis_yoy_selling_marketing_expenses.f_2=ceil(((float(projection_table1.ins_particulars_selling_marketing_expenses.f_2)-float(projection_table1.ins_particulars_selling_marketing_expenses.f_1))/float(projection_table1.ins_particulars_selling_marketing_expenses.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_selling_marketing_expenses.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_selling_marketing_expenses.f_3=ceil(((float(projection_table1.ins_particulars_selling_marketing_expenses.f_3)-float(projection_table1.ins_particulars_selling_marketing_expenses.f_2))/float(projection_table1.ins_particulars_selling_marketing_expenses.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_selling_marketing_expenses.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_selling_marketing_expenses.f_4=ceil(((float(projection_table1.ins_particulars_selling_marketing_expenses.f_4)-float(projection_table1.ins_particulars_selling_marketing_expenses.f_3))/float(projection_table1.ins_particulars_selling_marketing_expenses.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_selling_marketing_expenses.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_selling_marketing_expenses.f_5=ceil(((float(projection_table1.ins_particulars_selling_marketing_expenses.f_5)-float(projection_table1.ins_particulars_selling_marketing_expenses.f_4))/float(projection_table1.ins_particulars_selling_marketing_expenses.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_selling_marketing_expenses.f_5=0
             









            try:
                projection_table1.ins_growth_analysis_yoy_other_expenses_1.f_2=ceil(((float(projection_table1.ins_particulars_other_expenses_1.f_2)-float(projection_table1.ins_particulars_other_expenses_1.f_1))/float(projection_table1.ins_particulars_other_expenses_1.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_expenses_1.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_other_expenses_1.f_3=ceil(((float(projection_table1.ins_particulars_other_expenses_1.f_3)-float(projection_table1.ins_particulars_other_expenses_1.f_2))/float(projection_table1.ins_particulars_other_expenses_1.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_expenses_1.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_other_expenses_1.f_4=ceil(((float(projection_table1.ins_particulars_other_expenses_1.f_4)-float(projection_table1.ins_particulars_other_expenses_1.f_3))/float(projection_table1.ins_particulars_other_expenses_1.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_expenses_1.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_other_expenses_1.f_5=ceil(((float(projection_table1.ins_particulars_other_expenses_1.f_5)-float(projection_table1.ins_particulars_other_expenses_1.f_4))/float(projection_table1.ins_particulars_other_expenses_1.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_expenses_1.f_5=0














            try:
                projection_table1.ins_growth_analysis_yoy_other_expenses_2.f_2=ceil(((float(projection_table1.ins_particulars_other_expenses_2.f_2)-float(projection_table1.ins_particulars_other_expenses_2.f_1))/float(projection_table1.ins_particulars_other_expenses_2.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_expenses_2.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_other_expenses_2.f_3=ceil(((float(projection_table1.ins_particulars_other_expenses_2.f_3)-float(projection_table1.ins_particulars_other_expenses_2.f_2))/float(projection_table1.ins_particulars_other_expenses_2.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_expenses_2.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_other_expenses_2.f_4=ceil(((float(projection_table1.ins_particulars_other_expenses_2.f_4)-float(projection_table1.ins_particulars_other_expenses_2.f_3))/float(projection_table1.ins_particulars_other_expenses_2.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_expenses_2.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_other_expenses_2.f_5=ceil(((float(projection_table1.ins_particulars_other_expenses_2.f_5)-float(projection_table1.ins_particulars_other_expenses_2.f_4))/float(projection_table1.ins_particulars_other_expenses_2.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_expenses_2.f_5=0
             













            try:
                projection_table1.ins_growth_analysis_yoy_total_operating_expenses.f_2=ceil(((float(projection_table1.ins_particulars_total_operating_expenses.f_2)-float(projection_table1.ins_particulars_total_operating_expenses.f_1))/float(projection_table1.ins_particulars_total_operating_expenses.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_total_operating_expenses.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_total_operating_expenses.f_3=ceil(((float(projection_table1.ins_particulars_total_operating_expenses.f_3)-float(projection_table1.ins_particulars_total_operating_expenses.f_2))/float(projection_table1.ins_particulars_total_operating_expenses.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_total_operating_expenses.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_total_operating_expenses.f_4=ceil(((float(projection_table1.ins_particulars_total_operating_expenses.f_4)-float(projection_table1.ins_particulars_total_operating_expenses.f_3))/float(projection_table1.ins_particulars_total_operating_expenses.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_total_operating_expenses.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_total_operating_expenses.f_5=ceil(((float(projection_table1.ins_particulars_total_operating_expenses.f_5)-float(projection_table1.ins_particulars_total_operating_expenses.f_4))/float(projection_table1.ins_particulars_total_operating_expenses.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_total_operating_expenses.f_5=0










            try:
                projection_table1.ins_growth_analysis_yoy_ebitda_operating_profit.f_2=ceil(((float(projection_table1.ins_particulars_ebitda_operating_profit.f_2)-float(projection_table1.ins_particulars_ebitda_operating_profit.f_1))/float(projection_table1.ins_particulars_ebitda_operating_profit.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_ebitda_operating_profit.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_ebitda_operating_profit.f_3=ceil(((float(projection_table1.ins_particulars_ebitda_operating_profit.f_3)-float(projection_table1.ins_particulars_ebitda_operating_profit.f_2))/float(projection_table1.ins_particulars_ebitda_operating_profit.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_ebitda_operating_profit.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_ebitda_operating_profit.f_4=ceil(((float(projection_table1.ins_particulars_ebitda_operating_profit.f_4)-float(projection_table1.ins_particulars_ebitda_operating_profit.f_3))/float(projection_table1.ins_particulars_ebitda_operating_profit.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_ebitda_operating_profit.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_ebitda_operating_profit.f_5=ceil(((float(projection_table1.ins_particulars_ebitda_operating_profit.f_5)-float(projection_table1.ins_particulars_ebitda_operating_profit.f_4))/float(projection_table1.ins_particulars_ebitda_operating_profit.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_ebitda_operating_profit.f_5=0











            try:
                projection_table1.ins_growth_analysis_yoy_depreciation.f_2=ceil(((float(projection_table1.ins_particulars_depreciation.f_2)-float(projection_table1.ins_particulars_depreciation.f_1))/float(projection_table1.ins_particulars_depreciation.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_depreciation.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_depreciation.f_3=ceil(((float(projection_table1.ins_particulars_depreciation.f_3)-float(projection_table1.ins_particulars_depreciation.f_2))/float(projection_table1.ins_particulars_depreciation.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_depreciation.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_depreciation.f_4=ceil(((float(projection_table1.ins_particulars_depreciation.f_4)-float(projection_table1.ins_particulars_depreciation.f_3))/float(projection_table1.ins_particulars_depreciation.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_depreciation.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_depreciation.f_5=ceil(((float(projection_table1.ins_particulars_depreciation.f_5)-float(projection_table1.ins_particulars_depreciation.f_4))/float(projection_table1.ins_particulars_depreciation.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_depreciation.f_5=0










            try:
                projection_table1.ins_growth_analysis_yoy_other_income.f_2=ceil(((float(projection_table1.ins_particulars_other_income.f_2)-float(projection_table1.ins_particulars_other_income.f_1))/float(projection_table1.ins_particulars_other_income.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_income.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_other_income.f_3=ceil(((float(projection_table1.ins_particulars_other_income.f_3)-float(projection_table1.ins_particulars_other_income.f_2))/float(projection_table1.ins_particulars_other_income.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_income.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_other_income.f_4=ceil(((float(projection_table1.ins_particulars_other_income.f_4)-float(projection_table1.ins_particulars_other_income.f_3))/float(projection_table1.ins_particulars_other_income.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_income.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_other_income.f_5=ceil(((float(projection_table1.ins_particulars_other_income.f_5)-float(projection_table1.ins_particulars_other_income.f_4))/float(projection_table1.ins_particulars_other_income.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_other_income.f_5=0













            try:
                projection_table1.ins_growth_analysis_yoy_foreign_exchange_gain_loss.f_2=ceil(((float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_2)-float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_1))/float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_foreign_exchange_gain_loss.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_foreign_exchange_gain_loss.f_3=ceil(((float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_3)-float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_2))/float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_foreign_exchange_gain_loss.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_foreign_exchange_gain_loss.f_4=ceil(((float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_4)-float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_3))/float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_foreign_exchange_gain_loss.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_foreign_exchange_gain_loss.f_5=ceil(((float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_5)-float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_4))/float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_foreign_exchange_gain_loss.f_5=0











            try:
                projection_table1.ins_growth_analysis_yoy_ebit.f_2=ceil(((float(projection_table1.ins_particulars_ebit.f_2)-float(projection_table1.ins_particulars_ebit.f_1))/float(projection_table1.ins_particulars_ebit.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_ebit.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_ebit.f_3=ceil(((float(projection_table1.ins_particulars_ebit.f_3)-float(projection_table1.ins_particulars_ebit.f_2))/float(projection_table1.ins_particulars_ebit.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_ebit.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_ebit.f_4=ceil(((float(projection_table1.ins_particulars_ebit.f_4)-float(projection_table1.ins_particulars_ebit.f_3))/float(projection_table1.ins_particulars_ebit.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_ebit.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_ebit.f_5=ceil(((float(projection_table1.ins_particulars_ebit.f_5)-float(projection_table1.ins_particulars_ebit.f_4))/float(projection_table1.ins_particulars_ebit.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_ebit.f_5=0









            try:
                projection_table1.ins_growth_analysis_yoy_interest_including_finance_charges.f_2=ceil(((float(projection_table1.ins_particulars_interest_including_finance_charges.f_2)-float(projection_table1.ins_particulars_interest_including_finance_charges.f_1))/float(projection_table1.ins_particulars_interest_including_finance_charges.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_interest_including_finance_charges.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_interest_including_finance_charges.f_3=ceil(((float(projection_table1.ins_particulars_interest_including_finance_charges.f_3)-float(projection_table1.ins_particulars_interest_including_finance_charges.f_2))/float(projection_table1.ins_particulars_interest_including_finance_charges.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_interest_including_finance_charges.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_interest_including_finance_charges.f_4=ceil(((float(projection_table1.ins_particulars_interest_including_finance_charges.f_4)-float(projection_table1.ins_particulars_interest_including_finance_charges.f_3))/float(projection_table1.ins_particulars_interest_including_finance_charges.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_interest_including_finance_charges.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_interest_including_finance_charges.f_5=ceil(((float(projection_table1.ins_particulars_interest_including_finance_charges.f_5)-float(projection_table1.ins_particulars_interest_including_finance_charges.f_4))/float(projection_table1.ins_particulars_interest_including_finance_charges.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_interest_including_finance_charges.f_5=0










            try:
                projection_table1.ins_growth_analysis_yoy_earnings_before_tax_ebt.f_2=ceil(((float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_2)-float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_1))/float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_earnings_before_tax_ebt.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_earnings_before_tax_ebt.f_3=ceil(((float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_3)-float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_2))/float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_earnings_before_tax_ebt.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_earnings_before_tax_ebt.f_4=ceil(((float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_4)-float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_3))/float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_earnings_before_tax_ebt.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_earnings_before_tax_ebt.f_5=ceil(((float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_5)-float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_4))/float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_earnings_before_tax_ebt.f_5=0







            try:
                projection_table1.ins_growth_analysis_yoy_provision_for_income_tax.f_2=ceil(((float(projection_table1.ins_particulars_provision_for_income_tax.f_2)-float(projection_table1.ins_particulars_provision_for_income_tax.f_1))/float(projection_table1.ins_particulars_provision_for_income_tax.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_provision_for_income_tax.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_provision_for_income_tax.f_3=ceil(((float(projection_table1.ins_particulars_provision_for_income_tax.f_3)-float(projection_table1.ins_particulars_provision_for_income_tax.f_2))/float(projection_table1.ins_particulars_provision_for_income_tax.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_provision_for_income_tax.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_provision_for_income_tax.f_4=ceil(((float(projection_table1.ins_particulars_provision_for_income_tax.f_4)-float(projection_table1.ins_particulars_provision_for_income_tax.f_3))/float(projection_table1.ins_particulars_provision_for_income_tax.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_provision_for_income_tax.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_provision_for_income_tax.f_5=ceil(((float(projection_table1.ins_particulars_provision_for_income_tax.f_5)-float(projection_table1.ins_particulars_provision_for_income_tax.f_4))/float(projection_table1.ins_particulars_provision_for_income_tax.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_provision_for_income_tax.f_5=0











            try:
                projection_table1.ins_growth_analysis_yoy_profit_after_tax.f_2=ceil(((float(projection_table1.ins_particulars_profit_after_tax.f_2)-float(projection_table1.ins_particulars_profit_after_tax.f_1))/float(projection_table1.ins_particulars_profit_after_tax.f_1))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_profit_after_tax.f_2=0

            try:
                projection_table1.ins_growth_analysis_yoy_profit_after_tax.f_3=ceil(((float(projection_table1.ins_particulars_profit_after_tax.f_3)-float(projection_table1.ins_particulars_profit_after_tax.f_2))/float(projection_table1.ins_particulars_profit_after_tax.f_2))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_profit_after_tax.f_3=0

            try:
                projection_table1.ins_growth_analysis_yoy_profit_after_tax.f_4=ceil(((float(projection_table1.ins_particulars_profit_after_tax.f_4)-float(projection_table1.ins_particulars_profit_after_tax.f_3))/float(projection_table1.ins_particulars_profit_after_tax.f_3))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_profit_after_tax.f_4=0

            try:
                projection_table1.ins_growth_analysis_yoy_profit_after_tax.f_5=ceil(((float(projection_table1.ins_particulars_profit_after_tax.f_5)-float(projection_table1.ins_particulars_profit_after_tax.f_4))/float(projection_table1.ins_particulars_profit_after_tax.f_4))*100)
            except:
                projection_table1.ins_growth_analysis_yoy_profit_after_tax.f_5=0























            try:
                projection_table1.ins_analysis_as_of_revenue_stream_1.f_1=ceil((float(projection_table1.ins_particulars_stream_1.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_1.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_1.f_2=ceil((float(projection_table1.ins_particulars_stream_1.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_1.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_1.f_3=ceil((float(projection_table1.ins_particulars_stream_1.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_1.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_1.f_4=ceil((float(projection_table1.ins_particulars_stream_1.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_1.f_4=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_1.f_5=ceil((float(projection_table1.ins_particulars_stream_1.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_1.f_5=0











            try:
                projection_table1.ins_analysis_as_of_revenue_stream_2.f_1=ceil((float(projection_table1.ins_particulars_stream_2.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_2.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_2.f_2=ceil((float(projection_table1.ins_particulars_stream_2.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_2.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_2.f_3=ceil((float(projection_table1.ins_particulars_stream_2.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_2.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_2.f_4=ceil((float(projection_table1.ins_particulars_stream_2.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_2.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_stream_2.f_5=ceil((float(projection_table1.ins_particulars_stream_2.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_2.f_5=0










            try:
                projection_table1.ins_analysis_as_of_revenue_stream_3.f_1=ceil((float(projection_table1.ins_particulars_stream_3.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_3.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_3.f_2=ceil((float(projection_table1.ins_particulars_stream_3.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_3.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_3.f_3=ceil((float(projection_table1.ins_particulars_stream_3.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_3.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_3.f_4=ceil((float(projection_table1.ins_particulars_stream_3.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_3.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_stream_3.f_5=ceil((float(projection_table1.ins_particulars_stream_3.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_3.f_5=0







            try:
                projection_table1.ins_analysis_as_of_revenue_stream_4.f_1=ceil((float(projection_table1.ins_particulars_stream_4.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_4.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_4.f_2=ceil((float(projection_table1.ins_particulars_stream_4.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_4.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_4.f_3=ceil((float(projection_table1.ins_particulars_stream_4.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_4.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_stream_4.f_4=ceil((float(projection_table1.ins_particulars_stream_4.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_4.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_stream_4.f_5=ceil((float(projection_table1.ins_particulars_stream_4.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_stream_4.f_5=0

           







            try:
                projection_table1.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material.f_1=ceil((float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material.f_2=ceil((float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material.f_3=ceil((float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material.f_4=ceil((float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material.f_5=ceil((float(projection_table1.ins_particulars_product_development_expenses_operating_expenses_raw_material.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_product_development_expenses_operating_expenses_raw_material.f_5=0















            try:
                projection_table1.ins_analysis_as_of_revenue_employee_cost.f_1=ceil((float(projection_table1.ins_particulars_employee_cost.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_employee_cost.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_employee_cost.f_2=ceil((float(projection_table1.ins_particulars_employee_cost.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_employee_cost.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_employee_cost.f_3=ceil((float(projection_table1.ins_particulars_employee_cost.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_employee_cost.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_employee_cost.f_4=ceil((float(projection_table1.ins_particulars_employee_cost.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_employee_cost.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_employee_cost.f_5=ceil((float(projection_table1.ins_particulars_employee_cost.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_employee_cost.f_5=0










            try:
                projection_table1.ins_analysis_as_of_revenue_general_administrative_expenses.f_1=ceil((float(projection_table1.ins_particulars_general_administrative_expenses.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_general_administrative_expenses.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_general_administrative_expenses.f_2=ceil((float(projection_table1.ins_particulars_general_administrative_expenses.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_general_administrative_expenses.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_general_administrative_expenses.f_3=ceil((float(projection_table1.ins_particulars_general_administrative_expenses.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_general_administrative_expenses.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_general_administrative_expenses.f_4=ceil((float(projection_table1.ins_particulars_general_administrative_expenses.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_general_administrative_expenses.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_general_administrative_expenses.f_5=ceil((float(projection_table1.ins_particulars_general_administrative_expenses.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_general_administrative_expenses.f_5=0














            try:
                projection_table1.ins_analysis_as_of_revenue_selling_marketing_expenses.f_1=ceil((float(projection_table1.ins_particulars_selling_marketing_expenses.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_selling_marketing_expenses.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_selling_marketing_expenses.f_2=ceil((float(projection_table1.ins_particulars_selling_marketing_expenses.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_selling_marketing_expenses.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_selling_marketing_expenses.f_3=ceil((float(projection_table1.ins_particulars_selling_marketing_expenses.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_selling_marketing_expenses.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_selling_marketing_expenses.f_4=ceil((float(projection_table1.ins_particulars_selling_marketing_expenses.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_selling_marketing_expenses.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_selling_marketing_expenses.f_5=ceil((float(projection_table1.ins_particulars_selling_marketing_expenses.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_selling_marketing_expenses.f_5=0










            try:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_1.f_1=ceil((float(projection_table1.ins_particulars_other_expenses_1.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_1.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_1.f_2=ceil((float(projection_table1.ins_particulars_other_expenses_1.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_1.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_1.f_3=ceil((float(projection_table1.ins_particulars_other_expenses_1.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_1.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_1.f_4=ceil((float(projection_table1.ins_particulars_other_expenses_1.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_1.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_1.f_5=ceil((float(projection_table1.ins_particulars_other_expenses_1.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_1.f_5=0














            try:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_2.f_1=ceil((float(projection_table1.ins_particulars_other_expenses_2.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_2.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_2.f_2=ceil((float(projection_table1.ins_particulars_other_expenses_2.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_2.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_2.f_3=ceil((float(projection_table1.ins_particulars_other_expenses_2.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_2.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_2.f_4=ceil((float(projection_table1.ins_particulars_other_expenses_2.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_2.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_2.f_5=ceil((float(projection_table1.ins_particulars_other_expenses_2.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_expenses_2.f_5=0











            try:
                projection_table1.ins_analysis_as_of_revenue_total_operating_expenses.f_1=ceil((float(projection_table1.ins_particulars_total_operating_expenses.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_total_operating_expenses.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_total_operating_expenses.f_2=ceil((float(projection_table1.ins_particulars_total_operating_expenses.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_total_operating_expenses.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_total_operating_expenses.f_3=ceil((float(projection_table1.ins_particulars_total_operating_expenses.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_total_operating_expenses.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_total_operating_expenses.f_4=ceil((float(projection_table1.ins_particulars_total_operating_expenses.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_total_operating_expenses.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_total_operating_expenses.f_5=ceil((float(projection_table1.ins_particulars_total_operating_expenses.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_total_operating_expenses.f_5=0
















            try:
                projection_table1.ins_analysis_as_of_revenue_ebitda_operating_profit.f_1=ceil((float(projection_table1.ins_particulars_ebitda_operating_profit.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_ebitda_operating_profit.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_ebitda_operating_profit.f_2=ceil((float(projection_table1.ins_particulars_ebitda_operating_profit.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_ebitda_operating_profit.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_ebitda_operating_profit.f_3=ceil((float(projection_table1.ins_particulars_ebitda_operating_profit.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_ebitda_operating_profit.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_ebitda_operating_profit.f_4=ceil((float(projection_table1.ins_particulars_ebitda_operating_profit.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_ebitda_operating_profit.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_ebitda_operating_profit.f_5=ceil((float(projection_table1.ins_particulars_ebitda_operating_profit.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_ebitda_operating_profit.f_5=0













            try:
                projection_table1.ins_analysis_as_of_revenue_depreciation.f_1=ceil((float(projection_table1.ins_particulars_depreciation.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_depreciation.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_depreciation.f_2=ceil((float(projection_table1.ins_particulars_depreciation.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_depreciation.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_depreciation.f_3=ceil((float(projection_table1.ins_particulars_depreciation.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_depreciation.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_depreciation.f_4=ceil((float(projection_table1.ins_particulars_depreciation.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_depreciation.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_depreciation.f_5=ceil((float(projection_table1.ins_particulars_depreciation.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_depreciation.f_5=0















            try:
                projection_table1.ins_analysis_as_of_revenue_other_income.f_1=ceil((float(projection_table1.ins_particulars_other_income.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_income.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_other_income.f_2=ceil((float(projection_table1.ins_particulars_other_income.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_income.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_other_income.f_3=ceil((float(projection_table1.ins_particulars_other_income.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_income.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_other_income.f_4=ceil((float(projection_table1.ins_particulars_other_income.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_income.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_other_income.f_5=ceil((float(projection_table1.ins_particulars_other_income.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_other_income.f_5=0












            try:
                projection_table1.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss.f_1=ceil((float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss.f_2=ceil((float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss.f_3=ceil((float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss.f_4=ceil((float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss.f_5=ceil((float(projection_table1.ins_particulars_realised_foreign_exchange_gain_loss.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_realised_foreign_exchange_gain_loss.f_5=0














            try:
                projection_table1.ins_analysis_as_of_revenue_ebit.f_1=ceil((float(projection_table1.ins_particulars_ebit.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_ebit.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_ebit.f_2=ceil((float(projection_table1.ins_particulars_ebit.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_ebit.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_ebit.f_3=ceil((float(projection_table1.ins_particulars_ebit.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_ebit.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_ebit.f_4=ceil((float(projection_table1.ins_particulars_ebit.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_ebit.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_ebit.f_5=ceil((float(projection_table1.ins_particulars_ebit.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_ebit.f_5=0














            try:
                projection_table1.ins_analysis_as_of_revenue_interest_including_finance_charges.f_1=ceil((float(projection_table1.ins_particulars_interest_including_finance_charges.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_interest_including_finance_charges.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_interest_including_finance_charges.f_2=ceil((float(projection_table1.ins_particulars_interest_including_finance_charges.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_interest_including_finance_charges.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_interest_including_finance_charges.f_3=ceil((float(projection_table1.ins_particulars_interest_including_finance_charges.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_interest_including_finance_charges.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_interest_including_finance_charges.f_4=ceil((float(projection_table1.ins_particulars_interest_including_finance_charges.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_interest_including_finance_charges.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_interest_including_finance_charges.f_5=ceil((float(projection_table1.ins_particulars_interest_including_finance_charges.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_interest_including_finance_charges.f_5=0















            try:
                projection_table1.ins_analysis_as_of_revenue_earnings_before_tax_ebt.f_1=ceil((float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_earnings_before_tax_ebt.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_earnings_before_tax_ebt.f_2=ceil((float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_earnings_before_tax_ebt.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_earnings_before_tax_ebt.f_3=ceil((float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_earnings_before_tax_ebt.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_earnings_before_tax_ebt.f_4=ceil((float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_earnings_before_tax_ebt.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_earnings_before_tax_ebt.f_5=ceil((float(projection_table1.ins_particulars_earnings_before_tax_ebt.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_earnings_before_tax_ebt.f_5=0













            try:
                projection_table1.ins_analysis_as_of_revenue_provision_for_income_tax.f_1=ceil((float(projection_table1.ins_particulars_provision_for_income_tax.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_provision_for_income_tax.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_provision_for_income_tax.f_2=ceil((float(projection_table1.ins_particulars_provision_for_income_tax.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_provision_for_income_tax.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_provision_for_income_tax.f_3=ceil((float(projection_table1.ins_particulars_provision_for_income_tax.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_provision_for_income_tax.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_provision_for_income_tax.f_4=ceil((float(projection_table1.ins_particulars_provision_for_income_tax.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_provision_for_income_tax.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_provision_for_income_tax.f_5=ceil((float(projection_table1.ins_particulars_provision_for_income_tax.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_provision_for_income_tax.f_5=0














            try:
                projection_table1.ins_analysis_as_of_revenue_profit_after_tax.f_1=ceil((float(projection_table1.ins_particulars_profit_after_tax.f_1)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_1))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_profit_after_tax.f_1=0

            try:
                projection_table1.ins_analysis_as_of_revenue_profit_after_tax.f_2=ceil((float(projection_table1.ins_particulars_profit_after_tax.f_2)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_2))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_profit_after_tax.f_2=0

            try:
                projection_table1.ins_analysis_as_of_revenue_profit_after_tax.f_3=ceil((float(projection_table1.ins_particulars_profit_after_tax.f_3)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_3))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_profit_after_tax.f_3=0

            try:
                projection_table1.ins_analysis_as_of_revenue_profit_after_tax.f_4=ceil((float(projection_table1.ins_particulars_profit_after_tax.f_4)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_4))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_profit_after_tax.f_4=0
                
            try:
                projection_table1.ins_analysis_as_of_revenue_profit_after_tax.f_5=ceil((float(projection_table1.ins_particulars_profit_after_tax.f_5)/float(projection_table1.ins_particulars_total_revenue_from_operations_services.f_5))*100)
            except:
                projection_table1.ins_analysis_as_of_revenue_profit_after_tax.f_5=0



           
            projection_table1.save()
           

        else:
            return redirect('/login')
    else:
        return redirect('/login')





def cal_income_statement(request):
    calculate_income_statement(request)  
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    projection_table = super_plan_projection.objects.filter(id=book.projection_table).get()
    return render(request,'user-form-income-statement.html',{"data":book,"projection_table":projection_table})









#--------------------------------------------------- User Forms -------------------------------------------


def user_form_1(request):                                # User Form 1

    now = datetime.datetime.now()
    year = now.year
    years = [i for i in range(year-5,year+11)]
    request.session["years"]=years

    if(auth_user(request)):
        if(request.session.get("form")):
            del request.session['form']
        return render(request,'user-form1.html')
    else:
        return redirect('/login')



def user_form_1_submit(request):            # User Form 1 Submit

    if(not request.session.get("form")):
        book = super_plan_forms()
        book.user = User_db.objects.filter(id=request.session['user']).get()
        projection_table = super_plan_projection()
        projection_table.form_id = book.id
        projection_table.save()
        book.projection_table=projection_table
    else:
        book = super_plan_forms.objects.filter(id=request.session['form']).get()

    if(auth_user(request) and book and request.method=="POST"):

        if(request.POST.get("theme")):
            book.theme = request.POST["theme"]

        if(request.POST.get("currency")):
            book.currency = request.POST["currency"]

        if(request.POST.get("denomination")):
            book.denomination = request.POST["denomination"]


        book.pack = 'Starter Pack'

        book.current_fillup_position = 1
        book.save()

        request.session["form"] = book.id
        book.projection_table = projection_table_init(request) # initialize the projection table
        
        book.save()

        

        return render(request,'user-form2.html',{"data":book})
    else:
        return redirect('/login')






def user_form_2_submit(request):            # User Form 2 Submit
    if(auth_user(request) and request.method=="POST"):

        book = super_plan_forms.objects.filter(id=request.session['form']).get()
        if(auth_user(request) and book and request.method=="POST"):



            book.company_name = request.POST["company_name"]
            book.company_website_link = request.POST["company_website_link"]
            book.owner_name = request.POST["owner_name"]
            book.countrycode = request.POST['countrycode']
            book.phone_number = request.POST["phone_number"]
            book.email_id = request.POST["email_id"]

            if request.POST.get("gst_number") and request.POST.get("gst_name"):
                book.gst_number = request.POST["gst_number"]
                book.gst_name = request.POST["gst_name"]


            book.current_fillup_position = 2
            book.save()
            request.session["form"] = book.id





            ind_types = Industries.objects.all()




            return render(request,'user-form3.html',{"data":book,"industries":ind_types})
        else:
            return render(request,'user-form1.html')
    else:
        return redirect('/login')









def user_form_3_submit(request):            # User Form 3 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        book.about_the_company = request.POST["about_the_company"]
        book.company_founded = request.POST["company_founded"]
        book.industry_type = request.POST["industry_type"]

        if(request.FILES.get("company_logo")):
            book.company_logo = request.FILES["company_logo"]


        book.current_fillup_position = 3
        book.save()

        return render(request,'user-form4.html',{"data":book})
    else:
        return redirect('/login')








def user_form_4_submit(request):            # User Form 4 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        book.challenges_faced = multi_input_insert(request,"challenges_faced[]")
        book.solutions_provided = multi_input_insert(request,"solutions_provided[]")


        book.current_fillup_position = 4
        book.save()

        return render(request,'user-form5.html',{"data":book})
    else:
        return redirect('/login')







def user_form_5_submit(request):            # User Form 5 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):


        if(request.FILES.get("products_and_services[]")):
            if(book.products_and_services.id):
                multi_input_insert(request,"products_and_services[]",book.products_and_services.id)
            else:
                book.products_and_services = multi_input_insert(request,"products_and_services[]")

        if(request.FILES.get("products_and_services_file[]")):
            if(book.products_and_services_file.id):
                multi_image_insert(request,"products_and_services_file[]",book.products_and_services_file.id)
            else:
                 book.products_and_services_file = multi_image_insert(request,"products_and_services_file[]")

        book.top_clients= multi_input_insert(request,"top_clients[]")
        book.top_clients_file= multi_image_insert(request,"top_clients_file[]")
        book.milestones_time= multi_input_insert(request,"milestones_time[]")
        book.milestones_achievement= multi_input_insert(request,"milestones_achievement[]")
        book.locations_served= multi_input_insert(request,"locations_served[]")


        if(request.POST.get("swot_s")):
            book.swot_s = request.POST["swot_s"]

        if(request.POST.get("swot_w")):
            book.swot_w = request.POST["swot_w"]

        if(request.POST.get("swot_o")):
            book.swot_o = request.POST["swot_o"]

        if(request.POST.get("swot_t")):
            book.swot_t = request.POST["swot_t"]

        book.current_fillup_position = 5
        book.save()
        return render(request,'user-form6.html',{"data":book})
    else:
        return redirect('/login')







def user_form_6_submit(request):            # User Form 6 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):



        multi = super_plan_forms_multiple_inputs()
        multi.user = User_db.objects.filter(id=request.session['user']).get()
        multi.form_id=request.session['form']

        if(request.POST.get("management_team_name_1")):
            multi.f_1= request.POST["management_team_name_1"]
        if(request.POST.get("management_team_name_2")):
            multi.f_2= request.POST["management_team_name_2"]
        if(request.POST.get("management_team_name_3")):
            multi.f_3= request.POST["management_team_name_3"]

        multi.save()
        book.management_team_name=multi





        multi = super_plan_forms_multiple_inputs()
        multi.user = User_db.objects.filter(id=request.session['user']).get()
        multi.form_id=request.session['form']

        if(request.POST.get("management_team_designation_1")):
            multi.f_1= request.POST["management_team_designation_1"]
        if(request.POST.get("management_team_designation_2")):
            multi.f_2= request.POST["management_team_designation_2"]
        if(request.POST.get("management_team_designation_3")):
            multi.f_3= request.POST["management_team_designation_3"]

        multi.save()
        book.management_team_designation=multi





        multi = super_plan_forms_multiple_inputs()
        multi.user = User_db.objects.filter(id=request.session['user']).get()
        multi.form_id=request.session['form']

        if(request.POST.get("management_team_contact_1")):
            multi.f_1= request.POST["management_team_contact_1"]
        if(request.POST.get("management_team_contact_2")):
            multi.f_2= request.POST["management_team_contact_2"]
        if(request.POST.get("management_team_contact_3")):
            multi.f_3= request.POST["management_team_contact_3"]

        multi.save()
        book.management_team_contact=multi




        multi = super_plan_forms_multiple_images()
        multi.user = User_db.objects.filter(id=request.session['user']).get()
        multi.form_id=request.session['form']

        if(request.FILES.get("management_team_file_1")):
            multi.i_1=request.FILES["management_team_file_1"]
        if(request.FILES.get("management_team_file_2")):
            multi.i_2=request.FILES["management_team_file_2"]
        if(request.FILES.get("management_team_file_3")):
            multi.i_3=request.FILES["management_team_file_3"]

        multi.save()
        book.management_team_file=multi


        book.current_fillup_position = 6
        book.save()
        return render(request,'user-form7.html',{"data":book})
    else:
        return redirect('/login')









def user_form_7_submit(request):            # User Form 7 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        book.marketing_strategies_offline = multi_input_insert(request,"marketing_strategies_offline[]")
        book.marketing_strategies_online = multi_input_insert(request,"marketing_strategies_online[]")

        book.current_fillup_position = 7
        book.save()
        return render(request,'user-form8.html',{"data":book})
    else:
        return redirect('/login')




def user_form_8_submit(request):            # User Form 8 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        book.growth_strategy = multi_input_insert(request,"growth_strategy[]")

        book.current_fillup_position = 8
        book.save()




        ind_types = Industries.objects.all()

        if(book.industry_type):
            ind_an=None
            ind_gw=None
            ind_an_c=Industry_analysis.objects.filter(industry__pk=book.industry_type).count()
            ind_gw_c=Industry_growth_drivers.objects.filter(industry__pk=book.industry_type).count()
            if(ind_an_c):
                ind_an=Industry_analysis.objects.filter(industry__pk=book.industry_type).get()
            if(ind_gw_c):
                ind_gw=Industry_growth_drivers.objects.filter(industry__pk=book.industry_type).get()
            return render(request,'user-form9.html',{"data":book,"industries":ind_types,"industry_analysis":ind_an,"industry_growth_drivers":ind_gw})
        else:
            return render(request,'user-form9.html',{"data":book,"industries":ind_types})

    else:
        return redirect('/login')







def user_form_9_submit(request):            # User Form 9 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):


        user = User_db.objects.filter(id=request.session['user']).get()
        form_id = request.session['form']



        if(request.POST.get("industry_analysis_glob")):
            book.industry_analysis_glob = request.POST["industry_analysis_glob"]

        if(request.FILES.get("industry_analysis_glob_img")):
            book.industry_analysis_glob_img = request.FILES["industry_analysis_glob_img"]


        if(request.POST.get("industry_analysis_india")):
            book.industry_analysis_india = request.POST["industry_analysis_india"]

        if(request.FILES.get("industry_analysis_india_img")):
            book.industry_analysis_india_img = request.FILES["industry_analysis_india_img"]

        book.competitor_analysis_n = multi_input_insert(request,"competitor_analysis_n[]")
        book.competitor_analysis_p = multi_input_insert(request,"competitor_analysis_p[]")


        book.competitor_analysis_v1 = competitor_analysis_input(request,"competitor_analysis_v1[]")
        book.competitor_analysis_v2 = competitor_analysis_input(request,"competitor_analysis_v2[]")
        book.competitor_analysis_v3 = competitor_analysis_input(request,"competitor_analysis_v3[]")
        book.competitor_analysis_v4 = competitor_analysis_input(request,"competitor_analysis_v4[]")
        book.competitor_analysis_v5 = competitor_analysis_input(request,"competitor_analysis_v5[]")


        book.industry_growth_drivers = multi_input_insert(request,"industry_growth_drivers[]")
        book.usp = multi_input_insert(request,"usp[]")

        book.current_fillup_position = 9
        book.save()
        return render(request,'user-form9-1.html',{"data":book})
    else:
        return redirect('/login')





def user_form_9_1_submit(request):            # User Form 9_1 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):
        book.historical_data="no"
        book.save()

        return render(request,'user-form10.html',{"data":book})
    else:
        return redirect('/login')



def user_form_9_1_historical_submit(request):          #XLSX input form
    book = super_plan_forms.objects.filter(id=request.session['form']).get()

    if(auth_user(request) and book and request.method=="POST"):
        if(request.FILES.get("historical_xl")):
            book.historical_xl = request.FILES["historical_xl"]
            book.save()

            book = super_plan_forms.objects.filter(id=request.session['form']).get()

            data = get_data(settings.MEDIA_ROOT+book.historical_xl.url[7:])

            try:
                c=0
                for i in range(3,122):
                    if(len(data["Historicals"][i])>4):
                        for j in range(1,5):
                            c=c+1



                xl_form = super_plan_form_xl_input()
                xl_form.form_id=request.session['form']

                xl_form.capex_schedule_opening_gross = multi_input_insert_xl(request,data,3)
                xl_form.capex_schedule_additions = multi_input_insert_xl(request,data,4)
                xl_form.capex_schedule_additions_intangible = multi_input_insert_xl(request,data,5)
                xl_form.capex_schedule_deletions = multi_input_insert_xl(request,data,6)
                xl_form.capex_schedule_closing_gross = multi_input_insert_xl(request,data,7)
                xl_form.capex_schedule_accumulated_depreciation = multi_input_insert_xl(request,data,8)
                xl_form.capex_schedule_net_value = multi_input_insert_xl(request,data,9)
                xl_form.capex_schedule_current_depreciation = multi_input_insert_xl(request,data,10)
                xl_form.capex_schedule_average_depreciation_rate = multi_input_insert_xl(request,data,12)

                xl_form.debt_schedule_secured_loans_from_banks = multi_input_insert_xl(request,data,19)
                xl_form.debt_schedule_secured_loans_term_loans = multi_input_insert_xl(request,data,20)
                xl_form.debt_schedule_secured_loans_othe_loans = multi_input_insert_xl(request,data,21)
                xl_form.debt_schedule_secured_loans_finance_lease_obligation = multi_input_insert_xl(request,data,22)
                xl_form.debt_schedule_secured_loans_total_secured_loans = multi_input_insert_xl(request,data,23)
                xl_form.debt_schedule_unsecured_loans = multi_input_insert_xl(request,data,25)
                xl_form.debt_schedule_total_unsecured_loan = multi_input_insert_xl(request,data,27)
                xl_form.debt_schedule_total_debt  = multi_input_insert_xl(request,data,29)
                xl_form.debt_schedule_interest_expense  = multi_input_insert_xl(request,data,31)
                xl_form.debt_schedule_average_interest_rate = multi_input_insert_xl(request,data,32)

                xl_form.income_statement_revenue_stream_1 = multi_input_insert_xl(request,data,39)
                xl_form.income_statement_revenue_stream_2 = multi_input_insert_xl(request,data,40)
                xl_form.income_statement_revenue_stream_3 = multi_input_insert_xl(request,data,41)
                xl_form.income_statement_revenue_stream_4 = multi_input_insert_xl(request,data,42)
                xl_form.income_statement_total_revenue_from_operations_services = multi_input_insert_xl(request,data,44)
                xl_form.income_statement_product_development_expenses_operating_expenses_raw_material = multi_input_insert_xl(request,data,47)
                xl_form.income_statement_employee_cost = multi_input_insert_xl(request,data,48)
                xl_form.income_statement_general_and_administrative_expenses = multi_input_insert_xl(request,data,49)
                xl_form.income_statement_selling_and_marketing_expenses = multi_input_insert_xl(request,data,50)
                xl_form.income_statement_other_expenses_1 = multi_input_insert_xl(request,data,51)
                xl_form.income_statement_other_expenses_2 = multi_input_insert_xl(request,data,52)
                xl_form.income_statement_total_operating_expenses = multi_input_insert_xl(request,data,54)
                xl_form.income_statement_ebitda_operating_profit = multi_input_insert_xl(request,data,56)
                xl_form.income_statement_depreciation = multi_input_insert_xl(request,data,57)
                xl_form.income_statement_other_income = multi_input_insert_xl(request,data,58)
                xl_form.income_statement_realised_foreign_exchange_gain_loss  = multi_input_insert_xl(request,data,59)
                xl_form.income_statement_ebit = multi_input_insert_xl(request,data,60)
                xl_form.income_statement_interest_including_finance_charges  = multi_input_insert_xl(request,data,61)
                xl_form.income_statement_earnings_before_tax_ebt = multi_input_insert_xl(request,data,62)
                xl_form.income_statement_provision_for_income_tax  = multi_input_insert_xl(request,data,63)
                xl_form.income_statement_profit_after_tax  = multi_input_insert_xl(request,data,64)
                xl_form.income_statement_ebitda_prc = multi_input_insert_xl(request,data,66)
                xl_form.income_statement_pat_prc = multi_input_insert_xl(request,data,67)



                xl_form.balance_sheet_shareholders_funds_share_capital = multi_input_insert_xl(request,data,74)
                xl_form.balance_sheet_shareholders_funds_reserve_and_surplus = multi_input_insert_xl(request,data,75)
                xl_form.balance_sheet_shareholders_funds_equity_funds_raised = multi_input_insert_xl(request,data,76)
                xl_form.balance_sheet_shareholders_funds_total_shareholder_funds = multi_input_insert_xl(request,data,77)



                xl_form.balance_sheet_non_current_liabilities_secured_loans = multi_input_insert_xl(request,data,80)
                xl_form.balance_sheet_non_current_liabilities_unsecured_loans = multi_input_insert_xl(request,data,81)
                xl_form.balance_sheet_non_current_liabilities_deferred_tax_liabilities  = multi_input_insert_xl(request,data,82)
                xl_form.balance_sheet_non_current_liabilities_long_term_provisions = multi_input_insert_xl(request,data,83)
                xl_form.balance_sheet_non_current_liabilities_other_non_current_liabilities = multi_input_insert_xl(request,data,84)
                xl_form.balance_sheet_total_non_current_liabilitie = multi_input_insert_xl(request,data,85)


                xl_form.balance_sheet_current_liabilities_short_term_borrowings = multi_input_insert_xl(request,data,88)
                xl_form.balance_sheet_current_liabilities_short_term_provisions = multi_input_insert_xl(request,data,89)
                xl_form.balance_sheet_current_liabilities_sundry_creditors = multi_input_insert_xl(request,data,90)
                xl_form.balance_sheet_current_liabilities_other_current_liabilities = multi_input_insert_xl(request,data,91)
                xl_form.balance_sheet_current_liabilities_total_current_liabilities = multi_input_insert_xl(request,data,92)

                xl_form.balance_sheet_total_liabilities = multi_input_insert_xl(request,data,94)


                xl_form.balance_sheet_non_current_assets_gross_fixed_assets = multi_input_insert_xl(request,data,97)
                xl_form.balance_sheet_non_current_assets_less_accumulated_depreciation = multi_input_insert_xl(request,data,98)
                xl_form.balance_sheet_non_current_assets_net_fixed_assets = multi_input_insert_xl(request,data,99)
                xl_form.balance_sheet_non_current_assets_intangible_assets = multi_input_insert_xl(request,data,101)
                xl_form.balance_sheet_non_current_assets_long_term_loans_and_advances = multi_input_insert_xl(request,data,102)
                xl_form.balance_sheet_non_current_assets_long_term_investments = multi_input_insert_xl(request,data,103)
                xl_form.balance_sheet_non_current_assets_deferred_tax_assets = multi_input_insert_xl(request,data,104)
                xl_form.balance_sheet_non_current_assets_other_non_current_assets = multi_input_insert_xl(request,data,105)
                xl_form.balance_sheet_non_current_assets_total_non_current_asset = multi_input_insert_xl(request,data,107)


                xl_form.balance_sheet_current_assets_cash = multi_input_insert_xl(request,data,110)
                xl_form.balance_sheet_current_assets_sundry_debtors = multi_input_insert_xl(request,data,111)
                xl_form.balance_sheet_current_assets_inventory = multi_input_insert_xl(request,data,112)
                xl_form.balance_sheet_current_assets_short_term_investments = multi_input_insert_xl(request,data,113)
                xl_form.balance_sheet_current_assets_short_term_loans_and_advances = multi_input_insert_xl(request,data,114)
                xl_form.balance_sheet_current_assets_other_current_assets = multi_input_insert_xl(request,data,115)
                xl_form.balance_sheet_current_assets_total_current_assets = multi_input_insert_xl(request,data,117)

                xl_form.balance_sheet_total_assets = multi_input_insert_xl(request,data,119)
                xl_form.balance_sheet_check = multi_input_insert_xl(request,data,121)



                xl_form.save()
                book.historical_xl_data=xl_form
                book.historical_data="yes"
                book.save()
                return render(request,'user-form10.html',{"data":book})
            except:
                book.historical_xl=None
                book.historical_data="no"
                book.save()
                messages.info(request,"Invalid Excel file format !")
                return render(request,'user-form9-1.html')



        else:
            messages.info(request,"Something went wrong, Try again !")
            return render(request,'user-form9-1.html')

    else:
        return redirect('/login')





def user_form_10_submit(request):            # User Form 10 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        book.profit_and_loss_years = multi_input_insert(request,"profit_and_loss_years[]")
        book.revenue_growth_or_amount_1 = multi_input_insert(request,"revenue_growth_or_amount_1[]")
        book.revenue_growth_or_amount_2 = multi_input_insert(request,"revenue_growth_or_amount_2[]")
        book.revenue_growth_or_amount_3 = multi_input_insert(request,"revenue_growth_or_amount_3[]")
        book.revenue_growth_or_amount_4 = multi_input_insert(request,"revenue_growth_or_amount_4[]")
        book.other_income_growth_or_amount = multi_input_insert(request,"other_income_growth_or_amount[]")
        book.realised_foreign_exchange_gain_or_loss = multi_input_insert(request,"realised_foreign_exchange_gain_or_loss[]")
        book.direct_material_units = multi_input_insert(request,"direct_material_units[]")
        book.direct_material_average_cost_per_unit = multi_input_insert(request,"direct_material_average_cost_per_unit[]")
        book.direct_labour_no_of_employees = multi_input_insert(request,"direct_labour_no_of_employees[]")
        book.direct_labour_average_cost_per_employee = multi_input_insert(request,"direct_labour_average_cost_per_employee[]")
        book.direct_expenses = multi_input_insert(request,"direct_expenses[]")
        book.other_direct_expenses_1 = multi_input_insert(request,"other_direct_expenses_1[]")
        book.other_direct_expenses_2 = multi_input_insert(request,"other_direct_expenses_2[]")
        book.other_direct_expenses_3 = multi_input_insert(request,"other_direct_expenses_3[]")
        book.administration_no_of_employees = multi_input_insert(request,"administration_no_of_employees[]")
        book.administration_average_cost_per_employee = multi_input_insert(request,"administration_average_cost_per_employee[]")
        book.selling_and_distribution_no_of_employees = multi_input_insert(request,"selling_and_distribution_no_of_employees[]")
        book.selling_and_distribution_average_cost_per_employee = multi_input_insert(request,"selling_and_distribution_average_cost_per_employee[]")
        book.marketing_no_of_employees = multi_input_insert(request,"marketing_no_of_employees[]")
        book.marketing_average_cost_per_employee = multi_input_insert(request,"marketing_average_cost_per_employee[]")
        book.research_and_development_no_of_employees = multi_input_insert(request,"research_and_development_no_of_employees[]")
        book.research_and_development_average_cost_per_employee = multi_input_insert(request,"research_and_development_average_cost_per_employee[]")

        if(request.POST.get("other_employees_1")):
            book.other_employees_1 = request.POST["other_employees_1"]

            book.other_employees_1_no_of_employees = multi_input_insert(request,"other_employees_1_no_of_employees[]")
            book.other_employees_1_average_cost_per_employee = multi_input_insert(request,"other_employees_1_average_cost_per_employee[]")


        if(request.POST.get("other_employees_2")):
            book.other_employees_2 = request.POST["other_employees_2"]

            book.other_employees_2_no_of_employees = multi_input_insert(request,"other_employees_2_no_of_employees[]")
            book.other_employees_2_average_cost_per_employee = multi_input_insert(request,"other_employees_2_average_cost_per_employee[]")


        if(request.POST.get("other_employees_3")):
            book.other_employees_3 = request.POST["other_employees_3"]

            book.other_employees_3_no_of_employees = multi_input_insert(request,"other_employees_3_no_of_employees[]")
            book.other_employees_3_average_cost_per_employee = multi_input_insert(request,"other_employees_3_average_cost_per_employee[]")

        book.rent = multi_input_insert(request,"rent[]")
        book.telephone_expenses = multi_input_insert(request,"telephone_expenses[]")
        book.electricity = multi_input_insert(request,"electricity[]")
        book.printing_and_stationery = multi_input_insert(request,"printing_and_stationery[]")
        book.audit_fees = multi_input_insert(request,"audit_fees[]")
        book.other_administration_expenses_1 = multi_input_insert(request,"other_administration_expenses_1[]")
        book.other_administration_expenses_2 = multi_input_insert(request,"other_administration_expenses_2[]")
        book.other_administration_expenses_3 = multi_input_insert(request,"other_administration_expenses_3[]")
        book.digital_marketing_cost = multi_input_insert(request,"digital_marketing_cost[]")
        book.sales_commissions = multi_input_insert(request,"sales_commissions[]")
        book.travelling_expenses = multi_input_insert(request,"travelling_expenses[]")
        book.advertisement = multi_input_insert(request,"advertisement[]")
        book.logistics_expenses = multi_input_insert(request,"logistics_expenses[]")
        book.other_selling_and_marketing_expenses_1 = multi_input_insert(request,"other_selling_and_marketing_expenses_1[]")
        book.other_selling_and_marketing_expenses_2 = multi_input_insert(request,"other_selling_and_marketing_expenses_2[]")
        book.other_selling_and_marketing_expenses_3 = multi_input_insert(request,"other_selling_and_marketing_expenses_3[]")
        book.other_expenses_1 = multi_input_insert(request,"other_expenses_1[]")
        book.other_expenses_2 = multi_input_insert(request,"other_expenses_2[]")
        book.income_tax_rate = multi_input_insert(request,"income_tax_rate[]")
        
        


  #********* projection table data ******


        projection_table = super_plan_projection.objects.filter(id=book.projection_table).get()

        projection_table.p_revenue_growth_or_amount_1= multi_input_insert_projection(request,"revenue_growth_or_amount_1_[]")
        projection_table.p_revenue_growth_or_amount_2 = multi_input_insert_projection(request,"revenue_growth_or_amount_2_[]")
        projection_table.p_revenue_growth_or_amount_3 = multi_input_insert_projection(request,"revenue_growth_or_amount_3_[]")
        projection_table.p_revenue_growth_or_amount_4 = multi_input_insert_projection(request,"revenue_growth_or_amount_4_[]")
        projection_table.p_total_revenue_from_operations_services = multi_input_insert_projection(request,"total_revenue_from_operations_services_[]")
        projection_table.p_other_income_growth_or_amount = multi_input_insert_projection(request,"other_income_growth_or_amount_[]")
        projection_table.p_realised_foreign_exchange_gain_or_loss = multi_input_insert_projection(request,"realised_foreign_exchange_gain_or_loss_[]")

        projection_table.p_direct_material_units = multi_input_insert_projection(request,"direct_material_units_[]")
        projection_table.p_direct_material_average_cost_per_unit = multi_input_insert_projection(request,"direct_material_average_cost_per_unit_[]")
        projection_table.p_total_direct_material_cost = multi_input_insert_projection(request,"total_direct_material_cost_[]")


        projection_table.p_direct_labour_no_of_employees = multi_input_insert_projection(request,"direct_labour_no_of_employees_[]")
        projection_table.p_direct_labour_average_cost_per_employee = multi_input_insert_projection(request,"direct_labour_average_cost_per_employee_[]")
        projection_table.p_total_labour_cost = multi_input_insert_projection(request,"total_labour_cost_[]")

        projection_table.p_direct_expenses = multi_input_insert_projection(request,"direct_expenses_[]")
        projection_table.p_other_direct_expenses_1 = multi_input_insert_projection(request,"other_direct_expenses_1_[]")
        projection_table.p_other_direct_expenses_2 = multi_input_insert_projection(request,"other_direct_expenses_2_[]")
        projection_table.p_other_direct_expenses_3 = multi_input_insert_projection(request,"other_direct_expenses_3_[]")

        projection_table.p_total_product_development_expenses_operating_expenses = multi_input_insert_projection(request,"total_product_development_expenses_operating_expenses_[]")

        projection_table.p_administration_no_of_employees = multi_input_insert_projection(request,"administration_no_of_employees_[]")
        projection_table.p_administration_average_cost_per_employee = multi_input_insert_projection(request,"administration_average_cost_per_employee_[]")
        projection_table.p_administration_employees_total_cost_per_year = multi_input_insert_projection(request,"administration_employees_total_cost_per_year_[]")

        projection_table.p_selling_and_distribution_no_of_employees = multi_input_insert_projection(request,"selling_and_distribution_no_of_employees_[]")
        projection_table.p_selling_and_distribution_average_cost_per_employee = multi_input_insert_projection(request,"selling_and_distribution_average_cost_per_employee_[]")
        projection_table.p_selling_employees_total_cost_per_year = multi_input_insert_projection(request,"selling_employees_total_cost_per_year_[]")


        projection_table.p_marketing_no_of_employees = multi_input_insert_projection(request,"marketing_no_of_employees_[]")
        projection_table.p_marketing_average_cost_per_employee = multi_input_insert_projection(request,"marketing_average_cost_per_employee_[]")
        projection_table.p_marketing_employees_total_cost_per_year = multi_input_insert_projection(request,"marketing_employees_total_cost_per_year_[]")


        projection_table.p_research_and_development_no_of_employees = multi_input_insert_projection(request,"research_and_development_no_of_employees_[]")
        projection_table.p_research_and_development_average_cost_per_employee = multi_input_insert_projection(request,"research_and_development_average_cost_per_employee_[]")
        projection_table.p_research_employees_total_cost_per_year = multi_input_insert_projection(request,"research_employees_total_cost_per_year_[]")


        projection_table.p_other_employees_1_no_of_employees = multi_input_insert_projection(request,"other_employees_1_no_of_employees_[]")
        projection_table.p_other_employees_1_average_cost_per_employee = multi_input_insert_projection(request,"other_employees_1_average_cost_per_employee_[]")
        projection_table.p_other_employees_1_employees_total_cost_per_year = multi_input_insert_projection(request,"other_employees_1_employees_total_cost_per_year_[]")


        projection_table.p_other_employees_2_no_of_employees = multi_input_insert_projection(request,"other_employees_2_no_of_employees_[]")
        projection_table.p_other_employees_2_average_cost_per_employee = multi_input_insert_projection(request,"other_employees_2_average_cost_per_employee_[]")
        projection_table.p_other_employees_2_employees_total_cost_per_year = multi_input_insert_projection(request,"other_employees_2_employees_total_cost_per_year_[]")


        projection_table.p_other_employees_3_no_of_employees = multi_input_insert_projection(request,"other_employees_3_no_of_employees_[]")
        projection_table.p_other_employees_3_average_cost_per_employee = multi_input_insert_projection(request,"other_employees_3_average_cost_per_employee_[]")
        projection_table.p_other_employees_3_employees_total_cost_per_year = multi_input_insert_projection(request,"other_employees_3_employees_total_cost_per_year_[]")

        projection_table.p_total_employee_expenses = multi_input_insert_projection(request,"total_employee_expenses_[]")

        projection_table.p_rent = multi_input_insert_projection(request,"rent_[]")
        projection_table.p_telephone_expenses = multi_input_insert_projection(request,"telephone_expenses_[]")
        projection_table.p_electricity = multi_input_insert_projection(request,"electricity_[]")
        projection_table.p_printing_and_stationery = multi_input_insert_projection(request,"printing_and_stationery_[]")
        projection_table.p_audit_fees = multi_input_insert_projection(request,"audit_fees_[]")
        projection_table.p_other_administration_expenses_1 = multi_input_insert_projection(request,"other_administration_expenses_1_[]")
        projection_table.p_other_administration_expenses_2 = multi_input_insert_projection(request,"other_administration_expenses_2_[]")
        projection_table.p_other_administration_expenses_3 = multi_input_insert_projection(request,"other_administration_expenses_3_[]")
        projection_table.p_total_general_administrative_expenses = multi_input_insert_projection(request,"total_general_administrative_expenses_[]")

        projection_table.p_digital_marketing_cost = multi_input_insert_projection(request,"digital_marketing_cost_[]")
        projection_table.p_sales_commissions = multi_input_insert_projection(request,"sales_commissions_[]")
        projection_table.p_travelling_expenses = multi_input_insert_projection(request,"travelling_expenses_[]")
        projection_table.p_advertisement = multi_input_insert_projection(request,"advertisement_[]")
        projection_table.p_logistics_expenses = multi_input_insert_projection(request,"logistics_expenses_[]")
        projection_table.p_other_selling_and_marketing_expenses_1 = multi_input_insert_projection(request,"other_selling_and_marketing_expenses_1_[]")
        projection_table.p_other_selling_and_marketing_expenses_2 = multi_input_insert_projection(request,"other_selling_and_marketing_expenses_2_[]")
        projection_table.p_other_selling_and_marketing_expenses_3 = multi_input_insert_projection(request,"other_selling_and_marketing_expenses_3_[]")
        projection_table.p_total_selling_marketing_expenses = multi_input_insert_projection(request,"total_selling_marketing_expenses_[]")

        projection_table.p_other_expenses_1 = multi_input_insert_projection(request,"other_expenses_1_[]")
        projection_table.p_other_expenses_2 = multi_input_insert_projection(request,"other_expenses_2_[]")
        projection_table.p_income_tax_rate = multi_input_insert_projection(request,"income_tax_rate_[]")
        

        projection_table.save()

        book.current_fillup_position = 10
        book.save()

        

        return render(request,'user-form11.html',{"data":book})
    else:
        return redirect('/login')










def user_form_11_submit(request):            # User Form 11 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        
        book.capex_years = multi_input_insert(request,"capex_years[]")
        book.capex_opening_gross = multi_input_insert(request,"capex_opening_gross[]")
        book.capex_additions = multi_input_insert(request,"capex_additions[]")
        book.capex_additions_intangible = multi_input_insert(request,"capex_additions_intangible[]")
        book.capex_deletions = multi_input_insert(request,"capex_deletions[]")
        book.capex_average_depreciation_rate = multi_input_insert(request,"capex_average_depreciation_rate[]")




        #********** Projection table ***********

        projection_table = super_plan_projection.objects.filter(id=book.projection_table).get()

        projection_table.p_capex_opening_gross = multi_input_insert_projection(request,"capex_opening_gross_[]")
        projection_table.p_capex_additions  = multi_input_insert_projection(request,"capex_additions_[]")
        projection_table.p_capex_additions_intangible  = multi_input_insert_projection(request,"capex_additions_intangible_[]")
        projection_table.p_capex_deletions  = multi_input_insert_projection(request,"capex_deletions_[]")
        projection_table.p_closing_gross  = multi_input_insert_projection(request,"closing_gross_[]")
        projection_table.p_accumulated_depreciation  = multi_input_insert_projection(request,"accumulated_depreciation_[]")
        projection_table.p_net_value  = multi_input_insert_projection(request,"net_value_[]")
        projection_table.p_current_depreciation  = multi_input_insert_projection(request,"current_depreciation_[]")
        projection_table.p_capex_average_depreciation_rate  = multi_input_insert_projection(request,"capex_average_depreciation_rate_[]")

        projection_table.save()
        book.current_fillup_position = 11
        book.save()


        return render(request,'user-form12.html',{"data":book})
    else:
        return redirect('/login')



















def user_form_12_submit(request):            # User Form 12 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        book.balance_sheet_years = multi_input_insert(request,"balance_sheet_years[]")
        book.share_capital = multi_input_insert(request,"share_capital[]")
        book.equity_funds_raised = multi_input_insert(request,"equity_funds_raised[]")
        book.secured_loans_from_banks = multi_input_insert(request,"secured_loans_from_banks[]")
        book.secured_loans_term_loans = multi_input_insert(request,"secured_loans_term_loans[]")
        book.secured_loans_other_loans = multi_input_insert(request,"secured_loans_other_loans[]")
        book.secured_loans_finance_lease_obligation = multi_input_insert(request,"secured_loans_finance_lease_obligation[]")
        book.unsecured_loans = multi_input_insert(request,"unsecured_loans[]")
        book.average_interest_rate_debt = multi_input_insert(request,"average_interest_rate_debt[]")
        book.deferred_tax_liabilities  = multi_input_insert(request,"deferred_tax_liabilities[]")
        book.long_term_provisions_growth_or_amount = multi_input_insert(request,"long_term_provisions_growth_or_amount[]")
        book.other_non_current_liabilities_growth_or_amount = multi_input_insert(request,"other_non_current_liabilities_growth_or_amount[]")
        book.short_term_borrowings_growth_or_amount = multi_input_insert(request,"short_term_borrowings_growth_or_amount[]")
        book.short_term_provisions_growth_or_amount = multi_input_insert(request,"short_term_provisions_growth_or_amount[]")
        book.sundry_creditors_no_of_days = multi_input_insert(request,"sundry_creditors_no_of_days[]")
        book.other_current_liabilities_growth_or_amount = multi_input_insert(request,"other_current_liabilities_growth_or_amount[]")
        book.intangible_assets_growth_or_amount = multi_input_insert(request,"intangible_assets_growth_or_amount[]")
        book.long_term_loans_and_advances_growth_or_amount = multi_input_insert(request,"long_term_loans_and_advances_growth_or_amount[]")
        book.long_term_investments_growth_or_amount = multi_input_insert(request,"long_term_investments_growth_or_amount[]")
        book.deferred_tax_assets = multi_input_insert(request,"deferred_tax_assets[]")
        book.other_non_current_assets_growth_or_amount = multi_input_insert(request,"other_non_current_assets_growth_or_amount[]")
        book.sundry_debtors_no_of_days = multi_input_insert(request,"sundry_debtors_no_of_days[]")
        book.inventory_no_of_days = multi_input_insert(request,"inventory_no_of_days[]")
        book.short_term_investments_growth_or_amount = multi_input_insert(request,"short_term_investments_growth_or_amount[]")
        book.short_term_loans_and_advances_growth_or_amount = multi_input_insert(request,"short_term_loans_and_advances_growth_or_amount[]")
        book.other_current_assets_growth_or_amount = multi_input_insert(request,"other_current_assets_growth_or_amount[]")


        book.current_fillup_position = 12
        book.save()
        return redirect("/successful-purchased")
    else:
        return redirect('/login')



#----------------------------------------------------- Forms end-----------------------




def superplan_form_number(request,id):                                # User Superplan form by GET
    if(id=="9-1" or 1<=int(id)<=12 ):
        if(request.session.get('form')):
            book = super_plan_forms.objects.filter(id=request.session['form']).get()
        else:
            book=False
        if(auth_user(request) and book ):
            ind_types = Industries.objects.all()

            if(book.industry_type):
                ind_an=None
                ind_gw=None
                ind_an_c=Industry_analysis.objects.filter(industry__pk=book.industry_type).count()
                ind_gw_c=Industry_growth_drivers.objects.filter(industry__pk=book.industry_type).count()
                if(ind_an_c):
                    ind_an=Industry_analysis.objects.filter(industry__pk=book.industry_type).get()
                if(ind_gw_c):
                    ind_gw=Industry_growth_drivers.objects.filter(industry__pk=book.industry_type).get()
                return render(request,'user-form'+str(id)+'.html',{"data":book,"industries":ind_types,"industry_analysis":ind_an,"industry_growth_drivers":ind_gw})
            else:
                return render(request,'user-form'+str(id)+'.html',{"data":book,"industries":ind_types})
        else:
            return redirect('/login')
    else:
        return redirect('/login')













def user_all_superplan_bookings(request):                                # User All Template view

    if(auth_user(request)):
        data = super_plan_forms.objects.filter(user=request.session['user'],current_fillup_position=13)
        return render(request,'user-all-superplan-bookings.html',{"bookings":data})
    else:
        return redirect('/login')







def user_template_view_by_get(request,id):                                # User Template view by GET

    if(auth_user(request)):
        data = super_plan_forms.objects.filter(id=id).get()
        tdate = date.today()
        logo=""
        if(data.company_logo):
            logo=data.company_logo.url
        return render(request,'template/template1.html',{"data":data,"logo":logo,"year":tdate.year})
    else:
        return redirect('/login')








def incomplete_superplan_bookings_check(request):                                # User All incomplete superplan form Checking

    if(auth_user(request)):
        data = super_plan_forms.objects.filter(user=request.session['user'],current_fillup_position__lt=13)
        if(data):
            return render(request,'user-all-incomplete-superplan-bookings.html',{"bookings":data})
        else:
            return redirect('user_form_1')

    else:
        return redirect('/login')










def user_all_incomplete_superplan_bookings(request):                                # User All incomplete superplan form

    if(auth_user(request)):
        data = super_plan_forms.objects.filter(user=request.session['user'],current_fillup_position__lt=10)
        return render(request,'user-all-incomplete-superplan-bookings.html',{"bookings":data})
    else:
        return redirect('/login')








def user_incomplete_superplan_by_get(request,id):                                # User incomplete superplan form by GET

    if(auth_user(request)):
        now = datetime.datetime.now()
        year = now.year
        years = [i for i in range(year-5,year+11)]
        request.session["years"]=years

        book=super_plan_forms.objects.filter(id=int(id),user=request.session['user']).get()
        if(book):
            request.session["form"] = book.id
            form_url = 'user-form'+str((book.current_fillup_position)+1)+'.html'

            ind_types = Industries.objects.all()


            if(book.industry_type):
                ind_an=None
                ind_gw=None
                ind_an_c=Industry_analysis.objects.filter(industry__pk=book.industry_type).count()
                ind_gw_c=Industry_growth_drivers.objects.filter(industry__pk=book.industry_type).count()
                if(ind_an_c):
                    ind_an=Industry_analysis.objects.filter(industry__pk=book.industry_type).get()
                if(ind_gw_c):
                    ind_gw=Industry_growth_drivers.objects.filter(industry__pk=book.industry_type).get()


                return render(request,form_url,{"data":book,"industries":ind_types,"industry_analysis":ind_an,"industry_growth_drivers":ind_gw})
            else:
                return render(request,form_url,{"data":book,"industries":ind_types})
        else:
            return redirect('/login')
    else:
        return redirect('/login')




def ajax_call_delete_incomplete_booking(request):                                   # AJAX call DELETE incomplete booking - By User
    if(auth_user(request) and request.method=="POST"):
        booking = super_plan_forms.objects.filter(id=request.POST['id'],user=request.session['user'])
        if(booking):
            booking.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})







def user_template_view_1(request):                                # User View Template 1

    if(auth_user(request)):
        return render(request,'template/tem-1.html')
    else:
        return redirect('/login')



#---------------------------------------------------------------------- Debugging--------------------------------------------

def test(request):
    data=super_plan_forms_multiple_inputs.objects.all()
    return render(request,'print_data.html',{'datas':data})

def test_xl(request):
    data=super_plan_forms_multiple_inputs_xl.objects.all()
    return render(request,'print_data_xl.html',{'datas':data})

def test_image(request):
    data=super_plan_forms_multiple_images.objects.all()
    return render(request,'print_image.html',{'datas':data})

def test_pr(request):
    data=super_plan_projection.objects.all()
    return render(request,'print_projection.html',{'datas':data})

def reset_db(request):
    #data1=super_plan_forms_multiple_inputs.objects.all()
    data2=super_plan_forms_multiple_images.objects.all()
    data3=super_plan_forms_multiple_inputs_xl.objects.all()

    #data1.delete()
    data2.delete()
    data3.delete()

    return HttpResponse(request,"Done !")







#----------------------------------------------------------------------------------------------------------------------








    #-------------------------------------------------- XL file operation ---------------------------


def xl_file_find(request):
    name="form1.xlsx"
    path=settings.MEDIA_ROOT
    for root, dirs, files in os.walk(path):
        if name in files:
            return HttpResponse("File Found !")
    return HttpResponse("Not Found !")



def perc_to_amount(n,v):
    if(v.endswith("%")):
        v=v.replace("%","")
        try:
            v=float(v)
            n=float(n)
            return[((((v/100)*n))+n),v]
        except:
            return [n,0]
    else:
        try:
            v=float(v)
            n=float(n)
            return [n+v,((v/n)*100)]
        except:
            return [n,0]




def nperc_to_amount(n,v):
    if(v.endswith("%")):
        v=v.replace("%","")
        try:
            v=float(v)
            n=float(n)
            return[((((v/100)*n))+n),((v/100)*n)]
        except:
            return [n,0]
    else:
        try:
            v=float(v)
            n=float(n)
            return [n+v,v]
        except:
            return [n,0]




def new_xl_get(request,id):

    path_u=os.path.join(settings.MEDIA_ROOT,"user_xl")
    path_xl=os.path.join(path_u,str(id))
    if(not os.path.exists(path_xl)):
        os.mkdir(path_xl)


    new_xl = os.path.join(path_xl,"superplan.xlsx")
    copyfile(settings.MEDIA_ROOT+"/no_historicals.xlsx",new_xl)

    bv=super_plan_forms.objects.filter(id=int(id)).get()
    if(bv):

        wb = load_workbook(new_xl)


#--------------------------------- Balance sheet -----------------------------------------------------------
        s1 = wb["Balance Sheet"]

        n=0
        if(bv.share_capital):
            if(bv.share_capital.f_1):
                n=bv.share_capital.f_1
                s1["J6"]=float(n)

            if(bv.share_capital.f_2):
                n,r=nperc_to_amount(n,bv.share_capital.f_2)
                s1["K6"]=r

            if(bv.share_capital.f_3):
                n,r=nperc_to_amount(n,bv.share_capital.f_3)
                s1["L6"]=r

            if(bv.share_capital.f_4):
                n,r=nperc_to_amount(n,bv.share_capital.f_4)
                s1["M6"]=r

            if(bv.share_capital.f_5):
                n,r=nperc_to_amount(n,bv.share_capital.f_5)
                s1["N6"]=r




        n=0
        if(bv.equity_funds_raised):
            if(bv.equity_funds_raised.f_1):
                n=bv.equity_funds_raised.f_1
                s1["J8"]=float(n)

            if(bv.equity_funds_raised.f_2):
                n,r=nperc_to_amount(n,bv.equity_funds_raised.f_2)
                s1["K8"]=r

            if(bv.equity_funds_raised.f_3):
                n,r=nperc_to_amount(n,bv.equity_funds_raised.f_3)
                s1["L8"]=r

            if(bv.equity_funds_raised.f_4):
                n,r=nperc_to_amount(n,bv.equity_funds_raised.f_4)
                s1["M8"]=r

            if(bv.equity_funds_raised.f_5):
                n,r=nperc_to_amount(n,bv.equity_funds_raised.f_5)
                s1["N8"]=r



        n=0
        if(bv.deferred_tax_liabilities):
            if(bv.deferred_tax_liabilities.f_1):
                n=bv.deferred_tax_liabilities.f_1
                s1["J14"]=float(n)

            if(bv.deferred_tax_liabilities.f_2):
                n,r=perc_to_amount(n,bv.deferred_tax_liabilities.f_2)
                s1["K14"]=r/100

            if(bv.deferred_tax_liabilities.f_3):
                n,r=perc_to_amount(n,bv.deferred_tax_liabilities.f_3)
                s1["L14"]=r/100

            if(bv.deferred_tax_liabilities.f_4):
                n,r=perc_to_amount(n,bv.deferred_tax_liabilities.f_4)
                s1["M14"]=r/100

            if(bv.deferred_tax_liabilities.f_5):
                n,r=perc_to_amount(n,bv.deferred_tax_liabilities.f_5)
                s1["N14"]=r/100



        n=0
        if(bv.long_term_provisions_growth_or_amount):
            if(bv.long_term_provisions_growth_or_amount.f_1):
                n=bv.long_term_provisions_growth_or_amount.f_1
                s1["J15"]=float(n)

            if(bv.long_term_provisions_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.long_term_provisions_growth_or_amount.f_2)
                s1["K15"]=r/100

            if(bv.long_term_provisions_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.long_term_provisions_growth_or_amount.f_3)
                s1["L15"]=r/100

            if(bv.long_term_provisions_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.long_term_provisions_growth_or_amount.f_4)
                s1["M15"]=r/100

            if(bv.long_term_provisions_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.long_term_provisions_growth_or_amount.f_5)
                s1["N15"]=r/100




        n=0
        if(bv.other_non_current_liabilities_growth_or_amount):
            if(bv.other_non_current_liabilities_growth_or_amount.f_1):
                n=bv.other_non_current_liabilities_growth_or_amount.f_1
                s1["J16"]=float(n)

            if(bv.other_non_current_liabilities_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.other_non_current_liabilities_growth_or_amount.f_2)
                s1["K16"]=r/100

            if(bv.other_non_current_liabilities_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.other_non_current_liabilities_growth_or_amount.f_3)
                s1["L16"]=r/100

            if(bv.other_non_current_liabilities_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.other_non_current_liabilities_growth_or_amount.f_4)
                s1["M16"]=r/100

            if(bv.other_non_current_liabilities_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.other_non_current_liabilities_growth_or_amount.f_5)
                s1["N16"]=r/100




        n=0
        if(bv.short_term_borrowings_growth_or_amount):
            if(bv.short_term_borrowings_growth_or_amount.f_1):
                n=bv.short_term_borrowings_growth_or_amount.f_1
                s1["J20"]=float(n)

            if(bv.short_term_borrowings_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.short_term_borrowings_growth_or_amount.f_2)
                s1["K20"]=r/100

            if(bv.short_term_borrowings_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.short_term_borrowings_growth_or_amount.f_3)
                s1["L20"]=r/100

            if(bv.short_term_borrowings_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.short_term_borrowings_growth_or_amount.f_4)
                s1["M20"]=r/100

            if(bv.short_term_borrowings_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.short_term_borrowings_growth_or_amount.f_5)
                s1["N20"]=r/100





        n=0
        if(bv.short_term_provisions_growth_or_amount):
            if(bv.short_term_provisions_growth_or_amount.f_1):
                n=bv.short_term_provisions_growth_or_amount.f_1
                s1["J21"]=float(n)

            if(bv.short_term_provisions_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.short_term_provisions_growth_or_amount.f_2)
                s1["K21"]=r/100

            if(bv.short_term_provisions_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.short_term_provisions_growth_or_amount.f_3)
                s1["L21"]=r/100

            if(bv.short_term_provisions_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.short_term_provisions_growth_or_amount.f_4)
                s1["M21"]=r/100

            if(bv.short_term_provisions_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.short_term_provisions_growth_or_amount.f_5)
                s1["N21"]=r/100



        n=0
        if(bv.sundry_creditors_no_of_days):
            if(bv.sundry_creditors_no_of_days.f_1):
                n=bv.sundry_creditors_no_of_days.f_1
                s1["J22"]=int(n)

            if(bv.sundry_creditors_no_of_days.f_2):
                n=bv.sundry_creditors_no_of_days.f_2
                s1["K22"]=int(n)

            if(bv.sundry_creditors_no_of_days.f_3):
                n=bv.sundry_creditors_no_of_days.f_3
                s1["L22"]=int(n)

            if(bv.sundry_creditors_no_of_days.f_4):
                n=bv.sundry_creditors_no_of_days.f_4
                s1["M22"]=int(n)

            if(bv.sundry_creditors_no_of_days.f_5):
                n=bv.sundry_creditors_no_of_days.f_5
                s1["N22"]=int(n)





        n=0
        if(bv.other_current_liabilities_growth_or_amount):
            if(bv.other_current_liabilities_growth_or_amount.f_1):
                n=bv.other_current_liabilities_growth_or_amount.f_1
                s1["J23"]=float(n)

            if(bv.other_current_liabilities_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.other_current_liabilities_growth_or_amount.f_2)
                s1["K23"]=r/100

            if(bv.other_current_liabilities_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.other_current_liabilities_growth_or_amount.f_3)
                s1["L23"]=r/100

            if(bv.other_current_liabilities_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.other_current_liabilities_growth_or_amount.f_4)
                s1["M23"]=r/100

            if(bv.other_current_liabilities_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.other_current_liabilities_growth_or_amount.f_5)
                s1["N23"]=r/100



        n=0
        if(bv.intangible_assets_growth_or_amount):
            if(bv.intangible_assets_growth_or_amount.f_1):
                n=bv.intangible_assets_growth_or_amount.f_1
                s1["J33"]=float(n)

            if(bv.intangible_assets_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.intangible_assets_growth_or_amount.f_2)
                s1["K33"]=r/100

            if(bv.intangible_assets_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.intangible_assets_growth_or_amount.f_3)
                s1["L33"]=r/100

            if(bv.intangible_assets_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.intangible_assets_growth_or_amount.f_4)
                s1["M33"]=r/100

            if(bv.intangible_assets_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.intangible_assets_growth_or_amount.f_5)
                s1["N33"]=r/100




        n=0
        if(bv.long_term_loans_and_advances_growth_or_amount):
            if(bv.long_term_loans_and_advances_growth_or_amount.f_1):
                n=bv.long_term_loans_and_advances_growth_or_amount.f_1
                s1["J34"]=float(n)

            if(bv.long_term_loans_and_advances_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.long_term_loans_and_advances_growth_or_amount.f_2)
                s1["K34"]=r/100

            if(bv.long_term_loans_and_advances_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.long_term_loans_and_advances_growth_or_amount.f_3)
                s1["L34"]=r/100

            if(bv.long_term_loans_and_advances_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.long_term_loans_and_advances_growth_or_amount.f_4)
                s1["M34"]=r/100

            if(bv.long_term_loans_and_advances_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.long_term_loans_and_advances_growth_or_amount.f_5)
                s1["N34"]=r/100



        n=0
        if(bv.long_term_investments_growth_or_amount):
            if(bv.long_term_investments_growth_or_amount.f_1):
                n=bv.long_term_investments_growth_or_amount.f_1
                s1["J35"]=float(n)

            if(bv.long_term_investments_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.long_term_investments_growth_or_amount.f_2)
                s1["K35"]=r/100

            if(bv.long_term_investments_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.long_term_investments_growth_or_amount.f_3)
                s1["L35"]=r/100

            if(bv.long_term_investments_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.long_term_investments_growth_or_amount.f_4)
                s1["M35"]=r/100

            if(bv.long_term_investments_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.long_term_investments_growth_or_amount.f_5)
                s1["N35"]=r/100





        n=0
        if(bv.deferred_tax_liabilities):
            if(bv.deferred_tax_liabilities.f_1):
                n=bv.deferred_tax_liabilities.f_1
                s1["J36"]=float(n)

            if(bv.deferred_tax_liabilities.f_2):
                n,r=perc_to_amount(n,bv.deferred_tax_liabilities.f_2)
                s1["K36"]=r/100

            if(bv.deferred_tax_liabilities.f_3):
                n,r=perc_to_amount(n,bv.deferred_tax_liabilities.f_3)
                s1["L36"]=r/100

            if(bv.deferred_tax_liabilities.f_4):
                n,r=perc_to_amount(n,bv.deferred_tax_liabilities.f_4)
                s1["M36"]=r/100

            if(bv.deferred_tax_liabilities.f_5):
                n,r=perc_to_amount(n,bv.deferred_tax_liabilities.f_5)
                s1["N36"]=r/100




        n=0
        if(bv.other_non_current_assets_growth_or_amount):
            if(bv.other_non_current_assets_growth_or_amount.f_1):
                n=bv.other_non_current_assets_growth_or_amount.f_1
                s1["J37"]=float(n)

            if(bv.other_non_current_assets_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.other_non_current_assets_growth_or_amount.f_2)
                s1["K37"]=r/100

            if(bv.other_non_current_assets_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.other_non_current_assets_growth_or_amount.f_3)
                s1["L37"]=r/100

            if(bv.other_non_current_assets_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.other_non_current_assets_growth_or_amount.f_4)
                s1["M37"]=r/100

            if(bv.other_non_current_assets_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.other_non_current_assets_growth_or_amount.f_5)
                s1["N37"]=r/100






        n=0
        if(bv.sundry_debtors_no_of_days):
            if(bv.sundry_debtors_no_of_days.f_1):
                n=bv.sundry_debtors_no_of_days.f_1
                s1["J43"]=int(n)

            if(bv.sundry_debtors_no_of_days.f_2):
                n=bv.sundry_debtors_no_of_days.f_2
                s1["K43"]=int(n)

            if(bv.sundry_debtors_no_of_days.f_3):
                n=bv.sundry_debtors_no_of_days.f_3
                s1["L43"]=int(n)

            if(bv.sundry_debtors_no_of_days.f_4):
                n=bv.sundry_debtors_no_of_days.f_4
                s1["M43"]=int(n)

            if(bv.sundry_debtors_no_of_days.f_5):
                n=bv.sundry_debtors_no_of_days.f_5
                s1["N43"]=int(n)






        n=0
        if(bv.inventory_no_of_days):
            if(bv.inventory_no_of_days.f_1):
                n=bv.inventory_no_of_days.f_1
                s1["J44"]=int(n)

            if(bv.inventory_no_of_days.f_2):
                n=bv.inventory_no_of_days.f_2
                s1["K44"]=int(n)

            if(bv.inventory_no_of_days.f_3):
                n=bv.inventory_no_of_days.f_3
                s1["L44"]=int(n)

            if(bv.inventory_no_of_days.f_4):
                n=bv.inventory_no_of_days.f_4
                s1["M44"]=int(n)

            if(bv.inventory_no_of_days.f_5):
                n=bv.inventory_no_of_days.f_5
                s1["N44"]=int(n)






        n=0
        if(bv.short_term_investments_growth_or_amount):
            if(bv.short_term_investments_growth_or_amount.f_1):
                n=bv.short_term_investments_growth_or_amount.f_1
                s1["J45"]=float(n)

            if(bv.short_term_investments_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.short_term_investments_growth_or_amount.f_2)
                s1["K45"]=r/100

            if(bv.short_term_investments_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.short_term_investments_growth_or_amount.f_3)
                s1["L45"]=r/100

            if(bv.short_term_investments_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.short_term_investments_growth_or_amount.f_4)
                s1["M45"]=r/100

            if(bv.short_term_investments_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.short_term_investments_growth_or_amount.f_5)
                s1["N45"]=r/100





        n=0
        if(bv.short_term_loans_and_advances_growth_or_amount):
            if(bv.short_term_loans_and_advances_growth_or_amount.f_1):
                n=bv.short_term_loans_and_advances_growth_or_amount.f_1
                s1["J46"]=float(n)

            if(bv.short_term_loans_and_advances_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.short_term_loans_and_advances_growth_or_amount.f_2)
                s1["K46"]=r/100

            if(bv.short_term_loans_and_advances_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.short_term_loans_and_advances_growth_or_amount.f_3)
                s1["L46"]=r/100

            if(bv.short_term_loans_and_advances_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.short_term_loans_and_advances_growth_or_amount.f_4)
                s1["M46"]=r/100

            if(bv.short_term_loans_and_advances_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.short_term_loans_and_advances_growth_or_amount.f_5)
                s1["N46"]=r/100





        n=0
        if(bv.other_current_assets_growth_or_amount):
            if(bv.other_current_assets_growth_or_amount.f_1):
                n=bv.other_current_assets_growth_or_amount.f_1
                s1["J47"]=float(n)

            if(bv.other_current_assets_growth_or_amount.f_2):
                n,r=perc_to_amount(n,bv.other_current_assets_growth_or_amount.f_2)
                s1["K47"]=r/100

            if(bv.other_current_assets_growth_or_amount.f_3):
                n,r=perc_to_amount(n,bv.other_current_assets_growth_or_amount.f_3)
                s1["L47"]=r/100

            if(bv.other_current_assets_growth_or_amount.f_4):
                n,r=perc_to_amount(n,bv.other_current_assets_growth_or_amount.f_4)
                s1["M47"]=r/100

            if(bv.other_current_assets_growth_or_amount.f_5):
                n,r=perc_to_amount(n,bv.other_current_assets_growth_or_amount.f_5)
                s1["N47"]=r/100





        yr1 = bv.balance_sheet_years.f_1
        yr2 = bv.balance_sheet_years.f_2
        yr3 = bv.balance_sheet_years.f_3
        yr4 = bv.balance_sheet_years.f_4
        yr5 = bv.balance_sheet_years.f_5

        s1["C3"]=yr1
        s1["D3"]=yr2
        s1["E3"]=yr3
        s1["F3"]=yr4
        s1["G3"]=yr5

        s1["C55"]=yr1
        s1["D55"]=yr2
        s1["E55"]=yr3
        s1["F55"]=yr4
        s1["G55"]=yr5

        s1["J3"]=yr1
        s1["K3"]=yr2
        s1["L3"]=yr3
        s1["M3"]=yr4
        s1["N3"]=yr5








#--------------------------------- Balance sheet end -----------------------------------------------------------

        s2 = wb["Expenses Projection"]

        n=0
        if(bv.direct_material_units):
            if(bv.direct_material_units.f_1):
                n=bv.direct_material_units.f_1
                s2["J8"]=float(n)

            if(bv.direct_material_units.f_2):
                n,r=perc_to_amount(n,bv.direct_material_units.f_2)
                s2["K8"]=r/100

            if(bv.direct_material_units.f_3):
                n,r=perc_to_amount(n,bv.direct_material_units.f_3)
                s2["L8"]=r/100

            if(bv.direct_material_units.f_4):
                n,r=perc_to_amount(n,bv.direct_material_units.f_4)
                s2["M8"]=r/100

            if(bv.direct_material_units.f_5):
                n,r=perc_to_amount(n,bv.direct_material_units.f_5)
                s2["N8"]=r/100




        n=0
        if(bv.direct_material_average_cost_per_unit):
            if(bv.direct_material_average_cost_per_unit.f_1):
                n=bv.direct_material_average_cost_per_unit.f_1
                s2["J9"]=float(n)

            if(bv.direct_material_average_cost_per_unit.f_2):
                n,r=perc_to_amount(n,bv.direct_material_average_cost_per_unit.f_2)
                s2["K9"]=r/100

            if(bv.direct_material_average_cost_per_unit.f_3):
                n,r=perc_to_amount(n,bv.direct_material_average_cost_per_unit.f_3)
                s2["L9"]=r/100

            if(bv.direct_material_average_cost_per_unit.f_4):
                n,r=perc_to_amount(n,bv.direct_material_average_cost_per_unit.f_4)
                s2["M9"]=r/100

            if(bv.direct_material_average_cost_per_unit.f_5):
                n,r=perc_to_amount(n,bv.direct_material_average_cost_per_unit.f_5)
                s2["N9"]=r/100



        n=0
        if(bv.direct_labour_no_of_employees):
            if(bv.direct_labour_no_of_employees.f_1):
                n=bv.direct_labour_no_of_employees.f_1
                s2["J13"]=float(n)

            if(bv.direct_labour_no_of_employees.f_2):
                n,r=perc_to_amount(n,bv.direct_labour_no_of_employees.f_2)
                s2["K13"]=r/100

            if(bv.direct_labour_no_of_employees.f_3):
                n,r=perc_to_amount(n,bv.direct_labour_no_of_employees.f_3)
                s2["L13"]=r/100

            if(bv.direct_labour_no_of_employees.f_4):
                n,r=perc_to_amount(n,bv.direct_labour_no_of_employees.f_4)
                s2["M13"]=r/100

            if(bv.direct_labour_no_of_employees.f_5):
                n,r=perc_to_amount(n,bv.direct_labour_no_of_employees.f_5)
                s2["N13"]=r/100



        n=0
        if(bv.direct_labour_average_cost_per_employee):
            if(bv.direct_labour_average_cost_per_employee.f_1):
                n=bv.direct_labour_average_cost_per_employee.f_1
                s2["J14"]=float(n)

            if(bv.direct_labour_average_cost_per_employee.f_2):
                n,r=perc_to_amount(n,bv.direct_labour_average_cost_per_employee.f_2)
                s2["K14"]=r/100

            if(bv.direct_labour_average_cost_per_employee.f_3):
                n,r=perc_to_amount(n,bv.direct_labour_average_cost_per_employee.f_3)
                s2["L14"]=r/100

            if(bv.direct_labour_average_cost_per_employee.f_4):
                n,r=perc_to_amount(n,bv.direct_labour_average_cost_per_employee.f_4)
                s2["M14"]=r/100

            if(bv.direct_labour_average_cost_per_employee.f_5):
                n,r=perc_to_amount(n,bv.direct_labour_average_cost_per_employee.f_5)
                s2["N14"]=r/100



        n=0
        if(bv.direct_expenses):
            if(bv.direct_expenses.f_1):
                n=bv.direct_expenses.f_1
                s2["J17"]=float(n)

            if(bv.direct_expenses.f_2):
                n,r=perc_to_amount(n,bv.direct_expenses.f_2)
                s2["K17"]=r/100

            if(bv.direct_expenses.f_3):
                n,r=perc_to_amount(n,bv.direct_expenses.f_3)
                s2["L17"]=r/100

            if(bv.direct_expenses.f_4):
                n,r=perc_to_amount(n,bv.direct_expenses.f_4)
                s2["M17"]=r/100

            if(bv.direct_expenses.f_5):
                n,r=perc_to_amount(n,bv.direct_expenses.f_5)
                s2["N17"]=r/100



        n=0
        if(bv.other_direct_expenses_1):
            if(bv.other_direct_expenses_1.f_2):
                n=bv.other_direct_expenses_1.f_2
                s2["J18"]=float(n)

            if(bv.other_direct_expenses_1.f_3):
                n,r=perc_to_amount(n,bv.other_direct_expenses_1.f_3)
                s2["K18"]=r/100

            if(bv.other_direct_expenses_1.f_4):
                n,r=perc_to_amount(n,bv.other_direct_expenses_1.f_4)
                s2["L18"]=r/100

            if(bv.other_direct_expenses_1.f_5):
                n,r=perc_to_amount(n,bv.other_direct_expenses_1.f_5)
                s2["M18"]=r/100

            if(bv.other_direct_expenses_1.f_6):
                n,r=perc_to_amount(n,bv.other_direct_expenses_1.f_6)
                s2["N18"]=r/100




        n=0
        if(bv.other_direct_expenses_2):
            if(bv.other_direct_expenses_2.f_2):
                n=bv.other_direct_expenses_2.f_2
                s2["J19"]=float(n)

            if(bv.other_direct_expenses_2.f_3):
                n,r=perc_to_amount(n,bv.other_direct_expenses_2.f_3)
                s2["K19"]=r/100

            if(bv.other_direct_expenses_2.f_4):
                n,r=perc_to_amount(n,bv.other_direct_expenses_2.f_4)
                s2["L19"]=r/100

            if(bv.other_direct_expenses_2.f_5):
                n,r=perc_to_amount(n,bv.other_direct_expenses_2.f_5)
                s2["M19"]=r/100

            if(bv.other_direct_expenses_2.f_6):
                n,r=perc_to_amount(n,bv.other_direct_expenses_2.f_6)
                s2["N19"]=r/100




        n=0
        if(bv.other_direct_expenses_3):
            if(bv.other_direct_expenses_3.f_2):
                n=bv.other_direct_expenses_3.f_2
                s2["J20"]=float(n)

            if(bv.other_direct_expenses_3.f_3):
                n,r=perc_to_amount(n,bv.other_direct_expenses_3.f_3)
                s2["K20"]=r/100

            if(bv.other_direct_expenses_3.f_4):
                n,r=perc_to_amount(n,bv.other_direct_expenses_3.f_4)
                s2["L20"]=r/100

            if(bv.other_direct_expenses_3.f_5):
                n,r=perc_to_amount(n,bv.other_direct_expenses_3.f_5)
                s2["M20"]=r/100

            if(bv.other_direct_expenses_3.f_6):
                n,r=perc_to_amount(n,bv.other_direct_expenses_3.f_6)
                s2["N20"]=r/100







        n=0
        if(bv.administration_no_of_employees):
            if(bv.administration_no_of_employees.f_1):
                n=bv.administration_no_of_employees.f_1
                s2["J27"]=float(n)

            if(bv.administration_no_of_employees.f_2):
                n,r=perc_to_amount(n,bv.administration_no_of_employees.f_2)
                s2["K27"]=r/100

            if(bv.administration_no_of_employees.f_3):
                n,r=perc_to_amount(n,bv.administration_no_of_employees.f_3)
                s2["L27"]=r/100

            if(bv.administration_no_of_employees.f_4):
                n,r=perc_to_amount(n,bv.administration_no_of_employees.f_4)
                s2["M27"]=r/100

            if(bv.administration_no_of_employees.f_5):
                n,r=perc_to_amount(n,bv.administration_no_of_employees.f_5)
                s2["N27"]=r/100




        n=0
        if(bv.administration_average_cost_per_employee):
            if(bv.administration_average_cost_per_employee.f_1):
                n=bv.administration_average_cost_per_employee.f_1
                s2["J28"]=float(n)

            if(bv.administration_average_cost_per_employee.f_2):
                n,r=perc_to_amount(n,bv.administration_average_cost_per_employee.f_2)
                s2["K28"]=r/100

            if(bv.administration_average_cost_per_employee.f_3):
                n,r=perc_to_amount(n,bv.administration_average_cost_per_employee.f_3)
                s2["L28"]=r/100

            if(bv.administration_average_cost_per_employee.f_4):
                n,r=perc_to_amount(n,bv.administration_average_cost_per_employee.f_4)
                s2["M28"]=r/100

            if(bv.administration_average_cost_per_employee.f_5):
                n,r=perc_to_amount(n,bv.administration_average_cost_per_employee.f_5)
                s2["N28"]=r/100



        n=0
        if(bv.selling_and_distribution_no_of_employees):
            if(bv.selling_and_distribution_no_of_employees.f_1):
                n=bv.selling_and_distribution_no_of_employees.f_1
                s2["J32"]=float(n)

            if(bv.selling_and_distribution_no_of_employees.f_2):
                n,r=perc_to_amount(n,bv.selling_and_distribution_no_of_employees.f_2)
                s2["K32"]=r/100

            if(bv.selling_and_distribution_no_of_employees.f_3):
                n,r=perc_to_amount(n,bv.selling_and_distribution_no_of_employees.f_3)
                s2["L32"]=r/100

            if(bv.selling_and_distribution_no_of_employees.f_4):
                n,r=perc_to_amount(n,bv.selling_and_distribution_no_of_employees.f_4)
                s2["M32"]=r/100

            if(bv.selling_and_distribution_no_of_employees.f_5):
                n,r=perc_to_amount(n,bv.selling_and_distribution_no_of_employees.f_5)
                s2["N32"]=r/100




        n=0
        if(bv.selling_and_distribution_average_cost_per_employee):
            if(bv.selling_and_distribution_average_cost_per_employee.f_1):
                n=bv.selling_and_distribution_average_cost_per_employee.f_1
                s2["J33"]=float(n)

            if(bv.selling_and_distribution_average_cost_per_employee.f_2):
                n,r=perc_to_amount(n,bv.selling_and_distribution_average_cost_per_employee.f_2)
                s2["K33"]=r/100

            if(bv.selling_and_distribution_average_cost_per_employee.f_3):
                n,r=perc_to_amount(n,bv.selling_and_distribution_average_cost_per_employee.f_3)
                s2["L33"]=r/100

            if(bv.selling_and_distribution_average_cost_per_employee.f_4):
                n,r=perc_to_amount(n,bv.selling_and_distribution_average_cost_per_employee.f_4)
                s2["M33"]=r/100

            if(bv.selling_and_distribution_average_cost_per_employee.f_5):
                n,r=perc_to_amount(n,bv.selling_and_distribution_average_cost_per_employee.f_5)
                s2["N33"]=r/100



        n=0
        if(bv.marketing_no_of_employees):
            if(bv.marketing_no_of_employees.f_1):
                n=bv.marketing_no_of_employees.f_1
                s2["J37"]=float(n)

            if(bv.marketing_no_of_employees.f_2):
                n,r=perc_to_amount(n,bv.marketing_no_of_employees.f_2)
                s2["K37"]=r/100

            if(bv.marketing_no_of_employees.f_3):
                n,r=perc_to_amount(n,bv.marketing_no_of_employees.f_3)
                s2["L37"]=r/100

            if(bv.marketing_no_of_employees.f_4):
                n,r=perc_to_amount(n,bv.marketing_no_of_employees.f_4)
                s2["M37"]=r/100

            if(bv.marketing_no_of_employees.f_5):
                n,r=perc_to_amount(n,bv.marketing_no_of_employees.f_5)
                s2["N37"]=r/100




        n=0
        if(bv.marketing_average_cost_per_employee):
            if(bv.marketing_average_cost_per_employee.f_1):
                n=bv.marketing_average_cost_per_employee.f_1
                s2["J38"]=float(n)

            if(bv.marketing_average_cost_per_employee.f_2):
                n,r=perc_to_amount(n,bv.marketing_average_cost_per_employee.f_2)
                s2["K38"]=r/100

            if(bv.marketing_average_cost_per_employee.f_3):
                n,r=perc_to_amount(n,bv.marketing_average_cost_per_employee.f_3)
                s2["L38"]=r/100

            if(bv.marketing_average_cost_per_employee.f_4):
                n,r=perc_to_amount(n,bv.marketing_average_cost_per_employee.f_4)
                s2["M38"]=r/100

            if(bv.marketing_average_cost_per_employee.f_5):
                n,r=perc_to_amount(n,bv.marketing_average_cost_per_employee.f_5)
                s2["N38"]=r/100




        n=0
        if(bv.research_and_development_no_of_employees):
            if(bv.research_and_development_no_of_employees.f_1):
                n=bv.research_and_development_no_of_employees.f_1
                s2["J42"]=float(n)

            if(bv.research_and_development_no_of_employees.f_2):
                n,r=perc_to_amount(n,bv.research_and_development_no_of_employees.f_2)
                s2["K42"]=r/100

            if(bv.research_and_development_no_of_employees.f_3):
                n,r=perc_to_amount(n,bv.research_and_development_no_of_employees.f_3)
                s2["L42"]=r/100

            if(bv.research_and_development_no_of_employees.f_4):
                n,r=perc_to_amount(n,bv.research_and_development_no_of_employees.f_4)
                s2["M42"]=r/100

            if(bv.research_and_development_no_of_employees.f_5):
                n,r=perc_to_amount(n,bv.research_and_development_no_of_employees.f_5)
                s2["N42"]=r/100





        n=0
        if(bv.research_and_development_average_cost_per_employee):
            if(bv.research_and_development_average_cost_per_employee.f_1):
                n=bv.research_and_development_average_cost_per_employee.f_1
                s2["J43"]=float(n)

            if(bv.research_and_development_average_cost_per_employee.f_2):
                n,r=perc_to_amount(n,bv.research_and_development_average_cost_per_employee.f_2)
                s2["K43"]=r/100

            if(bv.research_and_development_average_cost_per_employee.f_3):
                n,r=perc_to_amount(n,bv.research_and_development_average_cost_per_employee.f_3)
                s2["L43"]=r/100

            if(bv.research_and_development_average_cost_per_employee.f_4):
                n,r=perc_to_amount(n,bv.research_and_development_average_cost_per_employee.f_4)
                s2["M43"]=r/100

            if(bv.research_and_development_average_cost_per_employee.f_5):
                n,r=perc_to_amount(n,bv.research_and_development_average_cost_per_employee.f_5)
                s2["N43"]=r/100




        n=0
        if(bv.other_employees_1_no_of_employees):
            if(bv.other_employees_1_no_of_employees.f_1):
                n=bv.other_employees_1_no_of_employees.f_1
                s2["J47"]=float(n)

            if(bv.other_employees_1_no_of_employees.f_2):
                n,r=perc_to_amount(n,bv.other_employees_1_no_of_employees.f_2)
                s2["K47"]=r/100

            if(bv.other_employees_1_no_of_employees.f_3):
                n,r=perc_to_amount(n,bv.other_employees_1_no_of_employees.f_3)
                s2["L47"]=r/100

            if(bv.other_employees_1_no_of_employees.f_4):
                n,r=perc_to_amount(n,bv.other_employees_1_no_of_employees.f_4)
                s2["M47"]=r/100

            if(bv.other_employees_1_no_of_employees.f_5):
                n,r=perc_to_amount(n,bv.other_employees_1_no_of_employees.f_5)
                s2["N47"]=r/100




        n=0
        if(bv.other_employees_1_average_cost_per_employee):
            if(bv.other_employees_1_average_cost_per_employee.f_1):
                n=bv.other_employees_1_average_cost_per_employee.f_1
                s2["J48"]=float(n)

            if(bv.other_employees_1_average_cost_per_employee.f_2):
                n,r=perc_to_amount(n,bv.other_employees_1_average_cost_per_employee.f_2)
                s2["K48"]=r/100

            if(bv.other_employees_1_average_cost_per_employee.f_3):
                n,r=perc_to_amount(n,bv.other_employees_1_average_cost_per_employee.f_3)
                s2["L48"]=r/100

            if(bv.other_employees_1_average_cost_per_employee.f_4):
                n,r=perc_to_amount(n,bv.other_employees_1_average_cost_per_employee.f_4)
                s2["M48"]=r/100

            if(bv.other_employees_1_average_cost_per_employee.f_5):
                n,r=perc_to_amount(n,bv.other_employees_1_average_cost_per_employee.f_5)
                s2["N48"]=r/100





        n=0
        if(bv.other_employees_2_no_of_employees):
            if(bv.other_employees_2_no_of_employees.f_1):
                n=bv.other_employees_2_no_of_employees.f_1
                s2["J52"]=float(n)

            if(bv.other_employees_2_no_of_employees.f_2):
                n,r=perc_to_amount(n,bv.other_employees_2_no_of_employees.f_2)
                s2["K52"]=r/100

            if(bv.other_employees_2_no_of_employees.f_3):
                n,r=perc_to_amount(n,bv.other_employees_2_no_of_employees.f_3)
                s2["L52"]=r/100

            if(bv.other_employees_2_no_of_employees.f_4):
                n,r=perc_to_amount(n,bv.other_employees_2_no_of_employees.f_4)
                s2["M52"]=r/100

            if(bv.other_employees_2_no_of_employees.f_5):
                n,r=perc_to_amount(n,bv.other_employees_2_no_of_employees.f_5)
                s2["N52"]=r/100






        n=0
        if(bv.other_employees_2_average_cost_per_employee):
            if(bv.other_employees_2_average_cost_per_employee.f_1):
                n=bv.other_employees_2_average_cost_per_employee.f_1
                s2["J53"]=float(n)

            if(bv.other_employees_2_average_cost_per_employee.f_2):
                n,r=perc_to_amount(n,bv.other_employees_2_average_cost_per_employee.f_2)
                s2["K53"]=r/100

            if(bv.other_employees_2_average_cost_per_employee.f_3):
                n,r=perc_to_amount(n,bv.other_employees_2_average_cost_per_employee.f_3)
                s2["L53"]=r/100

            if(bv.other_employees_2_average_cost_per_employee.f_4):
                n,r=perc_to_amount(n,bv.other_employees_2_average_cost_per_employee.f_4)
                s2["M53"]=r/100

            if(bv.other_employees_2_average_cost_per_employee.f_5):
                n,r=perc_to_amount(n,bv.other_employees_2_average_cost_per_employee.f_5)
                s2["N53"]=r/100




        n=0
        if(bv.other_employees_3_no_of_employees):
            if(bv.other_employees_3_no_of_employees.f_1):
                n=bv.other_employees_3_no_of_employees.f_1
                s2["J57"]=float(n)

            if(bv.other_employees_3_no_of_employees.f_2):
                n,r=perc_to_amount(n,bv.other_employees_3_no_of_employees.f_2)
                s2["K57"]=r/100

            if(bv.other_employees_3_no_of_employees.f_3):
                n,r=perc_to_amount(n,bv.other_employees_3_no_of_employees.f_3)
                s2["L57"]=r/100

            if(bv.other_employees_3_no_of_employees.f_4):
                n,r=perc_to_amount(n,bv.other_employees_3_no_of_employees.f_4)
                s2["M57"]=r/100

            if(bv.other_employees_3_no_of_employees.f_5):
                n,r=perc_to_amount(n,bv.other_employees_3_no_of_employees.f_5)
                s2["N57"]=r/100



        n=0
        if(bv.other_employees_3_average_cost_per_employee):
            if(bv.other_employees_3_average_cost_per_employee.f_1):
                n=bv.other_employees_3_average_cost_per_employee.f_1
                s2["J58"]=float(n)

            if(bv.other_employees_3_average_cost_per_employee.f_2):
                n,r=perc_to_amount(n,bv.other_employees_3_average_cost_per_employee.f_2)
                s2["K58"]=r/100

            if(bv.other_employees_3_average_cost_per_employee.f_3):
                n,r=perc_to_amount(n,bv.other_employees_3_average_cost_per_employee.f_3)
                s2["L58"]=r/100

            if(bv.other_employees_3_average_cost_per_employee.f_4):
                n,r=perc_to_amount(n,bv.other_employees_3_average_cost_per_employee.f_4)
                s2["M58"]=r/100

            if(bv.other_employees_3_average_cost_per_employee.f_5):
                n,r=perc_to_amount(n,bv.other_employees_3_average_cost_per_employee.f_5)
                s2["N58"]=r/100


        n=0
        if(bv.rent):
            if(bv.rent.f_1):
                n=bv.rent.f_1
                s2["J65"]=float(n)

            if(bv.rent.f_2):
                n,r=perc_to_amount(n,bv.rent.f_2)
                s2["K65"]=r/100

            if(bv.rent.f_3):
                n,r=perc_to_amount(n,bv.rent.f_3)
                s2["L65"]=r/100

            if(bv.rent.f_4):
                n,r=perc_to_amount(n,bv.rent.f_4)
                s2["M65"]=r/100

            if(bv.rent.f_5):
                n,r=perc_to_amount(n,bv.rent.f_5)
                s2["N65"]=r/100





        n=0
        if(bv.telephone_expenses):
            if(bv.telephone_expenses.f_1):
                n=bv.telephone_expenses.f_1
                s2["J66"]=float(n)

            if(bv.telephone_expenses.f_2):
                n,r=perc_to_amount(n,bv.telephone_expenses.f_2)
                s2["K66"]=r/100

            if(bv.telephone_expenses.f_3):
                n,r=perc_to_amount(n,bv.telephone_expenses.f_3)
                s2["L66"]=r/100

            if(bv.telephone_expenses.f_4):
                n,r=perc_to_amount(n,bv.telephone_expenses.f_4)
                s2["M66"]=r/100

            if(bv.telephone_expenses.f_5):
                n,r=perc_to_amount(n,bv.telephone_expenses.f_5)
                s2["N66"]=r/100




        n=0
        if(bv.electricity):
            if(bv.electricity.f_1):
                n=bv.electricity.f_1
                s2["J67"]=float(n)

            if(bv.electricity.f_2):
                n,r=perc_to_amount(n,bv.electricity.f_2)
                s2["K67"]=r/100

            if(bv.electricity.f_3):
                n,r=perc_to_amount(n,bv.electricity.f_3)
                s2["L67"]=r/100

            if(bv.electricity.f_4):
                n,r=perc_to_amount(n,bv.electricity.f_4)
                s2["M67"]=r/100

            if(bv.electricity.f_5):
                n,r=perc_to_amount(n,bv.electricity.f_5)
                s2["N67"]=r/100





        n=0
        if(bv.printing_and_stationery):
            if(bv.printing_and_stationery.f_1):
                n=bv.printing_and_stationery.f_1
                s2["J68"]=float(n)

            if(bv.printing_and_stationery.f_2):
                n,r=perc_to_amount(n,bv.printing_and_stationery.f_2)
                s2["K68"]=r/100

            if(bv.printing_and_stationery.f_3):
                n,r=perc_to_amount(n,bv.printing_and_stationery.f_3)
                s2["L68"]=r/100

            if(bv.printing_and_stationery.f_4):
                n,r=perc_to_amount(n,bv.printing_and_stationery.f_4)
                s2["M68"]=r/100

            if(bv.printing_and_stationery.f_5):
                n,r=perc_to_amount(n,bv.printing_and_stationery.f_5)
                s2["N68"]=r/100



        n=0
        if(bv.audit_fees):
            if(bv.audit_fees.f_1):
                n=bv.audit_fees.f_1
                s2["J69"]=float(n)

            if(bv.audit_fees.f_2):
                n,r=perc_to_amount(n,bv.audit_fees.f_2)
                s2["K69"]=r/100

            if(bv.audit_fees.f_3):
                n,r=perc_to_amount(n,bv.audit_fees.f_3)
                s2["L69"]=r/100

            if(bv.audit_fees.f_4):
                n,r=perc_to_amount(n,bv.audit_fees.f_4)
                s2["M69"]=r/100

            if(bv.audit_fees.f_5):
                n,r=perc_to_amount(n,bv.audit_fees.f_5)
                s2["N69"]=r/100


        n=0
        if(bv.other_administration_expenses_1):
            if(bv.other_administration_expenses_1.f_2):
                n=bv.other_administration_expenses_1.f_2
                s2["J70"]=float(n)

            if(bv.other_administration_expenses_1.f_3):
                n,r=perc_to_amount(n,bv.other_administration_expenses_1.f_3)
                s2["K70"]=r/100

            if(bv.other_administration_expenses_1.f_4):
                n,r=perc_to_amount(n,bv.other_administration_expenses_1.f_4)
                s2["L70"]=r/100

            if(bv.other_administration_expenses_1.f_5):
                n,r=perc_to_amount(n,bv.other_administration_expenses_1.f_5)
                s2["M70"]=r/100

            if(bv.other_administration_expenses_1.f_6):
                n,r=perc_to_amount(n,bv.other_administration_expenses_1.f_6)
                s2["N70"]=r/100




        n=0
        if(bv.other_administration_expenses_2):
            if(bv.other_administration_expenses_2.f_2):
                n=bv.other_administration_expenses_2.f_2
                s2["J71"]=float(n)

            if(bv.other_administration_expenses_2.f_3):
                n,r=perc_to_amount(n,bv.other_administration_expenses_2.f_3)
                s2["K71"]=r/100

            if(bv.other_administration_expenses_2.f_4):
                n,r=perc_to_amount(n,bv.other_administration_expenses_2.f_4)
                s2["L71"]=r/100

            if(bv.other_administration_expenses_2.f_5):
                n,r=perc_to_amount(n,bv.other_administration_expenses_2.f_5)
                s2["M71"]=r/100

            if(bv.other_administration_expenses_2.f_6):
                n,r=perc_to_amount(n,bv.other_administration_expenses_2.f_6)
                s2["N71"]=r/100



        n=0
        if(bv.other_administration_expenses_3):
            if(bv.other_administration_expenses_3.f_2):
                n=bv.other_administration_expenses_3.f_2
                s2["J72"]=float(n)

            if(bv.other_administration_expenses_3.f_3):
                n,r=perc_to_amount(n,bv.other_administration_expenses_3.f_3)
                s2["K72"]=r/100

            if(bv.other_administration_expenses_3.f_4):
                n,r=perc_to_amount(n,bv.other_administration_expenses_3.f_4)
                s2["L72"]=r/100

            if(bv.other_administration_expenses_3.f_5):
                n,r=perc_to_amount(n,bv.other_administration_expenses_3.f_5)
                s2["M72"]=r/100

            if(bv.other_administration_expenses_3.f_6):
                n,r=perc_to_amount(n,bv.other_administration_expenses_3.f_6)
                s2["N72"]=r/100




        n=0
        if(bv.digital_marketing_cost):
            if(bv.digital_marketing_cost.f_1):
                n=bv.digital_marketing_cost.f_1
                s2["J78"]=float(n)

            if(bv.digital_marketing_cost.f_2):
                n,r=perc_to_amount(n,bv.digital_marketing_cost.f_2)
                s2["K78"]=r/100

            if(bv.digital_marketing_cost.f_3):
                n,r=perc_to_amount(n,bv.digital_marketing_cost.f_3)
                s2["L78"]=r/100

            if(bv.digital_marketing_cost.f_4):
                n,r=perc_to_amount(n,bv.digital_marketing_cost.f_4)
                s2["M78"]=r/100

            if(bv.digital_marketing_cost.f_5):
                n,r=perc_to_amount(n,bv.digital_marketing_cost.f_5)
                s2["N78"]=r/100


        n=0
        if(bv.sales_commissions):
            if(bv.sales_commissions.f_1):
                n=bv.sales_commissions.f_1
                s2["J79"]=float(n)

            if(bv.sales_commissions.f_2):
                n,r=perc_to_amount(n,bv.sales_commissions.f_2)
                s2["K79"]=r/100

            if(bv.sales_commissions.f_3):
                n,r=perc_to_amount(n,bv.sales_commissions.f_3)
                s2["L79"]=r/100

            if(bv.sales_commissions.f_4):
                n,r=perc_to_amount(n,bv.sales_commissions.f_4)
                s2["M79"]=r/100

            if(bv.sales_commissions.f_5):
                n,r=perc_to_amount(n,bv.sales_commissions.f_5)
                s2["N79"]=r/100



        n=0
        if(bv.travelling_expenses):
            if(bv.travelling_expenses.f_1):
                n=bv.travelling_expenses.f_1
                s2["J80"]=float(n)

            if(bv.travelling_expenses.f_2):
                n,r=perc_to_amount(n,bv.travelling_expenses.f_2)
                s2["K80"]=r/100

            if(bv.travelling_expenses.f_3):
                n,r=perc_to_amount(n,bv.travelling_expenses.f_3)
                s2["L80"]=r/100

            if(bv.travelling_expenses.f_4):
                n,r=perc_to_amount(n,bv.travelling_expenses.f_4)
                s2["M80"]=r/100

            if(bv.travelling_expenses.f_5):
                n,r=perc_to_amount(n,bv.travelling_expenses.f_5)
                s2["N80"]=r/100




        n=0
        if(bv.advertisement):
            if(bv.advertisement.f_1):
                n=bv.advertisement.f_1
                s2["J81"]=float(n)

            if(bv.advertisement.f_2):
                n,r=perc_to_amount(n,bv.advertisement.f_2)
                s2["K81"]=r/100

            if(bv.advertisement.f_3):
                n,r=perc_to_amount(n,bv.advertisement.f_3)
                s2["L81"]=r/100

            if(bv.advertisement.f_4):
                n,r=perc_to_amount(n,bv.advertisement.f_4)
                s2["M81"]=r/100

            if(bv.advertisement.f_5):
                n,r=perc_to_amount(n,bv.advertisement.f_5)
                s2["N81"]=r/100



        n=0
        if(bv.logistics_expenses):
            if(bv.logistics_expenses.f_1):
                n=bv.logistics_expenses.f_1
                s2["J82"]=float(n)

            if(bv.logistics_expenses.f_2):
                n,r=perc_to_amount(n,bv.logistics_expenses.f_2)
                s2["K82"]=r/100

            if(bv.logistics_expenses.f_3):
                n,r=perc_to_amount(n,bv.logistics_expenses.f_3)
                s2["L82"]=r/100

            if(bv.logistics_expenses.f_4):
                n,r=perc_to_amount(n,bv.logistics_expenses.f_4)
                s2["M82"]=r/100

            if(bv.logistics_expenses.f_5):
                n,r=perc_to_amount(n,bv.logistics_expenses.f_5)
                s2["N82"]=r/100



        n=0
        if(bv.other_selling_and_marketing_expenses_1):
            if(bv.other_selling_and_marketing_expenses_1.f_2):
                n=bv.other_selling_and_marketing_expenses_1.f_2
                s2["J83"]=float(n)

            if(bv.other_selling_and_marketing_expenses_1.f_3):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_1.f_3)
                s2["K83"]=r/100

            if(bv.other_selling_and_marketing_expenses_1.f_4):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_1.f_4)
                s2["L83"]=r/100

            if(bv.other_selling_and_marketing_expenses_1.f_5):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_1.f_5)
                s2["M83"]=r/100

            if(bv.other_selling_and_marketing_expenses_1.f_6):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_1.f_6)
                s2["N83"]=r/100



        n=0
        if(bv.other_selling_and_marketing_expenses_2):
            if(bv.other_selling_and_marketing_expenses_2.f_2):
                n=bv.other_selling_and_marketing_expenses_2.f_2
                s2["J84"]=float(n)

            if(bv.other_selling_and_marketing_expenses_2.f_3):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_2.f_3)
                s2["K84"]=r/100

            if(bv.other_selling_and_marketing_expenses_2.f_4):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_2.f_4)
                s2["L84"]=r/100

            if(bv.other_selling_and_marketing_expenses_2.f_5):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_2.f_5)
                s2["M84"]=r/100

            if(bv.other_selling_and_marketing_expenses_2.f_6):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_2.f_6)
                s2["N84"]=r/100



        n=0
        if(bv.other_selling_and_marketing_expenses_3):
            if(bv.other_selling_and_marketing_expenses_3.f_2):
                n=bv.other_selling_and_marketing_expenses_3.f_2
                s2["J85"]=float(n)

            if(bv.other_selling_and_marketing_expenses_3.f_3):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_3.f_3)
                s2["K85"]=r/100

            if(bv.other_selling_and_marketing_expenses_3.f_4):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_3.f_4)
                s2["L85"]=r/100

            if(bv.other_selling_and_marketing_expenses_3.f_5):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_3.f_5)
                s2["M85"]=r/100

            if(bv.other_selling_and_marketing_expenses_3.f_6):
                n,r=perc_to_amount(n,bv.other_selling_and_marketing_expenses_3.f_6)
                s2["N85"]=r/100



        n=0
        if(bv.other_expenses_1):
            if(bv.other_expenses_1.f_2):
                n=bv.other_expenses_1.f_2
                s2["J89"]=float(n)

            if(bv.other_expenses_1.f_3):
                n,r=perc_to_amount(n,bv.other_expenses_1.f_3)
                s2["K89"]=r/100

            if(bv.other_expenses_1.f_4):
                n,r=perc_to_amount(n,bv.other_expenses_1.f_4)
                s2["L89"]=r/100

            if(bv.other_expenses_1.f_5):
                n,r=perc_to_amount(n,bv.other_expenses_1.f_5)
                s2["M89"]=r/100

            if(bv.other_expenses_1.f_6):
                n,r=perc_to_amount(n,bv.other_expenses_1.f_6)
                s2["N89"]=r/100



        n=0
        if(bv.other_expenses_2):
            if(bv.other_expenses_2.f_2):
                n=bv.other_expenses_2.f_2
                s2["J93"]=float(n)

            if(bv.other_expenses_2.f_3):
                n,r=perc_to_amount(n,bv.other_expenses_2.f_3)
                s2["K93"]=r/100

            if(bv.other_expenses_2.f_4):
                n,r=perc_to_amount(n,bv.other_expenses_2.f_4)
                s2["L93"]=r/100

            if(bv.other_expenses_2.f_5):
                n,r=perc_to_amount(n,bv.other_expenses_2.f_5)
                s2["M93"]=r/100

            if(bv.other_expenses_2.f_6):
                n,r=perc_to_amount(n,bv.other_expenses_2.f_6)
                s2["N93"]=r/100



        n=0
        if(bv.income_tax_rate):
            if(bv.income_tax_rate.f_1):
                n,r=perc_to_amount(n,bv.income_tax_rate.f_1)
                s2["J97"]=r

            if(bv.income_tax_rate.f_2):
                n,r=perc_to_amount(n,bv.income_tax_rate.f_2)
                s2["K97"]=r

            if(bv.income_tax_rate.f_3):
                n,r=perc_to_amount(n,bv.income_tax_rate.f_3)
                s2["L97"]=r

            if(bv.income_tax_rate.f_4):
                n,r=perc_to_amount(n,bv.income_tax_rate.f_4)
                s2["M97"]=r

            if(bv.income_tax_rate.f_5):
                n,r=perc_to_amount(n,bv.income_tax_rate.f_5)
                s2["N97"]=r



#--------------------------------- Revenue Projections -----------------------------------------------------------
        s3 = wb["Revenue Projections"]


        n=0
        if(bv.revenue_growth_or_amount_1):
            if(bv.revenue_growth_or_amount_1.f_2):
                n=bv.revenue_growth_or_amount_1.f_2
                s3["J7"]=float(n)

            if(bv.revenue_growth_or_amount_1.f_3):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_1.f_3)
                s3["K7"]=r/100

            if(bv.revenue_growth_or_amount_1.f_4):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_1.f_4)
                s3["L7"]=r/100

            if(bv.revenue_growth_or_amount_1.f_5):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_1.f_5)
                s3["M7"]=r/100

            if(bv.revenue_growth_or_amount_1.f_6):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_1.f_6)
                s3["N7"]=r/100



        n=0
        if(bv.revenue_growth_or_amount_2):
            if(bv.revenue_growth_or_amount_2.f_2):
                n=bv.revenue_growth_or_amount_2.f_2
                s3["J8"]=float(n)

            if(bv.revenue_growth_or_amount_2.f_3):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_2.f_3)
                s3["K8"]=r/100

            if(bv.revenue_growth_or_amount_2.f_4):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_2.f_4)
                s3["L8"]=r/100

            if(bv.revenue_growth_or_amount_2.f_5):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_2.f_5)
                s3["M8"]=r/100

            if(bv.revenue_growth_or_amount_2.f_6):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_2.f_6)
                s3["N8"]=r/100




        n=0
        if(bv.revenue_growth_or_amount_3):
            if(bv.revenue_growth_or_amount_3.f_2):
                n=bv.revenue_growth_or_amount_3.f_2
                s3["J9"]=float(n)

            if(bv.revenue_growth_or_amount_3.f_3):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_3.f_3)
                s3["K9"]=r/100

            if(bv.revenue_growth_or_amount_3.f_4):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_3.f_4)
                s3["L9"]=r/100

            if(bv.revenue_growth_or_amount_3.f_5):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_3.f_5)
                s3["M9"]=r/100

            if(bv.revenue_growth_or_amount_3.f_6):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_3.f_6)
                s3["N9"]=r/100





        n=0
        if(bv.revenue_growth_or_amount_4):
            if(bv.revenue_growth_or_amount_4.f_2):
                n=bv.revenue_growth_or_amount_4.f_2
                s3["J10"]=float(n)

            if(bv.revenue_growth_or_amount_4.f_3):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_4.f_3)
                s3["K10"]=r/100

            if(bv.revenue_growth_or_amount_4.f_4):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_4.f_4)
                s3["L10"]=r/100

            if(bv.revenue_growth_or_amount_4.f_5):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_4.f_5)
                s3["M10"]=r/100

            if(bv.revenue_growth_or_amount_4.f_6):
                n,r=perc_to_amount(n,bv.revenue_growth_or_amount_4.f_6)
                s3["N10"]=r/100



        n=0
        if(bv.other_income_growth_or_amount):
            if(bv.other_income_growth_or_amount.f_1):
                n=bv.other_income_growth_or_amount.f_1
                s3["J14"]=float(n)

            if(bv.other_income_growth_or_amount.f_2):
                n,r=nperc_to_amount(n,bv.other_income_growth_or_amount.f_2)
                s3["K14"]=r

            if(bv.other_income_growth_or_amount.f_3):
                n,r=nperc_to_amount(n,bv.other_income_growth_or_amount.f_3)
                s3["L14"]=r

            if(bv.other_income_growth_or_amount.f_4):
                n,r=nperc_to_amount(n,bv.other_income_growth_or_amount.f_4)
                s3["M14"]=r

            if(bv.other_income_growth_or_amount.f_5):
                n,r=nperc_to_amount(n,bv.other_income_growth_or_amount.f_5)
                s3["N14"]=r



        n=0
        if(bv.realised_foreign_exchange_gain_or_loss):
            if(bv.realised_foreign_exchange_gain_or_loss.f_1):
                n=bv.realised_foreign_exchange_gain_or_loss.f_1
                s3["J15"]=float(n)

            if(bv.realised_foreign_exchange_gain_or_loss.f_2):
                n,r=nperc_to_amount(n,bv.realised_foreign_exchange_gain_or_loss.f_2)
                s3["K15"]=r

            if(bv.realised_foreign_exchange_gain_or_loss.f_3):
                n,r=nperc_to_amount(n,bv.realised_foreign_exchange_gain_or_loss.f_3)
                s3["L15"]=r

            if(bv.realised_foreign_exchange_gain_or_loss.f_4):
                n,r=nperc_to_amount(n,bv.realised_foreign_exchange_gain_or_loss.f_4)
                s3["M15"]=r

            if(bv.realised_foreign_exchange_gain_or_loss.f_5):
                n,r=nperc_to_amount(n,bv.realised_foreign_exchange_gain_or_loss.f_5)
                s3["N15"]=r





#--------------------------------- CAPEX Schedule  -----------------------------------------------------------
        s4 = wb["CAPEX Schedule "]

        n=0
        if(bv.capex_opening_gross):
            if(bv.capex_opening_gross.f_1):
                n=bv.capex_opening_gross.f_1
                s4["C4"]=float(n)



        n=0
        if(bv.capex_additions):
            if(bv.capex_additions.f_1):
                n=bv.capex_additions.f_1
                s4["J5"]=float(n)

            if(bv.capex_additions.f_2):
                n,r=perc_to_amount(n,bv.capex_additions.f_2)
                s4["K5"]=r/100

            if(bv.capex_additions.f_3):
                n,r=perc_to_amount(n,bv.capex_additions.f_3)
                s4["L5"]=r/100

            if(bv.capex_additions.f_4):
                n,r=perc_to_amount(n,bv.capex_additions.f_4)
                s4["M5"]=r/100

            if(bv.capex_additions.f_5):
                n,r=perc_to_amount(n,bv.capex_additions.f_5)
                s4["N5"]=r/100



        n=0
        if(bv.capex_additions_intangible):
            if(bv.capex_additions_intangible.f_1):
                n=bv.capex_additions_intangible.f_1
                s4["J6"]=float(n)

            if(bv.capex_additions_intangible.f_2):
                n,r=perc_to_amount(n,bv.capex_additions_intangible.f_2)
                s4["K6"]=r/100

            if(bv.capex_additions_intangible.f_3):
                n,r=perc_to_amount(n,bv.capex_additions_intangible.f_3)
                s4["L6"]=r/100

            if(bv.capex_additions_intangible.f_4):
                n,r=perc_to_amount(n,bv.capex_additions_intangible.f_4)
                s4["M6"]=r/100

            if(bv.capex_additions_intangible.f_5):
                n,r=perc_to_amount(n,bv.capex_additions_intangible.f_5)
                s4["N6"]=r/100







        n=0
        if(bv.capex_deletions):
            if(bv.capex_deletions.f_1):
                n=bv.capex_deletions.f_1
                s4["J7"]=float(n)

            if(bv.capex_deletions.f_2):
                n,r=perc_to_amount(n,bv.capex_deletions.f_2)
                s4["K7"]=r/100

            if(bv.capex_deletions.f_3):
                n,r=perc_to_amount(n,bv.capex_deletions.f_3)
                s4["L7"]=r/100

            if(bv.capex_deletions.f_4):
                n,r=perc_to_amount(n,bv.capex_deletions.f_4)
                s4["M7"]=r/100

            if(bv.capex_deletions.f_5):
                n,r=perc_to_amount(n,bv.capex_deletions.f_5)
                s4["N7"]=r/100





        n=0
        if(bv.capex_average_depreciation_rate):
            if(bv.capex_average_depreciation_rate.f_1):
                n,r=perc_to_amount(n,bv.capex_average_depreciation_rate.f_1)
                s4["J13"]=r/100

            if(bv.capex_average_depreciation_rate.f_2):
                n,r=perc_to_amount(n,bv.capex_average_depreciation_rate.f_2)
                s4["K13"]=r/100

            if(bv.capex_average_depreciation_rate.f_3):
                n,r=perc_to_amount(n,bv.capex_average_depreciation_rate.f_3)
                s4["L13"]=r/100

            if(bv.capex_average_depreciation_rate.f_4):
                n,r=perc_to_amount(n,bv.capex_average_depreciation_rate.f_4)
                s4["M13"]=r/100

            if(bv.capex_average_depreciation_rate.f_5):
                n,r=perc_to_amount(n,bv.capex_average_depreciation_rate.f_5)
                s4["N13"]=r/100




#--------------------------------- Debt Schedule   -----------------------------------------------------------
        s5 = wb["Debt Schedule "]

        n=0
        if(bv.secured_loans_from_banks):
            if(bv.secured_loans_from_banks.f_1):
                n=bv.secured_loans_from_banks.f_1
                s5["J6"]=float(n)

            if(bv.secured_loans_from_banks.f_2):
                n,r=perc_to_amount(n,bv.secured_loans_from_banks.f_2)
                s5["K6"]=r/100

            if(bv.secured_loans_from_banks.f_3):
                n,r=perc_to_amount(n,bv.secured_loans_from_banks.f_3)
                s5["L6"]=r/100

            if(bv.secured_loans_from_banks.f_4):
                n,r=perc_to_amount(n,bv.secured_loans_from_banks.f_4)
                s5["M6"]=r/100

            if(bv.secured_loans_from_banks.f_5):
                n,r=perc_to_amount(n,bv.secured_loans_from_banks.f_5)
                s5["N6"]=r/100




        n=0
        if(bv.secured_loans_term_loans):
            if(bv.secured_loans_term_loans.f_1):
                n=bv.secured_loans_term_loans.f_1
                s5["J7"]=float(n)

            if(bv.secured_loans_term_loans.f_2):
                n,r=perc_to_amount(n,bv.secured_loans_term_loans.f_2)
                s5["K7"]=r/100

            if(bv.secured_loans_term_loans.f_3):
                n,r=perc_to_amount(n,bv.secured_loans_term_loans.f_3)
                s5["L7"]=r/100

            if(bv.secured_loans_term_loans.f_4):
                n,r=perc_to_amount(n,bv.secured_loans_term_loans.f_4)
                s5["M7"]=r/100

            if(bv.secured_loans_term_loans.f_5):
                n,r=perc_to_amount(n,bv.secured_loans_term_loans.f_5)
                s5["N7"]=r/100




        n=0
        if(bv.secured_loans_other_loans):
            if(bv.secured_loans_other_loans.f_1):
                n=bv.secured_loans_other_loans.f_1
                s5["J8"]=float(n)

            if(bv.secured_loans_other_loans.f_2):
                n,r=perc_to_amount(n,bv.secured_loans_other_loans.f_2)
                s5["K8"]=r/100

            if(bv.secured_loans_other_loans.f_3):
                n,r=perc_to_amount(n,bv.secured_loans_other_loans.f_3)
                s5["L8"]=r/100

            if(bv.secured_loans_other_loans.f_4):
                n,r=perc_to_amount(n,bv.secured_loans_other_loans.f_4)
                s5["M8"]=r/100

            if(bv.secured_loans_other_loans.f_5):
                n,r=perc_to_amount(n,bv.secured_loans_other_loans.f_5)
                s5["N8"]=r/100




        n=0
        if(bv.secured_loans_finance_lease_obligation):
            if(bv.secured_loans_finance_lease_obligation.f_1):
                n=bv.secured_loans_finance_lease_obligation.f_1
                s5["J9"]=float(n)

            if(bv.secured_loans_finance_lease_obligation.f_2):
                n,r=perc_to_amount(n,bv.secured_loans_finance_lease_obligation.f_2)
                s5["K9"]=r/100

            if(bv.secured_loans_finance_lease_obligation.f_3):
                n,r=perc_to_amount(n,bv.secured_loans_finance_lease_obligation.f_3)
                s5["L9"]=r/100

            if(bv.secured_loans_finance_lease_obligation.f_4):
                n,r=perc_to_amount(n,bv.secured_loans_finance_lease_obligation.f_4)
                s5["M9"]=r/100

            if(bv.secured_loans_finance_lease_obligation.f_5):
                n,r=perc_to_amount(n,bv.secured_loans_finance_lease_obligation.f_5)
                s5["N9"]=r/100



        n=0
        if(bv.unsecured_loans):
            if(bv.unsecured_loans.f_1):
                n=bv.unsecured_loans.f_1
                s5["J12"]=float(n)

            if(bv.unsecured_loans.f_2):
                n,r=perc_to_amount(n,bv.unsecured_loans.f_2)
                s5["K12"]=r/100

            if(bv.unsecured_loans.f_3):
                n,r=perc_to_amount(n,bv.unsecured_loans.f_3)
                s5["L12"]=r/100

            if(bv.unsecured_loans.f_4):
                n,r=perc_to_amount(n,bv.unsecured_loans.f_4)
                s5["M12"]=r/100

            if(bv.unsecured_loans.f_5):
                n,r=perc_to_amount(n,bv.unsecured_loans.f_5)
                s5["N12"]=r/100




        n=0
        if(bv.average_interest_rate_debt):
            if(bv.average_interest_rate_debt.f_1):
                n,r=perc_to_amount(n,bv.average_interest_rate_debt.f_1)
                s5["J19"]=r/100

            if(bv.average_interest_rate_debt.f_2):
                n,r=perc_to_amount(n,bv.average_interest_rate_debt.f_2)
                s5["K19"]=r/100

            if(bv.average_interest_rate_debt.f_3):
                n,r=perc_to_amount(n,bv.average_interest_rate_debt.f_3)
                s5["L19"]=r/100

            if(bv.average_interest_rate_debt.f_4):
                n,r=perc_to_amount(n,bv.average_interest_rate_debt.f_4)
                s5["M19"]=r/100

            if(bv.average_interest_rate_debt.f_5):
                n,r=perc_to_amount(n,bv.average_interest_rate_debt.f_5)
                s5["N19"]=r/100










        wb.save(new_xl)
        new_p=settings.MEDIA_URL+"/user_xl/"+str(id)+"superplan.xlsx"
        return HttpResponse("<a href='"+new_p+"'> Click Here to Download !</a>")


    else:
        return HttpResponse("Failed !")







