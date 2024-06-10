
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , homepage , name="home"),
    path('<int:tag_id>' , homepage , name="tags_search"),
    path('<slug:vacancy_slug>/' , job_details , name="job_detail"),
    path('companiesemails' , companies_emails , name="emails" ),
    path('companiesemails/<int:category_id>/' , emaildetails , name='emaildetails'),
    path('getting/service' , services , name="services"),
    path('getting/service/<int:service_id>' , service_detail , name = "servicedetail"),
    path('createCV/fillData' , createcv , name="createcv"),
    path('site/policy/' , policy , name="policy"),
    path('terms&/policy/' , termspolicy , name="terms"),
    path('contact/us', contact , name="contactus"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
