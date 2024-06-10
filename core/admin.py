from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Category)
admin.site.register(Comment)
@admin.register(Vacancy)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}

admin.site.register(Emails)
admin.site.register(EmailCat)
admin.site.register(Advertisement)
admin.site.register(Service)
admin.site.register(Sendmessage)
admin.site.register(CVorders)