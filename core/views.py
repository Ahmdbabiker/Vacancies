from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _


def homepage(request , tag_id =None):
    
    tags = Category.objects.all()
    job_search = Vacancy.objects.all()
    paginator = Paginator(job_search , 12)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)


    if request.method == "POST":
        tags = Category.objects.all()
        searched = request.POST.get("job-search")
        side = request.POST.get("side") #gtaa
        jobtype = request.POST.get("jobtype")  #alagd
        location = request.POST.get("location")

        if searched:
            if location:
                if side:
                    if jobtype:
                        job_search = Vacancy.objects.filter(title__icontains=searched, location=location , 
                        jobtype=side , contracttype=jobtype)
        else:
            job_search = Vacancy.objects.filter(title__icontains=searched)
       
       

        
        dataa = {"job_search":job_search ,
         "searched":searched,"dis":searched  , "tags":tags}
        return render (request , 'home.html' , dataa)
    else:
        job_search = Vacancy.objects.all()
        dis = None
        searched = None

    
    if tag_id:
        job_search = Vacancy.objects.filter(tag_id = tag_id)
        paginator = Paginator(job_search , 9)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
    else:
        job_search = Vacancy.objects.all()

  

    data = {'tags':tags,
    'job_search':job_search , 'dis':dis ,
    'searched':searched , 'job_search':page_obj, }

    return render(request , 'home.html' , data)

def job_details(request , vacancy_slug):
    vacancy_detail = Vacancy.objects.get(slug = vacancy_slug)
    vacancy_tag = vacancy_detail.tag  # tag of the job
    vacancy_by_tag = Vacancy.objects.filter(tag = vacancy_tag).exclude(slug = vacancy_slug).order_by('?')[:3]

    if request.method == 'POST':
        name = request.POST.get("name")
        location = request.POST.get("location")
        date = request.POST.get("date")
        comment = request.POST.get("comment")
        print(date)
        comment_save = Comment.objects.create(name=name , location = location
         , comment =comment ,date = date, vacancy= vacancy_detail)
    
    count_comments = Comment.objects.filter(vacancy__slug = vacancy_slug)
    commentonjob = Comment.objects.filter(vacancy = vacancy_detail)
    
    
    data = {"vacancy" : vacancy_detail,
    "vacancy_tag":vacancy_by_tag ,
    "comment_save":commentonjob,
    "count_comments":count_comments}
    return render(request , 'job_details.html' , data)


def companies_emails(request):
    com_emasils = EmailCat.objects.all()
    data = {"com_emails":com_emasils}
    return render(request , 'emails.html', data)

def emaildetails(request , category_id):
    emails = EmailCat.objects.get(id= category_id )
    mails = emails.emails_set.all
  
    data = {"emails":mails }
    return render(request , 'email-details.html' , data)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")
        send_message = Sendmessage.objects.create(name=name , email=email,
        phone_number = number , message=message)
        messages.success(request, ' شكـرا لك , تم إرسال رسالتك ')


    return render(request , 'contactus.html' ) 


def services(request):
    if request.method == "POST":
        name = request.POST.get("name")
        title= request.POST.get("title")
        phone_no = request.POST.get("phone_no")
        budget = request.POST.get("budget")
        desc = request.POST.get("desc")
        service_create = Service.objects.create(
            name=name , phone_no = phone_no,  title=title,
            budget = budget , desc = desc
        )
        service_create.save()
        messages.success(request, 'تم نشر الخدمـة ')

    
    services = Service.objects.all().order_by('-id')
    paginator = Paginator(services , 8)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)


    
    data = {"services": services , "services":page_obj}
    return render(request , 'services.html' , data)

def service_detail(request , service_id):
    all_service = Service.objects.all().exclude(id = service_id).order_by('?')[:2]
    service_detail = Service.objects.get(id = service_id)
    service_detail.views += 1
    service_detail.save()
    data = {"service_detail":service_detail,
    'all_services':all_service}
    return render(request , 'servicesdetails.html' , data)


def policy(request):
    pass
    return render(request , "policy.html" )


def termspolicy(request):
    pass
    return render(request , "terms-condition.html" )


def createcv(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        wazzifa = request.POST.get("wazzifa")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        linkedurl = request.POST.get("linkedurl")

        prof = request.POST.get("prof")

        aqq = request.POST.get("quali")
        aqq_date_ = request.POST.get("qualidate")

      
     
        namepro = request.POST.get("namepro")
        comname = request.POST.get("comname")
        prodes = request.POST.get("prodes")
        stdate = request.POST.get("stdate")
        endate = request.POST.get("endate")


        trof = request.POST.get("trof")
        trofdate = request.POST.get("trofdate")

        proj = request.POST.get("proj")
        projdate = request.POST.get("projdate")
        skill = request.POST.get("skill")
        langu = request.POST.get("langu")

        cv_save = CVorders.objects.create(
        fullname = fullname , job_title=wazzifa,
        phone=phone , email=email , dof=dob , address=address,
        likndein= linkedurl , professional_summary=prof,
        qualification1=aqq , qualification_date1=aqq_date_,
        
        practical_experience=namepro,practical_comp=comname,
        practrical_summ=prodes,practical_start=stdate,
        practical_end=endate,torpihe=trof,troph_date=trofdate,
        project=proj,pro_date=projdate,skill=skill,
        langugaes=langu
        )

        cv_save.save()
        
       
       

    return render(request , 'cvbuilder.html' )