from django.shortcuts import render,redirect
from django.http import HttpResponse,request,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from tasks.models import User_db,Pages,Posts,Banners
from django.core.paginator import Paginator
from .models import Packs,Industries



#---------------------------------------------------- Pages -----------------------------------------------




def auth_admin(request):                                # Admin authentication
    if(request.session.get('user')):
        user = User_db.objects.filter(id=request.session['user']).get()
        if(user and user.role=="admin"):
            return True
        else:
            return False
    else:
        return False




def admin_all_packages(request):                        # Admin All packages page
    if(auth_admin(request)):
        packs = Packs.objects.all()
        return render(request,"bmanage/admin-all-packages.html",{"packs":packs})
    else:
        return render(request,'login.html')






def admin_add_package(request):                        # Admin Add package page
    if(auth_admin(request)):
        return render(request,"bmanage/admin-add-package.html")
    else:
        return render(request,'login.html')









def admin_all_industries(request):                        # Admin All industries page
    if(auth_admin(request)):
        ind = Industries.objects.all()
        return render(request,"bmanage/admin-all-industries.html",{"inds":ind})
    else:
        return render(request,'login.html')






def admin_add_industry(request):                        # Admin Add industry page
    if(auth_admin(request)):
        return render(request,"bmanage/admin-add-industry.html")
    else:
        return render(request,'login.html')













#--------------------------------------------------------------- Tasks ------------------------------------------------


def admin_new_package_form(request):                                   # Admin add new Package Form

    pack = Packs.objects.filter(title=request.POST["title"]).count()

    if(pack):
        messages.info(request,"Package Title id already exists !")
        return redirect('/admin-add-package')

    if(auth_admin(request) and request.method=="POST"):
        pack =  Packs()
        pack.title=request.POST["title"]
        pack.price=request.POST["price"]
        pack.validity=request.POST["validity"]
        pack.plan=request.POST["plan"]
        
        
        if(request.FILES):
            pack.photo = request.FILES["photo"]

        pack.save()

        return redirect("/admin-all-packages")
    else:
        return render(request,'login.html')






def package_update_by_get(request,id):                                   # Package by GET method by Admin
    if(auth_admin(request)):
        pack =  Packs.objects.get(id=id)
        if(pack):
            if(pack.photo):
                return render(request,'bmanage/admin-package-update.html',{'id':id,'title':pack.title,'photo':pack.photo.url,
                'validity':pack.validity,'price':pack.price,'plan':pack.plan})
            else:
                return render(request,'bmanage/admin-package-update.html',{'id':id,'title':pack.title,
                'validity':pack.validity,'price':pack.price,'plan':pack.plan})

        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')











def admin_package_update_form(request):                                   # Admin Package update Form

    pack = Packs.objects.filter(id=request.POST['id']).get()
    if(pack.title!=request.POST["title"]):
        c = Packs.objects.filter(title=request.POST["title"]).count()
        if(c):
            messages.info(request,"Package Title is already exists !")
            return redirect('/package_update_by_get/'+str(request.POST['id']))

    if(auth_admin(request) and pack and request.method=="POST"):
        pack.title=request.POST["title"]
        pack.price=request.POST["price"]
        pack.validity=request.POST["validity"]
        pack.plan=request.POST["plan"]
        if(request.FILES):
            pack.photo = request.FILES["photo"]
        pack.save()            
        return redirect("/admin-all-packages")
    else:
        return render(request,'login.html')



def ajax_call_delete_package(request):                                   # AJAX call DELETE Package - By Admin
    if(auth_admin(request) and request.method=="POST"):
        pack = Packs.objects.filter(id=request.POST['id']).get()
        if(pack):
            pack.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})











# +++++++++++++++++   * ////////////////// ---------++++++++++++++ ]]]]]]]]][[[[[[[[[[]]]]]]]]]]









def admin_new_industry_form(request):                                   # Admin add new industry Form

    ind = Industries.objects.filter(name=request.POST["name"]).count()

    if(ind):
        messages.info(request,"Industry Name id already exists !")
        return redirect('/admin-add-industry')

    if(not request.FILES["photo"]):
        messages.info(request,"Industry photo not found !")
        return redirect('/admin-add-industry')

    if(auth_admin(request) and request.method=="POST"):
        ind =  Industries()
        ind.name=request.POST["name"]
        ind.owner=request.POST["owner"]
        ind.email=request.POST["email"]
        ind.mobile=request.POST["mobile"]
        ind.address=request.POST["address"]
        ind.photo = request.FILES["photo"]
        ind.save()

        return redirect("/admin-all-industries")
    else:
        return render(request,'login.html')






def industry_update_by_get(request,id):                                   # Industry by GET method by Admin
    if(auth_admin(request)):
        ind =  Industries.objects.get(id=id)
        if(ind):
            return render(request,'bmanage/admin-industry-update.html',{'id':id,'name':ind.name,'photo':ind.photo.url,
            'owner':ind.owner,'email':ind.email,'mobile':ind.mobile,'address':ind.address})  

        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')











def admin_industry_update_form(request):                                   # Admin industry update Form

    ind = Industries.objects.filter(id=request.POST['id']).get()
    if(ind.name!=request.POST["name"]):
        c = Industries.objects.filter(name=request.POST["name"]).count()
        if(c):
            messages.info(request,"industry name is already exists !")
            return redirect('/industry_update_by_get/'+str(request.POST['id']))

    if(auth_admin(request) and ind and request.method=="POST"):
        ind.name=request.POST["name"]
        ind.owner=request.POST["owner"]
        ind.email=request.POST["email"]
        ind.mobile=request.POST["mobile"]
        ind.address=request.POST["address"]
        if(request.FILES):
            ind.photo = request.FILES["photo"]
        ind.save()            
        return redirect("/admin-all-industries")
    else:
        return render(request,'login.html')



def ajax_call_delete_industry(request):                                   # AJAX call DELETE industry - By Admin
    if(auth_admin(request) and request.method=="POST"):
        ind = Industries.objects.filter(id=request.POST['id']).get()
        if(ind):
            ind.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})