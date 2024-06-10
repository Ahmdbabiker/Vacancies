from django.db import models
from django.utils.text import Truncator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    CHOISES = (
        ('abudhabi' , 'أبوظبي'),
        ('dubai' , 'دبي'),
        ('sharjah' , 'الشارقة'),
        ('fujairah' , 'الفحيرة'),
        ('rak' , 'راس الخيمة'),
        ('ajman' , 'عجمان'),
    )

    WORKTYPE = (
        ('full' , 'دوام كامل'),
        ('part' , 'دوام جزئي'),
        ('remot' , 'عمل عن بعد')
    )

    CHOISES2 = (
        ('spec' , 'جهة خاصة'),
        ('gover' , 'جهة حكومية'),
    )

    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length = 20 , null=True)
    tag = models.ForeignKey(Category , on_delete=models.CASCADE)
    contracttype = models.CharField(max_length=10 ,null=True, choices=WORKTYPE)
    jobtype = models.CharField(max_length=10 , choices=CHOISES2)
    location = models.CharField(max_length=10 , choices=CHOISES)
    desc = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    applying = models.CharField(max_length=50 , null=True)

    def count_comments(self):
        return Comment.objects.get(vacancy = self ).count()


    def __str__(self):
        return Truncator (self.title).chars(40)


class Comment(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=15)
    comment  = models.TextField(null=True)
    date = models.DateField(null=True)
    vacancy = models.ForeignKey(Vacancy , on_delete=models.CASCADE , related_name='vacancies')
    date_commented = models.DateTimeField(auto_now_add=True , null=True)

 
    def __str__(self):
        return f"{self.name} commented on {self.vacancy}"


class EmailCat(models.Model):
    name = models.CharField(max_length=40 , null=True)

    def __str__(self):
        return self.name


class Emails(models.Model):
    name = models.CharField(max_length=40 , null= True)
    contact = models.CharField(max_length=30)
    specialist = models.ForeignKey(EmailCat , on_delete=models.CASCADE , null=True)

    def __str__(self):
        return f"{self.name} contact:: {self.contact}"


class Advertisement(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    message = models.TextField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    whatsapp_no = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.name} orderd in {self.date_ordered}"


class Service(models.Model):
    name =  models.CharField(max_length=40)
    phone_no = models.IntegerField()
    title = models.CharField(max_length=30)
    budget = models.IntegerField()
    desc = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} posted a service {self.title}"

class Sendmessage(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.IntegerField()
    message = models.TextField()


    def __str__(self):
        return f"{self.name} sent a Message"

class CVorders(models.Model):
    fullname = models.CharField(max_length=100)
    job_title = models.CharField(max_length=70)
    phone = models.IntegerField()
    email = models.EmailField()
    dof = models.DateField()
    address = models.CharField(max_length=70)
    likndein = models.CharField(max_length=250)
    professional_summary = models.TextField()
    qualification1 = models.CharField(max_length=400 , blank=True , null=True)
    qualification_date1 = models.DateField( blank=True , null=True)
    qualification2 = models.CharField(max_length=400, blank=True , null=True)
    qualification_date2 = models.DateField( blank=True , null=True)
    qualification3 = models.CharField(max_length=400, blank=True , null=True)
    qualification_date3 = models.DateField( blank=True , null=True)
    qualification4 = models.CharField(max_length=400, blank=True , null=True)
    qualification_date4 = models.DateField( blank=True , null=True)
    
    practical_experience= models.CharField(max_length=300)
    practical_comp = models.CharField(max_length=255)
    practrical_summ = models.TextField()
    practical_start = models.DateField()
    practical_end = models.DateField()

    practical_experience1= models.CharField(max_length=300, blank=True , null=True)
    practical_comp1 = models.CharField(max_length=255, blank=True , null=True)
    practrical_summ1 = models.TextField( blank=True , null=True)
    practical_start1 = models.DateField( blank=True , null=True)
    practical_end1 = models.DateField( blank=True , null=True)

    practical_experience2= models.CharField(max_length=300, blank=True , null=True)
    practical_comp2 = models.CharField(max_length=255, blank=True , null=True)
    practrical_summ2 = models.TextField( blank=True , null=True)
    practical_start2 = models.DateField( blank=True , null=True)
    practical_end2 = models.DateField( blank=True , null=True)

    practical_experience3= models.CharField(max_length=300, blank=True , null=True)
    practical_comp3 = models.CharField(max_length=255, blank=True , null=True)
    practrical_summ3 = models.TextField( blank=True , null=True)
    practical_start3 = models.DateField( blank=True , null=True)
    practical_end3 = models.DateField( blank=True , null=True)

    practical_experience4= models.CharField(max_length=300, blank=True , null=True)
    practical_comp4 = models.CharField(max_length=255, blank=True , null=True)
    practrical_summ4 = models.TextField( blank=True , null=True)
    practical_start4 = models.DateField( blank=True , null=True)
    practical_end4 = models.DateField(blank=True , null=True)

    torpihe = models.CharField(max_length=250)
    troph_date = models.DateField()

    torpihe1 = models.CharField(max_length=250, blank=True , null=True)
    troph_date1 = models.DateField( blank=True , null=True)

    torpihe2 = models.CharField(max_length=250, blank=True , null=True)
    troph_date2 = models.DateField( blank=True , null=True)

    torpihe3 = models.CharField(max_length=250, blank=True , null=True)
    troph_date3 = models.DateField( blank=True , null=True)

    project = models.CharField(max_length=250)
    pro_date = models.DateField()

    project1 = models.CharField(max_length=250, blank=True , null=True)
    pro_date1= models.DateField( blank=True , null=True)

    project2 = models.CharField(max_length=250, blank=True , null=True)
    pro_date2 = models.DateField( blank=True , null=True)

    project3 = models.CharField(max_length=250, blank=True , null=True)
    pro_date3 = models.DateField( blank=True , null=True)

    skill = models.CharField(max_length=200)
    langugaes = models.CharField(max_length=250)