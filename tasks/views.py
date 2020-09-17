from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from .models import User_db,Pages
from django.core.paginator import Paginator

# Create your views here.


# -------------------------------------- Static pages -----------------------------------------



                                # Home page
def home(request):
    return render(request,'home.html')





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
        role = request.POST['role']
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


def auth_admin(request):
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
        total = User_db.objects.all().count()
        return render(request,'admin-dashboard.html',{'total_users':total})
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
            return render(request,'admin-profile-update.html',{'name':user.name,'mobile':user.mobile,'email':user.email,'address':user.address,'photo':user.photo.url})
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







# -------------------------------------- Admin tasks --------------------------------------------





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















def admin_profile_update_form(request):
    
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








def admin_profile_photo_update(request):

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
            







def ajax_call_delete_user(request):
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










def profile_edit_by_get(request,id):
    if(auth_admin(request)):
        user =  User_db.objects.get(id=id)
        if(user.role !="admin"):
            return render(request,'admin-update-user.html',{'id':id,'name':user.name,'mobile':user.mobile,'email':user.email,'address':user.address,'role':user.role,'photo':user.photo.url})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')










def admin_user_profile_update_form(request):
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








def admin_user_profile_photo_update(request):

    inp_user = User_db.objects.filter(id=request.POST['id']).count()
    if(auth_admin(request) and inp_user and request.method=="POST"):
        user =  User_db.objects.get(id=request.POST['id'])
        photo = request.FILES["photo"]
        user.photo = photo
        user.save()
        return redirect("/admin-all-users")
    else:
        return render(request,'login.html')















def admin_new_user_profile_form(request):
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










def admin_new_page_form(request):
    
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






def page_update_by_get(request,id):
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








def admin_page_update_form(request):

    page = Pages.objects.filter(id=request.POST['id']).get()
    if(page.slug!=request.POST["slug"]):
        c = Pages.objects.filter(slug=request.POST["slug"]).count()
        if(c):
            messages.info(request,"Slug is already exists !")
            return redirect('/admin-add-page')


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





def ajax_call_delete_page(request):
    if(auth_admin(request) and request.method=="POST"):
        page = Pages.objects.filter(id=request.POST['id']).get()
        if(page):
            page.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})



#----------------------------------------- USER's Page and Tasks---------------


def auth_user(request):
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role!="admin"):
            return True
        else:
            return False
    else:
        return False




def user_dashboard(request):

    if(auth_user(request)):
        return render(request,'user-dashboard.html')
    else:
        return render(request,'login.html')




def user_profile_update(request):

    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role!="admin"):
            user =  User_db.objects.get(id=request.session['user'])
            
            return render(request,'user-profile-update.html',{'name':user.name,'mobile':user.mobile,'email':user.email,'address':user.address,'photo':user.photo.url})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')











def user_profile_update_form(request):
    
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









def user_profile_photo_update(request):         

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