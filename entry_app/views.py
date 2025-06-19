from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.dateparse import parse_date
from .models import PersonalInfo, BusinessAd, JobAd
from .forms import PersonalInfoForm

# Create your views here.
def home(request):
    # Get counts for dashboard
    entries_count = PersonalInfo.objects.count()
    ads_count = BusinessAd.objects.count()
    jobs_count = JobAd.objects.count()
    
    context = {
        'entries_count': entries_count,
        'ads_count': ads_count,
        'jobs_count': jobs_count
    }
    
    return render(request, 'entry_app/home.html', context)

def business_ads_list(request):
    """View to display all business advertisements"""
    ads = BusinessAd.objects.select_related('business').order_by('-created_at')
    return render(request, 'entry_app/business_ads_list.html', {'ads': ads})

def job_ads_list(request):
    """View to display all job recruitment advertisements"""
    jobs = JobAd.objects.select_related('employer').order_by('-created_at')
    return render(request, 'entry_app/job_ads_list.html', {'jobs': jobs})

def job_ad_create(request):
    """View to create a new job ad"""
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        location = request.POST.get('location')
        employment_type = request.POST.get('employment_type')
        experience_level = request.POST.get('experience_level')
        description = request.POST.get('description')
        responsibilities = request.POST.get('responsibilities')
        qualifications = request.POST.get('qualifications')
        salary_range = request.POST.get('salary_range')
        application_deadline = request.POST.get('application_deadline')
        contact_email = request.POST.get('contact_email')
        
        # Use the first business person as employer (this should be improved in a real-world app)
        employer = PersonalInfo.objects.filter(profession__iexact='business').first()
        
        if not employer:
            messages.error(request, "No business profiles found to create job ads.")
            return redirect('list_entries')
        
        if job_title and company_name and description:
            # Create a new job ad
            job = JobAd(
                employer=employer,
                job_title=job_title,
                company_name=company_name,
                location=location,
                employment_type=employment_type,
                experience_level=experience_level,
                description=description,
                responsibilities=responsibilities,
                qualifications=qualifications,
                salary_range=salary_range,
                application_deadline=parse_date(application_deadline) if application_deadline else None,
                contact_email=contact_email
            )
            job.save()
            messages.success(request, "Your job advertisement has been published successfully!")
            return redirect('job_ads_list')
        else:
            messages.error(request, "Please provide a job title, company name, and description.")
    
    # Render the form
    context = {
        'employment_types': JobAd.EMPLOYMENT_TYPE_CHOICES,
        'experience_levels': JobAd.EXPERIENCE_LEVEL_CHOICES
    }
    return render(request, 'entry_app/job_ad_form.html', context)

class PersonalInfoListView(ListView):
    model = PersonalInfo
    template_name = 'entry_app/list.html'
    context_object_name = 'entries'
    ordering = ['-created_at']

class PersonalInfoCreateView(CreateView):
    model = PersonalInfo
    form_class = PersonalInfoForm
    template_name = 'entry_app/form.html'
    
    def get_success_url(self):
        # If the user's profession is business, redirect to the business ad page
        if self.object.is_business():
            return reverse_lazy('business_ad', kwargs={'pk': self.object.pk})
        return reverse_lazy('list_entries')

class PersonalInfoUpdateView(UpdateView):
    model = PersonalInfo
    form_class = PersonalInfoForm
    template_name = 'entry_app/form.html'
    
    def get_success_url(self):
        # If the user's profession is business, redirect to the business ad page
        if self.object.is_business():
            return reverse_lazy('business_ad', kwargs={'pk': self.object.pk})
        return reverse_lazy('list_entries')

class PersonalInfoDeleteView(DeleteView):
    model = PersonalInfo
    template_name = 'entry_app/confirm_delete.html'
    success_url = reverse_lazy('list_entries')

def business_ad_view(request, pk):
    business = get_object_or_404(PersonalInfo, pk=pk)
    
    # If the person is not a business professional, redirect to the list
    if not business.is_business():
        messages.warning(request, "This feature is only available for business professionals.")
        return redirect('list_entries')
    
    # Handle form submission
    if request.method == 'POST':
        headline = request.POST.get('ad_headline')
        description = request.POST.get('ad_description')
        offers = request.POST.get('ad_offers')
        home_delivery = request.POST.get('home_delivery') == 'on'
        free_delivery = request.POST.get('free_delivery') == 'on'
        delivery_areas = request.POST.get('delivery_areas')
        keywords = request.POST.get('ad_keywords')
        
        if headline and description:
            # Create a new business ad
            ad = BusinessAd(
                business=business,
                headline=headline,
                description=description,
                offers=offers,
                home_delivery=home_delivery,
                free_delivery=free_delivery,
                delivery_areas=delivery_areas,
                keywords=keywords
            )
            ad.save()
            messages.success(request, "Your business advertisement has been published successfully!")
        else:
            messages.error(request, "Please provide a headline and description for your advertisement.")
    
    # Get existing ads for this business
    ads = BusinessAd.objects.filter(business=business).order_by('-created_at')
    
    context = {
        'business': business,
        'ads': ads
    }
    
    return render(request, 'entry_app/business_ad.html', context)
