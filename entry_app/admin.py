from django.contrib import admin
from .models import PersonalInfo, BusinessAd, JobAd

# Register your models here.
@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'city', 'state', 'created_at')
    search_fields = ('name', 'profession', 'city', 'state')
    list_filter = ('profession', 'city', 'state')

@admin.register(BusinessAd)
class BusinessAdAdmin(admin.ModelAdmin):
    list_display = ('headline', 'business', 'created_at')
    search_fields = ('headline', 'description', 'keywords', 'business__name')
    list_filter = ('created_at', 'business')

@admin.register(JobAd)
class JobAdAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'location', 'employment_type', 'created_at')
    search_fields = ('job_title', 'company_name', 'description', 'responsibilities', 'qualifications')
    list_filter = ('employment_type', 'experience_level', 'created_at')
    date_hierarchy = 'created_at'
