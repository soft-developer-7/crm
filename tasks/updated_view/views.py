from django.shortcuts import render,redirect
from django.core.serializers import serialize
from django.http import HttpResponse,request,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
import json
from datetime import date
import datetime
from django.http import JsonResponse
from .models import User_db,Pages,Posts,Banners,super_plan_forms,super_plan_forms_multiple_inputs,super_plan_forms_multiple_images,super_plan_forms_multiple_files,super_plan_forms_multiple_inputs_xl,super_plan_form_xl_input
from django.core.paginator import Paginator
from business_management.models import Packs,Industries,User_bookings,Templates,Industries, Industry_analysis,Industry_growth_drivers
from pyexcel_xlsx import get_data
from openpyxl import load_workbook
import os
from django.conf import settings


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


#--------------------------------------------------- User Forms -------------------------------------------


def user_form_1(request):                                # User Form 1

    now = datetime.datetime.now()
    year = now.year
    years = [i for i in range(year-5,year+1)]
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


            file = os.path.join(settings.MEDIA_ROOT, book.historical_xl.url[7:])
            data = get_data(file)

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
                book.save()
                return render(request,'user-form10.html',{"data":book})
            except:
                book.historical_xl=None
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
        book.revenue_growth_1_or = request.POST["revenue_growth_1_or"]

        book.revenue_growth_or_amount_2 = multi_input_insert(request,"revenue_growth_or_amount_2[]")
        book.revenue_growth_2_or = request.POST["revenue_growth_2_or"]

        book.revenue_growth_or_amount_3 = multi_input_insert(request,"revenue_growth_or_amount_3[]")
        book.revenue_growth_3_or = request.POST["revenue_growth_3_or"]

        book.revenue_growth_or_amount_4 = multi_input_insert(request,"revenue_growth_or_amount_4[]")
        book.revenue_growth_4_or = request.POST["revenue_growth_4_or"]

        book.other_income_growth_or_amount = multi_input_insert(request,"other_income_growth_or_amount[]")
        book.other_income_growth_or = request.POST["other_income_growth_or"]

        book.realised_foreign_exchange_gain_or_loss = multi_input_insert(request,"realised_foreign_exchange_gain_or_loss[]")
        book.realised_foreign_exchange_gain_or = request.POST["realised_foreign_exchange_gain_or"]


        book.direct_material_units = multi_input_insert(request,"direct_material_units[]")

        book.direct_material_average_cost_per_unit = multi_input_insert(request,"direct_material_average_cost_per_unit[]")

        book.direct_labour_no_of_employees = multi_input_insert(request,"direct_labour_no_of_employees[]")

        book.direct_labour_average_cost_per_employee = multi_input_insert(request,"direct_labour_average_cost_per_employee[]")

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

        book.current_fillup_position = 10
        book.save()

        return render(request,'user-form11.html',{"data":book})
    else:
        return redirect('/login')










def user_form_11_submit(request):            # User Form 11 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        book.balance_sheet_years = multi_input_insert(request,"balance_sheet_years[]")
        book.share_capital = multi_input_insert(request,"share_capital[]")
        book.reserves_and_surplus = multi_input_insert(request,"reserves_and_surplus[]")
        book.equity_funds_raised = multi_input_insert(request,"equity_funds_raised[]")

        book.secured_loans_from_banks = multi_input_insert(request,"secured_loans_from_banks[]")
        book.secured_loans_term_loans = multi_input_insert(request,"secured_loans_term_loans[]")
        book.secured_loans_other_loans = multi_input_insert(request,"secured_loans_other_loans[]")
        book.secured_loans_finance_lease_obligation = multi_input_insert(request,"secured_loans_finance_lease_obligation[]")

        book.unsecured_loans = multi_input_insert(request,"unsecured_loans[]")
        book.average_interest_rate_debt = multi_input_insert(request,"average_interest_rate_debt[]")

        book.deferred_tax_liabilities  = multi_input_insert(request,"deferred_tax_liabilities[]")

        book.long_term_provisions_growth_or = request.POST["long_term_provisions_growth_or"]
        book.long_term_provisions_growth_or_amount = multi_input_insert(request,"long_term_provisions_growth_or_amount[]")

        book.other_non_current_liabilities_growth_or = request.POST["other_non_current_liabilities_growth_or"]
        book.other_non_current_liabilities_growth_or_amount = multi_input_insert(request,"other_non_current_liabilities_growth_or_amount[]")




        book.short_term_borrowings_growth_or = request.POST["short_term_borrowings_growth_or"]
        book.short_term_borrowings_growth_or_amount = multi_input_insert(request,"short_term_borrowings_growth_or_amount[]")


        book.short_term_provisions_growth_or = request.POST["short_term_provisions_growth_or"]
        book.short_term_provisions_growth_or_amount = multi_input_insert(request,"short_term_provisions_growth_or_amount[]")


        book.sundry_creditors_no_of_days = multi_input_insert(request,"sundry_creditors_no_of_days[]")

        book.other_current_liabilities_growth_or = request.POST["other_current_liabilities_growth_or"]
        book.other_current_liabilities_growth_or_amount = multi_input_insert(request,"other_current_liabilities_growth_or_amount[]")




        book.intangible_assets_growth_or = request.POST["intangible_assets_growth_or"]
        book.intangible_assets_growth_or_amount = multi_input_insert(request,"intangible_assets_growth_or_amount[]")


        book.long_term_loans_and_advances_growth_or = request.POST["long_term_loans_and_advances_growth_or"]
        book.long_term_loans_and_advances_growth_or_amount = multi_input_insert(request,"long_term_loans_and_advances_growth_or_amount[]")


        book.long_term_investments_growth_or = request.POST["long_term_investments_growth_or"]
        book.long_term_investments_growth_or_amount = multi_input_insert(request,"long_term_investments_growth_or_amount[]")

        book.deferred_tax_assets_or = request.POST["deferred_tax_assets_or"]
        book.deferred_tax_assets = multi_input_insert(request,"deferred_tax_assets[]")

        book.other_non_current_assets_growth_or = request.POST["other_non_current_assets_growth_or"]
        book.other_non_current_assets_growth_or_amount = multi_input_insert(request,"other_non_current_assets_growth_or_amount[]")




        book.sundry_debtors_no_of_days = multi_input_insert(request,"sundry_debtors_no_of_days[]")
        book.inventory_no_of_days = multi_input_insert(request,"inventory_no_of_days[]")
        book.short_term_investments_growth_or = request.POST["short_term_investments_growth_or"]
        book.short_term_investments_growth_or_amount = multi_input_insert(request,"short_term_investments_growth_or_amount[]")
        book.short_term_loans_and_advances_growth_or = request.POST["short_term_loans_and_advances_growth_or"]
        book.short_term_loans_and_advances_growth_or_amount = multi_input_insert(request,"short_term_loans_and_advances_growth_or_amount[]")
        book.other_current_assets_growth_or = request.POST["other_current_assets_growth_or"]
        book.other_current_assets_growth_or_amount = multi_input_insert(request,"other_current_assets_growth_or_amount[]")

        book.working_capital = multi_input_insert(request,"working_capital[]")



        book.current_fillup_position = 11
        book.save()


        return render(request,'user-form12.html',{"data":book})
    else:
        return redirect('/login')



















def user_form_12_submit(request):            # User Form 12 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):
        book.capex_opening_gross = multi_input_insert(request,"capex_opening_gross[]")
        book.capex_years = multi_input_insert(request,"capex_years[]")

        book.capex_additions_or=request.POST["capex_additions_or"]
        book.capex_additions = multi_input_insert(request,"capex_additions[]")

        book.capex_additions_intangible_or=request.POST["capex_additions_intangible_or"]
        book.capex_additions_intangible = multi_input_insert(request,"capex_additions_intangible[]")

        book.capex_deletions_or=request.POST["capex_deletions_or"]
        book.capex_deletions = multi_input_insert(request,"capex_deletions[]")


        book.capex_average_depreciation_rate = multi_input_insert(request,"capex_average_depreciation_rate[]")
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
        years = [i for i in range(year-5,year+1)]
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





def test(request):
    data=super_plan_forms_multiple_inputs.objects.all()
    return render(request,'print_data.html',{'datas':data})

def test_xl(request):
    data=super_plan_forms_multiple_inputs_xl.objects.all()
    return render(request,'print_data_xl.html',{'datas':data})

def test_image(request):
    data=super_plan_forms_multiple_images.objects.all()
    return render(request,'print_image.html',{'datas':data})


def reset_db(request):
    #data1=super_plan_forms_multiple_inputs.objects.all()
    data2=super_plan_forms_multiple_images.objects.all()
    data3=super_plan_forms_multiple_inputs_xl.objects.all()

    #data1.delete()
    data2.delete()
    data3.delete()

    return HttpResponse(request,"Done !")
















    #-------------------------------------------------- XL file operation ---------------------------


def xl_file_find(request):
    name="form1.xlsx"
    path=settings.MEDIA_ROOT
    for root, dirs, files in os.walk(path):
        if name in files:
            return HttpResponse("File Found !")
    return HttpResponse("Not Found !")



def new_xl(request):
    name="no_historicals.xlsx"
    path=settings.MEDIA_ROOT
    wb = load_workbook(os.path.join(path,name))
    s1 = wb["Balance Sheet"]
    s1["J14"]=12
    s1["K14"]=12/100
    s1["L14"]=12/100
    s1["M14"]=12/100
    s1["N14"]=12/100

    s1["J15"]=12
    s1["K15"]=12.2/100
    s1["L15"]=12/100
    s1["M15"]=12/100
    s1["N15"]=12/100

    s1["J16"]=12
    s1["K16"]=12/100
    s1["L16"]=12/100
    s1["M16"]=12/100
    s1["N16"]=12/100

    wb.save(os.path.join(path,'form1.xlsx'))

    return HttpResponse("Done !")