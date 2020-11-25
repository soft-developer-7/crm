from django.shortcuts import render,redirect
from django.core.serializers import serialize
from django.http import HttpResponse,request,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
import json
from datetime import date
from django.http import JsonResponse
from .models import User_db,Pages,Posts,Banners,super_plan_forms,super_plan_forms_multiple_inputs,super_plan_forms_multiple_images,super_plan_forms_multiple_files
from django.core.paginator import Paginator
from business_management.models import Packs,Industries,User_bookings,Templates




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
                
                return redirect('/user-profile-update')
                

            else:
                
                messages.info(request,"Invalid user id or password !")
                return render(request,'login.html')

        else:
            
            messages.info(request,"Invalid user id or password !")
            return render(request,'login.html')

    







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
        return render(request,'login.html')





                                # Logout
def logout(request):
    request.session.clear()
    return redirect('/login')



                                # Admin Add user page
def admin_add_user(request):
    if(auth_admin(request)):
        return render(request,'admin-add-user.html')
    else:
        return render(request,'login.html')




                                # Admin All users page
def admin_all_users(request):
    if(auth_admin(request)):
        users = User_db.objects.exclude(role="admin").all()
        return render(request,'admin-all-users.html',{'users':users})
    else:
        return render(request,'login.html')



                                # Admin profile update page
def admin_profile_update(request):
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role=="admin"):
            return render(request,'admin-profile-update.html',{'name':user.name,'mobile':user.mobile,
            'email':user.email,'address':user.address,'photo':user.photo.url})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')





                                # Admin Add PAGE page
def admin_add_page(request):
    if(auth_admin(request)):
        return render(request,'admin-add-page.html')
    else:
        return render(request,'login.html')





                                # Admin all PAGES page
def admin_all_pages(request):
    if(auth_admin(request)):
        pages = Pages.objects.all()
        return render(request,'admin-all-pages.html',{"pages":pages})
    else:
        return render(request,'login.html')       






                                # Admin Add Post page
def admin_add_post(request):
    if(auth_admin(request)):
        return render(request,'admin-add-post.html')
    else:
        return render(request,'login.html')




                                # Admin all Posts page
def admin_all_posts(request):
    if(auth_admin(request)):
        posts = Posts.objects.order_by('-pub_date')
        return render(request,'admin-all-posts.html',{"posts":posts})
    else:
        return render(request,'login.html')    







                                # Admin Add Banner page
def admin_add_banner(request):
    if(auth_admin(request)):
        return render(request,'admin-add-banner.html')
    else:
        return render(request,'login.html')




                                # Admin all Banners page
def admin_all_banners(request):
    if(auth_admin(request)):
        banners = Banners.objects.order_by('-date')
        return render(request,'admin-all-banners.html',{"banners":banners})
    else:
        return render(request,'login.html')    






# -------------------------------------- Admin tasks -----------------------------------------------------------------









                                # Admin Login Form Submit
def admin_login_form(request):

    if(request.method=="POST"):
        email = request.POST['email']
        user = User_db.objects.filter(email=email).get()
        if(user and user.role=="admin"):
            password = request.POST['password']

            if(check_password(password,user.password)):
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
            return render(request,'login.html')
    else:
        return render(request,'login.html')








def admin_profile_photo_update(request):                                # Admin Profile Photo Update Form

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role=="admin" and request.method=="POST"):
            
            photo = request.FILES["photo"]
            user.photo = photo
            user.save()
            return redirect("/admin-profile-update")
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
            







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
            return render(request,'login.html')
    else:
        return render(request,'login.html')










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
        return render(request,'login.html')








def admin_user_profile_photo_update(request):                               # Admin USER profile PHOTO update Form

    inp_user = User_db.objects.filter(id=request.POST['id']).count()
    if(auth_admin(request) and inp_user and request.method=="POST"):
        user =  User_db.objects.get(id=request.POST['id'])
        photo = request.FILES["photo"]
        user.photo = photo
        user.save()
        return redirect("/admin-all-users")
    else:
        return render(request,'login.html')















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
        return render(request,'login.html')










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
        return render(request,'login.html')






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
            return render(request,'login.html')
    else:
        return render(request,'login.html')








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
        return render(request,'login.html')





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
        return render(request,'login.html')








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
            return render(request,'login.html')
    else:
        return render(request,'login.html')






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
        return render(request,'login.html')




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
        return render(request,'login.html')






def banner_update_by_get(request,id):                                   # Banner by GET method by Admin
    if(auth_admin(request)):
        banner =  Banners.objects.get(id=id)
        if(banner):
            return render(request,'admin-banner-update.html',{'id':id,'title':banner.title,'desc':banner.desc,
            'alt':banner.alt,'category':banner.category,'photo':banner.photo.url})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')





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
        return render(request,'login.html')











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
        return render(request,'login.html')




def user_profile_update(request):                                # User Profile Update Page

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role!="admin"):
            user =  User_db.objects.get(id=request.session['user'])
            
            return render(request,'user-profile-update.html',{'name':user.name,'countrycode':user.countrycode,'mobile':user.mobile,
            'email':user.email,'address':user.address,'photo':user.photo.url})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')











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
            return render(request,'login.html')
    else:
        return render(request,'login.html')












def successful_purchased(request):                                # User Successful Purchased

    if(auth_user(request)):
        return render(request,'successful-purchased.html')
    else:
        return render(request,'login.html')


#--------------------------------------------------- User Forms -------------------------------------------


def user_form_1(request):                                # User Form 1

    if(auth_user(request)):
        if(request.session.get("form")):
            del request.session['form']
        return render(request,'user-form1.html')
    else:
        return render(request,'login.html')




def user_form_1_submit(request):            # User Form 1 Submit
    if(auth_user(request) and request.method=="POST"):

        if(not request.session.get("form")):

            book = super_plan_forms()

            book.user = User_db.objects.filter(id=request.session['user']).get()
            book.company_name = request.POST["company_name"]
            book.company_website_link = request.POST["company_website_link"]
            book.owner_name = request.POST["owner_name"]
            book.countrycode = request.POST['countrycode']
            book.phone_number = request.POST["phone_number"]
            book.email_id = request.POST["email_id"]

            if request.POST.get("gst_number") and request.POST.get("gst_name"):
                book.gst_number = request.POST["gst_number"]
                book.gst_name = request.POST["gst_name"]


            
            book.current_fillup_position = 1
            book.save()
            request.session["form"] = book.id

            return render(request,'user-form2.html')
        else:
            return render(request,'user-form1.html')
    else:
        return render(request,'login.html')









def user_form_2_submit(request):            # User Form 2 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        book.about_the_company = request.POST["about_the_company"]
        book.company_founded = request.POST["company_founded"]
        book.industry_type = request.POST["industry_type"]

        if(request.FILES.get("company_logo")):
            book.company_logo = request.FILES["company_logo"]

        if(book.current_fillup_position<12):
            book.current_fillup_position = 2
        book.save()

        return render(request,'user-form3.html')
    else:
        return render(request,'login.html')








def user_form_3_submit(request):            # User Form 3 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):


        c=0
        multi = super_plan_forms_multiple_inputs()
        multi.user = User_db.objects.filter(id=request.session['user']).get()
        multi.form_id=request.session['form']
        
        for i in range(1,6):
            if(request.POST.get("challenges_faced_"+str(i))):
                c+=1
                if(c==1):
                     multi.f_1 = request.POST["challenges_faced_"+str(i)]
                elif(c==2):
                     multi.f_2 = request.POST["challenges_faced_"+str(i)]
                elif(c==3):
                     multi.f_3 = request.POST["challenges_faced_"+str(i)]
                elif(c==4):
                     multi.f_4 = request.POST["challenges_faced_"+str(i)]
                elif(c==5):
                     multi.f_5 = request.POST["challenges_faced_"+str(i)]
        multi.save()
        book.challenges_faced = multi


        c=0
        multi = super_plan_forms_multiple_inputs()
        multi.user = User_db.objects.filter(id=request.session['user']).get()
        multi.form_id=request.session['form']
        
        for i in range(1,6):
            if(request.POST.get("solutions_provided_"+str(i))):
                c+=1
                if(c==1):
                     multi.f_1 = request.POST["solutions_provided_"+str(i)]
                elif(c==2):
                     multi.f_2 = request.POST["solutions_provided_"+str(i)]
                elif(c==3):
                     multi.f_3 = request.POST["solutions_provided_"+str(i)]
                elif(c==4):
                     multi.f_4 = request.POST["solutions_provided_"+str(i)]
                elif(c==5):
                     multi.f_5 = request.POST["solutions_provided_"+str(i)]
        multi.save()
        book.solutions_provided = multi


        if(book.current_fillup_position<12):
            book.current_fillup_position = 3
        book.save()

        return render(request,'user-form4.html')
    else:
        return render(request,'login.html')







def user_form_4_submit(request):            # User Form 4 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):



        multi = super_plan_forms_multiple_inputs()
        multi.user = User_db.objects.filter(id=request.session['user']).get()
        multi.form_id=request.session['form']

        if(request.POST.get("products_and_services_1")):
            multi.f_1 = request.POST["products_and_services_1"]

        if(request.POST.get("products_and_services_2")):
            multi.f_2 = request.POST["products_and_services_2"]

        multi.save()
        book.products_and_services = multi



        multi = super_plan_forms_multiple_images()
        multi.user = User_db.objects.filter(id=request.session['user']).get()
        multi.form_id=request.session['form']

        if(request.FILES.get("products_and_services_file_1")):
            multi.i_1 = request.FILES["products_and_services_file_1"]

        if(request.FILES.get("products_and_services_file_2")):
            multi.i_2 = request.FILES["products_and_services_file_2"]

        multi.save()
        book.products_and_services_file = multi




        if(request.POST.get("top_clients")):
            book.top_clients = request.POST["top_clients"]
        if(request.FILES.get("top_clients_file")):
            book.top_clients_file = request.FILES["top_clients_file"]

        if(request.POST.get("milestones")):
            book.milestones = request.POST["milestones"]

        if(request.POST.get("locations_served")):
            book.locations_served = request.POST["locations_served"]
        
        if(request.POST.get("swot_s")):
            book.swot_s = request.POST["swot_s"]

        if(request.POST.get("swot_w")):
            book.swot_w = request.POST["swot_w"]

        if(request.POST.get("swot_o")):
            book.swot_o = request.POST["swot_o"]

        if(request.POST.get("swot_t")):
            book.swot_t = request.POST["swot_t"]

        if(book.current_fillup_position<12):
            book.current_fillup_position = 4
        book.save()
        return render(request,'user-form5.html')
    else:
        return render(request,'login.html')







def user_form_5_submit(request):            # User Form 5 Submit
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
        

        if(book.current_fillup_position<12):
            book.current_fillup_position = 5
        book.save()
        return render(request,'user-form6.html')
    else:
        return render(request,'login.html')









def user_form_6_submit(request):            # User Form 6 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        if(request.POST.get("marketing_strategies")):
            book.marketing_strategies = request.POST["marketing_strategies"]

        if(request.POST.get("growth_strategy")):
            book.growth_strategy = request.POST["growth_strategy"]

        if(book.current_fillup_position<12):
            book.current_fillup_position = 6
        book.save()
        return render(request,'user-form7.html')
    else:
        return render(request,'login.html')









def user_form_7_submit(request):            # User Form 7 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        if(request.POST.get("industry_analysis")):
            book.industry_analysis = request.POST["industry_analysis"]

        if(request.POST.get("competitor_analysis")):
            book.competitor_analysis = request.POST["competitor_analysis"]

        if(request.POST.get("usp")):
            book.usp = request.POST["usp"]

        if(book.current_fillup_position<12):
            book.current_fillup_position = 7
        book.save()
        return render(request,'user-form8.html')
    else:
        return render(request,'login.html')












def user_form_8_submit(request):            # User Form 8 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):


        if(request.POST.get("revenue_growth_or_amount")):
            book.revenue_growth_or_amount = request.POST["revenue_growth_or_amount"]
        if(request.FILES.get("revenue_growth_or_amount_file")):
            book.revenue_growth_or_amount_file = request.FILES["revenue_growth_or_amount_file"]


        if(request.POST.get("other_income_growth_or_amount")):
            book.other_income_growth_or_amount = request.POST["other_income_growth_or_amount"]
        if(request.FILES.get("other_income_growth_or_amount_file")):
            book.other_income_growth_or_amount_file = request.FILES["other_income_growth_or_amount_file"]


        if(request.POST.get("total_revenue_amount")):
            book.total_revenue_amount = request.POST["total_revenue_amount"]
        if(request.FILES.get("total_revenue_amount_file")):
            book.total_revenue_amount_file = request.FILES["total_revenue_amount_file"]


        if(request.POST.get("operating_expenses_growth_or_amount")):
            book.operating_expenses_growth_or_amount = request.POST["operating_expenses_growth_or_amount"]
        if(request.FILES.get("operating_expenses_growth_or_amount_file")):
            book.operating_expenses_growth_or_amount_file = request.FILES["operating_expenses_growth_or_amount_file"]

        
        if(request.POST.get("employee_cost")):
            book.employee_cost = request.POST["employee_cost"]
        if(request.FILES.get("employee_cost_file")):
            book.employee_cost_file = request.FILES["employee_cost_file"]


        if(request.POST.get("general_and_administration_cost")):
            book.general_and_administration_cost = request.POST["general_and_administration_cost"]
        if(request.FILES.get("general_and_administration_cost_file")):
            book.general_and_administration_cost_file = request.FILES["general_and_administration_cost_file"]


        if(request.POST.get("selling_and_marketing_cost")):
            book.selling_and_marketing_cost = request.POST["selling_and_marketing_cost"]
        if(request.FILES.get("selling_and_marketing_cost_file")):
            book.selling_and_marketing_cost_file = request.FILES["selling_and_marketing_cost_file"]


        if(request.POST.get("other_expenses_growth_or_amount")):
            book.other_expenses_growth_or_amount = request.POST["other_expenses_growth_or_amount"]
        if(request.FILES.get("other_expenses_growth_or_amount_file")):
            book.other_expenses_growth_or_amount_file = request.FILES["other_expenses_growth_or_amount_file"]


        if(request.POST.get("ebitda")):
            book.ebitda = request.POST["ebitda"]
        if(request.FILES.get("ebitda_file")):
            book.ebitda_file = request.FILES["ebitda_file"]


        if(request.POST.get("depreciation_or_amount")):
            book.depreciation_or_amount = request.POST["depreciation_or_amount"]
        if(request.FILES.get("depreciation_or_amount_file")):
            book.depreciation_or_amount_file = request.FILES["depreciation_or_amount_file"]


        if(request.POST.get("interest_expense_interest_or_amount")):
            book.interest_expense_interest_or_amount = request.POST["interest_expense_interest_or_amount"]
        if(request.FILES.get("interest_expense_interest_or_amount_file")):
            book.interest_expense_interest_or_amount_file = request.FILES["interest_expense_interest_or_amount_file"]


        if(request.POST.get("ebt")):
            book.ebt = request.POST["ebt"]
        if(request.FILES.get("ebt_file")):
            book.ebt_file = request.FILES["ebt_file"]


        if(request.POST.get("tax_expense_tax_or_amount")):
            book.tax_expense_tax_or_amount = request.POST["tax_expense_tax_or_amount"]
        if(request.FILES.get("tax_expense_tax_or_amount_file")):
            book.tax_expense_tax_or_amount_file = request.FILES["tax_expense_tax_or_amount_file"]


        if(request.POST.get("pat")):
            book.pat = request.POST["pat"]
        if(request.FILES.get("pat_file")):
            book.pat_file = request.FILES["pat_file"]


        if(book.current_fillup_position<12):
            book.current_fillup_position = 8
        book.save()
        return render(request,'user-form9.html')
    else:
        return render(request,'login.html')










def user_form_9_submit(request):            # User Form 9 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        if(request.POST.get("share_capital")):
            book.share_capital = request.POST["share_capital"]
        if(request.FILES.get("share_capital_file")):
            book.share_capital_file = request.FILES["share_capital_file"]


        if(request.POST.get("reserves_and_surplus")):
            book.reserves_and_surplus = request.POST["reserves_and_surplus"]
        if(request.FILES.get("reserves_and_surplus_file")):
            book.reserves_and_surplus_file = request.FILES["reserves_and_surplus_file"]

        
        if(request.POST.get("fund_requirement")):
            book.fund_requirement = request.POST["fund_requirement"]
        if(request.FILES.get("fund_requirement_file")):
            book.fund_requirement_file = request.FILES["fund_requirement_file"]


        if(request.POST.get("total_shareholder_funds")):
            book.total_shareholder_funds = request.POST["total_shareholder_funds"]
        if(request.FILES.get("total_shareholder_funds_file")):
            book.total_shareholder_funds_file = request.FILES["total_shareholder_funds_file"]


        if(request.POST.get("secured_loans")):
            book.secured_loans = request.POST["secured_loans"]
        if(request.FILES.get("secured_loans_file")):
            book.secured_loans_file = request.FILES["secured_loans_file"]

        
        if(request.POST.get("unsecured_loans")):
            book.unsecured_loans = request.POST["unsecured_loans"]
        if(request.FILES.get("unsecured_loans_file")):
            book.unsecured_loans_file = request.FILES["unsecured_loans_file"]


        if(request.POST.get("long_term_provisions_growth_or_amount")):
            book.long_term_provisions_growth_or_amount = request.POST["long_term_provisions_growth_or_amount"]
        if(request.FILES.get("long_term_provisions_growth_or_amount_file")):
            book.long_term_provisions_growth_or_amount_file = request.FILES["long_term_provisions_growth_or_amount_file"]


        if(request.POST.get("other_non_current_liabilities_growth_or_amount")):
            book.other_non_current_liabilities_growth_or_amount = request.POST["other_non_current_liabilities_growth_or_amount"]
        if(request.FILES.get("other_non_current_liabilities_growth_or_amount_file")):
            book.other_non_current_liabilities_growth_or_amount_file = request.FILES["other_non_current_liabilities_growth_or_amount_file"]

        
        if(request.POST.get("total_non_current_liabilities")):
            booktotal_non_current_liabilities = request.POST["total_non_current_liabilities"]
        if(request.FILES.get("total_non_current_liabilities_file")):
            book.total_non_current_liabilities_file = request.FILES["total_non_current_liabilities_file"]

        
        if(request.POST.get("short_term_borrowings_growth_or_amount")):
            book.short_term_borrowings_growth_or_amount = request.POST["short_term_borrowings_growth_or_amount"]
        if(request.FILES.get("short_term_borrowings_growth_or_amount_file")):
            book.short_term_borrowings_growth_or_amount_file = request.FILES["short_term_borrowings_growth_or_amount_file"]


        if(request.POST.get("short_term_provisions_growth_or_amount")):
            book.short_term_provisions_growth_or_amount = request.POST["short_term_provisions_growth_or_amount"]
        if(request.FILES.get("short_term_provisions_growth_or_amount_file")):
            book.short_term_provisions_growth_or_amount_file = request.FILES["short_term_provisions_growth_or_amount_file"]

        
        if(request.POST.get("sundry_creditors_no_of_days_or_amount")):
            book.sundry_creditors_no_of_days_or_amount = request.POST["sundry_creditors_no_of_days_or_amount"]
        if(request.FILES.get("sundry_creditors_no_of_days_or_amount_file")):
            book.sundry_creditors_no_of_days_or_amount_file = request.FILES["sundry_creditors_no_of_days_or_amount_file"]


        if(request.POST.get("other_current_liabilities_growth_or_amount")):
            book.other_current_liabilities_growth_or_amount = request.POST["other_current_liabilities_growth_or_amount"]
        if(request.FILES.get("other_current_liabilities_growth_or_amount_file")):
            book.other_current_liabilities_growth_or_amount_file = request.FILES["other_current_liabilities_growth_or_amount_file"]


        if(request.POST.get("total_current_liabilities")):
            book.total_current_liabilities = request.POST["total_current_liabilities"]
        if(request.FILES.get("total_current_liabilities_file")):
            book.total_current_liabilities_file = request.FILES["total_current_liabilities_file"]

        
        if(request.POST.get("total_liabilities")):
            book.total_liabilities = request.POST["total_liabilities"]
        if(request.FILES.get("total_liabilities_file")):
            book.total_liabilities_file = request.FILES["total_liabilities_file"]


        if(request.POST.get("gross_fixed_assets_growth_or_amount")):
            book.gross_fixed_assets_growth_or_amount = request.POST["gross_fixed_assets_growth_or_amount"]
        if(request.FILES.get("gross_fixed_assets_growth_or_amount_file")):
            book.gross_fixed_assets_growth_or_amount_file = request.FILES["gross_fixed_assets_growth_or_amount_file"]


        if(request.POST.get("less_accumulated_depreciation_or_amount")):
            book.less_accumulated_depreciation_or_amount = request.POST["less_accumulated_depreciation_or_amount"]
        if(request.FILES.get("_file")):
            book.less_accumulated_depreciation_or_amount_file = request.FILES["less_accumulated_depreciation_or_amount_file"]

        
        if(request.POST.get("net_fixed_assets_growth_or_amount")):
            book.net_fixed_assets_growth_or_amount = request.POST["net_fixed_assets_growth_or_amount"]
        if(request.FILES.get("net_fixed_assets_growth_or_amount_file")):
            book.net_fixed_assets_growth_or_amount_file = request.FILES["net_fixed_assets_growth_or_amount_file"]


        if(request.POST.get("intangible_assets_growth_or_amount")):
            book.intangible_assets_growth_or_amount = request.POST["intangible_assets_growth_or_amount"]
        if(request.FILES.get("intangible_assets_growth_or_amount_file")):
            book.intangible_assets_growth_or_amount_file = request.FILES["intangible_assets_growth_or_amount_file"]


        if(request.POST.get("long_term_loans_and_advances_growth_or_amount")):
            book.long_term_loans_and_advances_growth_or_amount = request.POST["long_term_loans_and_advances_growth_or_amount"]
        if(request.FILES.get("long_term_loans_and_advances_growth_or_amount_file")):
            book.long_term_loans_and_advances_growth_or_amount_file = request.FILES["long_term_loans_and_advances_growth_or_amount_file"]

        
        if(request.POST.get("long_term_investments_growth_or_amount")):
            book.long_term_investments_growth_or_amount = request.POST["long_term_investments_growth_or_amount"]
        if(request.FILES.get("long_term_investments_growth_or_amount_file")):
            book.long_term_investments_growth_or_amount_file = request.FILES["long_term_investments_growth_or_amount_file"]

        
        if(request.POST.get("other_non_current_assets_growth_or_amount")):
            book.other_non_current_assets_growth_or_amount = request.POST["other_non_current_assets_growth_or_amount"]
        if(request.FILES.get("other_non_current_assets_growth_or_amount_file")):
            book.other_non_current_assets_growth_or_amount_file = request.FILES["other_non_current_assets_growth_or_amount_file"]


        if(request.POST.get("total_non_current_assets")):
            book.total_non_current_assets = request.POST["total_non_current_assets"]
        if(request.FILES.get("_file")):
            book.total_non_current_assets_file = request.FILES["total_non_current_assets_file"]

        
        if(request.POST.get("cash")):
            book.cash = request.POST["cash"]
        if(request.FILES.get("cash_file")):
            book.cash_file = request.FILES["cash_file"]


        if(request.POST.get("sundry_debtors_no_of_days_or_amount")):
            book.sundry_debtors_no_of_days_or_amount = request.POST["sundry_debtors_no_of_days_or_amount"]
        if(request.FILES.get("sundry_debtors_no_of_days_or_amount_file")):
            book.sundry_debtors_no_of_days_or_amount_file = request.FILES["sundry_debtors_no_of_days_or_amount_file"]

        
        if(request.POST.get("inventory_no_of_days_or_amount")):
            book.inventory_no_of_days_or_amount = request.POST["inventory_no_of_days_or_amount"]
        if(request.FILES.get("inventory_no_of_days_or_amount_file")):
            book.inventory_no_of_days_or_amount_file = request.FILES["inventory_no_of_days_or_amount_file"]


        if(request.POST.get("short_term_investments_growth_or_amount")):
            book.short_term_investments_growth_or_amount = request.POST["short_term_investments_growth_or_amount"]
        if(request.FILES.get("short_term_investments_growth_or_amount_file")):
            book.short_term_investments_growth_or_amount_file = request.FILES["short_term_investments_growth_or_amount_file"]

        
        if(request.POST.get("short_term_loans_and_advances_growth_or_amount")):
            book.short_term_loans_and_advances_growth_or_amount = request.POST["short_term_loans_and_advances_growth_or_amount"]
        if(request.FILES.get("short_term_loans_and_advances_growth_or_amount_file")):
            book.short_term_loans_and_advances_growth_or_amount_file = request.FILES["short_term_loans_and_advances_growth_or_amount_file"]

        
        if(request.POST.get("other_current_assets_growth_or_amount")):
            book.other_current_assets_growth_or_amount = request.POST["other_current_assets_growth_or_amount"]
        if(request.FILES.get("other_current_assets_growth_or_amount_file")):
            book.other_current_assets_growth_or_amount_file = request.FILES["other_current_assets_growth_or_amount_file"]


        if(request.POST.get("total_current_assets")):
            book.total_current_assets = request.POST["total_current_assets"]
        if(request.FILES.get("total_current_assets_file")):
            book.total_current_assets_file = request.FILES["total_current_assets_file"]


        if(request.POST.get("total_assets")):
            book.total_assets = request.POST["total_assets"]
        if(request.FILES.get("total_assets_file")):
            book.total_assets_file = request.FILES["total_assets_file"]


        if(book.current_fillup_position<12):
            book.current_fillup_position = 9
        book.save()
        return render(request,'user-form10.html')
    else:
        return render(request,'login.html')



















def user_form_10_submit(request):            # User Form 10 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        if(request.POST.get("company_owned_land_and_building")):
            book.company_owned_land_and_building = request.POST["company_owned_land_and_building"]
        if(request.FILES.get("company_owned_land_and_building_file")):
            book.company_owned_land_and_building_file = request.FILES["company_owned_land_and_building_file"]


        if(request.POST.get("other_fixed_assets")):
            book.other_fixed_assets = request.POST["other_fixed_assets"]
        if(request.FILES.get("other_fixed_assets_file")):
            book.other_fixed_assets_file = request.FILES["other_fixed_assets_file"]


        if(request.POST.get("depreciation_growth_or_amount")):
            book.depreciation_growth_or_amount = request.POST["depreciation_growth_or_amount"]
        if(request.FILES.get("depreciation_growth_or_amount_file")):
            book.depreciation_growth_or_amount_file = request.FILES["depreciation_growth_or_amount_file"]


        if(request.POST.get("total_capex_expense")):
            book.total_capex_expense = request.POST["total_capex_expense"]

        if(book.current_fillup_position<12):
            book.current_fillup_position = 10
        book.save()
        return render(request,'user-form11.html')
    else:
        return render(request,'login.html')








def user_form_11_submit(request):            # User Form 11 Submit
    book = super_plan_forms.objects.filter(id=request.session['form']).get()
    if(auth_user(request) and book and request.method=="POST"):

        if(request.POST.get("theme")):
            book.theme = request.POST["theme"]

        if(request.POST.get("currency")):
            book.currency = request.POST["currency"]

        if(request.POST.get("denomination")):
            book.denomination = request.POST["denomination"]

        if(request.POST.get("pack")):
            book.pack = request.POST["pack"]

        book.current_fillup_position = 12
        book.save()
        return redirect("/successful-purchased")
    else:
        return render(request,'login.html')






def user_all_superplan_bookings(request):                                # User All Template view

    if(auth_user(request)):
        data = super_plan_forms.objects.filter(user=request.session['user'],current_fillup_position=12) 
        return render(request,'user-all-superplan-bookings.html',{"bookings":data})
    else:
        return render(request,'login.html')







def user_template_view_by_get(request,id):                                # User Template view by GET

    if(auth_user(request)):
        data = super_plan_forms.objects.filter(id=id).get()
        tdate = date.today()
        logo=""
        if(data.company_logo):
            logo=data.company_logo.url
        return render(request,'template/template1.html',{"data":data,"logo":logo,"year":tdate.year})
    else:
        return render(request,'login.html')







def user_all_incomplete_superplan_bookings(request):                                # User All incomplete superplan form

    if(auth_user(request)):
        data = super_plan_forms.objects.filter(user=request.session['user'],current_fillup_position__lt=12)
        return render(request,'user-all-incomplete-superplan-bookings.html',{"bookings":data})
    else:
        return render(request,'login.html')








def user_incomplete_superplan_by_get(request,id):                                # User incomplete superplan form by GET

    if(auth_user(request)):
        book=super_plan_forms.objects.filter(id=id,user=request.session['user']).get()
        if(book):
            request.session["form"] = book.id
            form_url = 'user-form'+str((book.current_fillup_position)+1)+'.html'
            return render(request,form_url)
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')




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
        return render(request,'login.html')





def test(request):
    data=super_plan_forms_multiple_inputs.objects.all()
    return render(request,'print_data.html',{'datas':data})