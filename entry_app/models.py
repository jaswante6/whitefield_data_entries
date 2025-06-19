from django.db import models

# Create your models here.

class PersonalInfo(models.Model):
    """Model to store personal and professional information"""
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def is_business(self):
        """Check if the profession is business"""
        return self.profession.lower() == 'business'

class BusinessAd(models.Model):
    """Model to store business advertisements"""
    business = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='ads')
    headline = models.CharField(max_length=200)
    description = models.TextField()
    offers = models.TextField(blank=True, null=True, help_text="Special offers and promotions")
    home_delivery = models.BooleanField(default=False, help_text="Whether home delivery is available")
    free_delivery = models.BooleanField(default=False, help_text="Whether free delivery is available")
    delivery_areas = models.CharField(max_length=200, blank=True, null=True, help_text="Areas where delivery is available")
    keywords = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.business.name}'s Ad: {self.headline}"

class JobAd(models.Model):
    """Model to store job recruitment advertisements"""
    EMPLOYMENT_TYPE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
        ('internship', 'Internship'),
    ]
    
    EXPERIENCE_LEVEL_CHOICES = [
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level'),
        ('executive', 'Executive'),
    ]
    
    employer = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, related_name='job_ads')
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE_CHOICES, default='full_time')
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES, default='entry')
    description = models.TextField(help_text="Detailed job description")
    responsibilities = models.TextField(help_text="Job responsibilities")
    qualifications = models.TextField(help_text="Required qualifications")
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    application_deadline = models.DateField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.company_name}: {self.job_title}"
