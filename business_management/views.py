from django.shortcuts import render,redirect
from django.http import HttpResponse,request,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from tasks.models import User_db,Pages,Posts,Banners,super_plan_forms,super_plan_forms_multiple_inputs
from django.core.paginator import Paginator
from .models import Packs,Industries,Industry_analysis,Industry_growth_drivers,Templates,User_bookings
from django.core.paginator import Paginator
#------------------------------------------------- Custom functions --------------------------------------

def multi_input_insert(request,name):
    user = User_db.objects.filter(id=request.session['user']).get()
    form_id = "admin"
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





def admin_all_industries(request):                        # Admin All industries page
    if(auth_admin(request)):
        ind = Industries.objects.all()
        ind_an = Industry_analysis.objects.all().values_list("industry__id", flat=True)
        ind_gw = Industry_growth_drivers.objects.all().values_list("industry__id", flat=True)
        paginator = Paginator(ind, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,"bmanage/admin-all-industries.html",{"inds":page_obj,"inds_an":ind_an,"inds_gw":ind_gw})
    else:
        return redirect('/login')






def admin_add_industry(request):                        # Admin Add industry page
    if(auth_admin(request)):
        return render(request,"bmanage/admin-add-industry.html")
    else:
        return redirect('/login')









def admin_add_industry_analysis(request):                        # Admin Add industry Analysis page
    if(auth_admin(request)):
        ind = Industries.objects.all()
        return render(request,"bmanage/admin-add-industry-analysis.html",{"data":ind})
    else:
        return redirect('/login')





def industry_analysis_view_by_get(request,id):                                   # Industry Analysisby view GET method by Admin
    if(auth_admin(request)):
        ind =  Industry_analysis.objects.filter(industry__id=id).count()
        if(ind):
            ind =  Industry_analysis.objects.filter(industry__id=id).get()
            
            return render(request,'bmanage/admin-view-industry-analysis.html',{"data":ind})  

        else:
            return render(request,'bmanage/admin-view-industry-analysis.html',{"message":"Value not set yet !"})
    else:
        return redirect('/login')




def industry_analysis_update_by_get(request,id):                                   # Update Industry Analysisby GET method by Admin
    if(auth_admin(request)):
        ind =  Industry_analysis.objects.filter(industry__id=id).get()
        if(ind):
            
            return render(request,'bmanage/admin-update-industry-analysis.html',{"data":ind})  

        else:
            return render(request,'bmanage/admin-update-industry-analysis.html',{"message":"Value not set yet !"})
    else:
        return redirect('/login')









def admin_add_industry_growth_drivers(request):                        # Admin Add industry growth drivers page
    if(auth_admin(request)):
        ind = Industries.objects.all()
        return render(request,"bmanage/admin-add-industry-growth-drivers.html",{"data":ind})
    else:
        return redirect('/login')








def industry_growth_drivers_view_by_get(request,id):                                   # Industry growth drivers view GET method by Admin
    if(auth_admin(request)):
        ind =  Industry_growth_drivers.objects.filter(industry__id=id).count()
        if(ind):
            ind =  Industry_growth_drivers.objects.filter(industry__id=id).get()
            
            return render(request,'bmanage/admin-view-industry-growth-drivers.html',{"data":ind})  

        else:
            return render(request,'bmanage/admin-view-industry-growth-drivers.html',{"message":"Value not set yet !"})
    else:
        return redirect('/login')




def industry_growth_drivers_update_by_get(request,id):                                   # Update Industry growth drivers GET method by Admin
    if(auth_admin(request)):
        ind =  Industry_growth_drivers.objects.filter(industry__id=id).get()
        if(ind):
            
            return render(request,'bmanage/admin-update-industry-growth-drivers.html',{"data":ind})  

        else:
            return render(request,'bmanage/admin-update-industry-growth-drivers.html',{"message":"Value not set yet !"})
    else:
        return redirect('/login')




















def admin_all_packages(request):                        # Admin All packages page
    if(auth_admin(request)):
        packs = Packs.objects.all()
        return render(request,"bmanage/admin-all-packages.html",{"packs":packs})
    else:
        return redirect('/login')






def admin_add_package(request):                        # Admin Add package page
    if(auth_admin(request)):
        return render(request,"bmanage/admin-add-package.html")
    else:
        return redirect('/login')






def admin_all_templates(request):                        # Admin All Templates page
    if(auth_admin(request)):
        tmp = Templates.objects.all()
        return render(request,"bmanage/admin-all-templates.html",{"templates":tmp})
    else:
        return redirect('/login')





def admin_add_template(request):                        # Admin Add Template page
    if(auth_admin(request)):
        packs = Packs.objects.all()
        inds = Industries.objects.all()
        return render(request,"bmanage/admin-add-template.html",{"packs":packs,"inds":inds})
    else:
        return redirect('/login')








def admin_all_bookings(request):                        # Admin All Bookings page
    if(auth_admin(request)):
        bookings = User_bookings.objects.all()
        return render(request,"bmanage/admin-all-bookings.html",{"bookings":bookings})
    else:
        return redirect('/login')




def admin_add_booking(request):                        # Admin Add booking page
    if(auth_admin(request)):
        tmps = Templates.objects.all()
        return render(request,"bmanage/admin-add-booking.html",{"tmps":tmps})
    else:
        return redirect('/login')


def admin_all_superplan_bookings(request):                        # Admin All Bookings page
    if(auth_admin(request)):
        bookings = super_plan_forms.objects.all()
        return render(request,"bmanage/admin-all-superplan-bookings.html",{"bookings":bookings})
    else:
        return redirect('/login')









        
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
        return redirect('/login')






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
            return redirect('/login')
    else:
        return redirect('/login')











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
        return redirect('/login')



def ajax_call_delete_package(request):                                   # AJAX call DELETE Package - By Admin
    if(auth_admin(request) and request.method=="POST"):
        pack = Packs.objects.filter(id=request.POST['id']).count()
        if(pack):
            pack = Packs.objects.filter(id=request.POST['id']).get()
            pack.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})




















def admin_new_industry_form(request):                                   # Admin add new industry Form

    ind = Industries.objects.filter(name=request.POST["name"]).count()

    if(ind):
        messages.info(request,"Industry Name id already exists !")
        return redirect('/admin-add-industry')

    if(auth_admin(request) and request.method=="POST"):
        ind =  Industries()
        ind.name=request.POST["name"]
        ind.save()

        return redirect("/admin-all-industries")
    else:
        return redirect('/login')






def industry_update_by_get(request,id):                                   # Industry by GET method by Admin
    if(auth_admin(request)):
        ind =  Industries.objects.get(id=id)
        if(ind):
            return render(request,'bmanage/admin-industry-update.html',{'id':id,'name':ind.name})  

        else:
            return redirect('/login')
    else:
        return redirect('/login')











def admin_industry_update_form(request):                                   # Admin industry update Form

    ind = Industries.objects.filter(id=request.POST['id']).get()
    if(ind.name!=request.POST["name"]):
        c = Industries.objects.filter(name=request.POST["name"]).count()
        if(c):
            messages.info(request,"industry name is already exists !")
            return redirect('/industry_update_by_get/'+str(request.POST['id']))

    if(auth_admin(request) and ind and request.method=="POST"):
        ind.name=request.POST["name"]
        ind.save()            
        return redirect("/admin-all-industries")
    else:
        return redirect('/login')



def ajax_call_delete_industry(request):                                   # AJAX call DELETE industry - By Admin
    if(auth_admin(request) and request.method=="POST"):
        ind = Industries.objects.filter(id=request.POST['id']).count()
        if(ind):
            ind = Industries.objects.filter(id=request.POST['id']).get()
            ind.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})








def admin_new_industry_analysis_form(request):                                   # Admin add new industry analysis Form

    ind = Industry_analysis.objects.filter(industry__pk=request.POST["industry"]).count()

    if(ind):
        messages.info(request,"This Industry already has a Analysis !")
        return redirect('/admin-add-industry-analysis')

    if(auth_admin(request) and request.method=="POST"):
        ind_an = Industry_analysis()

        ind_an.industry = Industries.objects.get(pk=request.POST["industry"])

        if(request.POST.get("india")):
            ind_an.india = request.POST["india"]
        if(request.FILES.get("india_img")):
            ind_an.india_img =  request.FILES["india_img"]

        if(request.POST.get("glob")):
            ind_an.glob = request.POST["glob"]
        if(request.FILES.get("glob_img")):
            ind_an.glob_img =  request.FILES["glob_img"]
        ind_an.save()

        return redirect("/admin-all-industries")
    else:
        return redirect('/login')






def admin_update_industry_analysis_form(request):                                   # Admin industry analysis update Form

    ind_an = Industry_analysis.objects.filter(id=request.POST['id']).get()
    if(auth_admin(request) and ind_an and request.method=="POST"):
        if(request.POST.get("india")):
            ind_an.india = request.POST["india"]
        if(request.FILES.get("india_img")):
            ind_an.india_img =  request.FILES["india_img"]

        if(request.POST.get("glob")):
            ind_an.glob = request.POST["glob"]
        if(request.FILES.get("glob_img")):
            ind_an.glob_img =  request.FILES["glob_img"]
        ind_an.save()            
        return redirect("/admin-all-industries")
    else:
        return redirect('/login')








def ajax_call_delete_industry_analysis(request):                                   # AJAX call DELETE industry analysis - By Admin
    if(auth_admin(request) and request.method=="POST"):
        ind = Industry_analysis.objects.filter(industry__pk=request.POST['id']).count()
        if(ind):
            ind = Industry_analysis.objects.filter(industry__pk=request.POST['id'])
            ind.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})







def admin_new_industry_growth_drivers_form(request):

    ind = Industry_growth_drivers.objects.filter(industry__pk=request.POST["industry"]).count()

    if(ind):
        messages.info(request,"This Industry already has growth drivers !")
        return redirect('/admin-add-industry-growth-drivers')

    if(auth_admin(request) and request.method=="POST"):
        
        ind_gw = Industry_growth_drivers()
        ind_gw.industry = Industries.objects.get(pk=request.POST["industry"])
        ind_gw.drivers_t=multi_input_insert(request,"drivers_t[]")
        ind_gw.drivers_c=multi_input_insert(request,"drivers_c[]")
        ind_gw.save()

        return redirect("/admin-all-industries")
    else:
        return redirect('/login')












def admin_update_industry_growth_drivers_form(request):

    ind_gw = Industry_growth_drivers.objects.filter(id=request.POST['id']).get()
    if(auth_admin(request) and ind_gw and request.method=="POST"):
        ind_gw.drivers_t=multi_input_insert(request,"drivers_t[]")
        ind_gw.drivers_c=multi_input_insert(request,"drivers_c[]")
        ind_gw.save()            
        return redirect("/admin-all-industries")
    else:
        return redirect('/login')







def ajax_call_delete_industry_growth_drivers(request):                                   # AJAX call DELETE industry growth drivers - By Admin
    if(auth_admin(request) and request.method=="POST"):
        ind = Industry_growth_drivers.objects.filter(industry__pk=request.POST['id']).count()
        if(ind):
            ind = Industry_growth_drivers.objects.filter(industry__pk=request.POST['id'])
            ind.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})





















def admin_new_template_form(request):                                   # Admin add new template Form

    if(Templates.objects.filter(code=request.POST["code"]).count()):
        messages.add_message(request, messages.INFO,"Template Code already exists !")

    if(Templates.objects.filter(name=request.POST["name"]).count()):
        messages.add_message(request, messages.INFO,"Template Name already exists !")
    
    if(Templates.objects.filter(pack=request.POST["pack"],ind=request.POST["ind"]).count()):
        messages.add_message(request, messages.INFO,"Template Package and Industry combination already exists !")
    
    if(messages.get_messages(request)):
        return redirect('/admin-add-template')


    if(auth_admin(request) and request.method=="POST"):
       
        tmp =  Templates()
        tmp.name=request.POST["name"]
        tmp.ind= Industries.objects.get(id=request.POST["ind"])
        tmp.pack= Packs.objects.get(id=request.POST["pack"])
        tmp.code=request.POST["code"]
        tmp.save()

       

        return redirect("/admin-all-templates")
    else:
        return redirect('/login')






def template_view_by_get(request,id):                                   # Template view by GET method by Admin
    if(auth_admin(request)):
        tmp =  Templates.objects.get(id=id)
        if(tmp):
            return render(request,'bmanage/admin-template-view.html',{'tmp':tmp})  

        else:
            return redirect('/login')
    else:
        return redirect('/login')








def template_update_by_get(request,id):                                   # Template Update by GET method by Admin
    if(auth_admin(request)):
        tmp =  Templates.objects.get(id=id)
        packs = Packs.objects.all()
        inds = Industries.objects.all()

        if(tmp):
            return render(request,'bmanage/admin-template-update.html',{'data':tmp,'packs':packs,'inds':inds})  

        else:
            return redirect('/login')
    else:
        return redirect('/login')









def admin_template_update_form(request):                                   # Admin template update Form

    id = request.POST["id"]

    if(not Templates.objects.filter(id=id,code=request.POST["code"]).count()  and Templates.objects.filter(code=request.POST["code"]).count()):
        messages.add_message(request, messages.INFO,"Template Code already exists !")

    if(not Templates.objects.filter(id=id,name=request.POST["name"]).count() and Templates.objects.filter(name=request.POST["name"]).count()):
        messages.add_message(request, messages.INFO,"Template Name already exists !")
    
    if(not Templates.objects.filter(id=id,pack=request.POST["pack"],ind=request.POST["ind"]).count() and Templates.objects.filter(pack=request.POST["pack"],ind=request.POST["ind"]).count()):
        messages.add_message(request, messages.INFO,"Template Package and Industry combination already exists !")
    
    if(messages.get_messages(request)):
        return redirect('/template_update_by_get/'+str(id))


    if(auth_admin(request) and request.method=="POST"):
       
        tmp =  Templates.objects.filter(id=id).get()
        tmp.name=request.POST["name"]
        tmp.ind= Industries.objects.get(id=request.POST["ind"])
        tmp.pack= Packs.objects.get(id=request.POST["pack"])
        tmp.code=request.POST["code"]
        tmp.save()

        

        return redirect("/admin-all-templates")
    else:
        return redirect('/login')









def ajax_call_delete_template(request):                                   # AJAX call DELETE template - By Admin
    if(auth_admin(request) and request.method=="POST"):
        tmp = Templates.objects.filter(id=request.POST['id']).count()
        if(tmp):
            tmp = Templates.objects.filter(id=request.POST['id']).get()
            tmp.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})








def ajax_call_fetch_template(request):                                   # AJAX call Fetch template - By Admin
    if(auth_admin(request) and request.method=="POST"):
        tmp = Templates.objects.filter(id=request.POST['id']).count()
        if(tmp):
            tmp = Templates.objects.filter(id=request.POST['id']).get()
            ind = tmp.ind
            pack = tmp.pack
            return JsonResponse({"ind":str(ind),"pack":str(pack)},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})





def ajax_call_fetch_user(request):                                   # AJAX call Fetch user - By Admin
    if(auth_admin(request) and request.method=="POST"):
        user = User_db.objects.filter(email=request.POST['email']).count()
        if(user):
            return JsonResponse({"value":"found"},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})














def admin_new_booking_form(request):                                   # Admin add new Booking Form

    if(not Templates.objects.filter(id=request.POST["tmp_id"]).count()):
        messages.add_message(request, messages.INFO,"Template not exists !")

    if(not User_db.objects.filter(email=request.POST["email"]).count()):
        messages.add_message(request, messages.INFO,"User (email id) not exists !")
    
    if(messages.get_messages(request)):
        return redirect('/admin-add-booking')


    if(auth_admin(request) and request.method=="POST"):
       
        book =  User_bookings()
        book.title=request.POST["name"]
        book.user = User_db.objects.get(email=request.POST["email"])
        book.template= Templates.objects.get(id=request.POST["tmp_id"])
        book.save()

        return redirect("/admin-all-bookings")
    else:
        return redirect('/login')






def booking_view_by_get(request,id):                                   # Booking Update by GET method by Admin
    if(auth_admin(request)):
        data =  User_bookings.objects.get(id=id)
        if(data):
            return render(request,'bmanage/admin-booking-view.html',{'data':data})  

        else:
            return redirect('/login')
    else:
        return redirect('/login')










def booking_update_by_get(request,id):                                   # Booking Update by GET method by Admin
    if(auth_admin(request)):

        book =  User_bookings.objects.get(id=id)
        tmps = Templates.objects.all()

        if(book):
            return render(request,'bmanage/admin-booking-update.html',{'data':book,'tmps':tmps})  
        else:
            return redirect('/login')
    else:
        return redirect('/login')








def admin_booking_update_form(request):                                   # Admin Booking update Form


    id=request.POST["id"]

    if(not Templates.objects.filter(id=request.POST["tmp_id"]).count()):
        messages.add_message(request, messages.INFO,"Template not exists !")

    if(not User_db.objects.filter(email=request.POST["email"]).count()):
        messages.add_message(request, messages.INFO,"User (email id) not exists !")
    
    if(messages.get_messages(request)):
        return redirect('/booking_update_by_get/'+str(id))


    book = User_bookings.objects.get(id=id)

    if(auth_admin(request) and book and request.method=="POST"):
       
        book.title=request.POST["name"]
        book.user = User_db.objects.get(email=request.POST["email"])
        book.template= Templates.objects.get(id=request.POST["tmp_id"])
        book.save()

        return redirect("/admin-all-bookings")
    else:
        return redirect('/login')









def ajax_call_delete_booking(request):                                   # AJAX call DELETE Booking - By Admin
    if(auth_admin(request) and request.method=="POST"):
        book = User_bookings.objects.get(id=request.POST['id'])
        if(book):
            book.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})







def superplan_booking_view_by_get(request,id):                                   # Superplan booking view by GET method by Admin
    if(auth_admin(request)):
        book =  super_plan_forms.objects.get(id=id)
        if(book):
            return render(request,'bmanage/admin-superplan-booking-view.html',{'data':book})  

        else:
            return redirect('/login')
    else:
        return redirect('/login')








def ajax_call_delete_superplan_booking(request):                                   # AJAX call DELETE Superplan Booking - By Admin
    if(auth_admin(request) and request.method=="POST"):
        book = super_plan_forms.objects.get(id=request.POST['id'])
        if(book):
            book.delete()
            return JsonResponse({"value":request.POST['id']},status=200)
        else:
            return JsonResponse({"value":0})
    else:
        return JsonResponse({"value":0})