from django.shortcuts import render,redirect
from django.http import HttpResponse,request,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from .models import User_db,Pages,Posts,Banners
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
        role =request.POST['role']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['confrim_password']

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
            
            return render(request,'user-profile-update.html',{'name':user.name,'mobile':user.mobile,
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
            user.save()
            return redirect("/user-dashboard")
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')









def user_profile_photo_update(request):                                         # User Profile PHOTO Update Form

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()

        if(user and user.role!="admin" and request.method=="POST"):
            photo = request.FILES["photo"]
            user.photo = photo
            user.save()
            return redirect("/user-dashboard")
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')