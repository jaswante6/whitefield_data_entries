import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'data_entry_project.settings')
django.setup()

from entry_app.models import PersonalInfo, BusinessAd, JobAd

# Check businesses
businesses = PersonalInfo.objects.filter(profession__iexact='business')
print(f"Number of businesses found: {businesses.count()}")
for business in businesses:
    print(f"Business: {business.name}, ID: {business.id}")

# Check business ads
ads = BusinessAd.objects.all()
print(f"\nNumber of business ads found: {ads.count()}")
for ad in ads:
    print(f"Ad: {ad.headline}, Business: {ad.business.name}, ID: {ad.id}")
    print(f"  Offers: {ad.offers}")
    print(f"  Delivery: Home={ad.home_delivery}, Free={ad.free_delivery}, Areas={ad.delivery_areas}")

# Check job ads
jobs = JobAd.objects.all()
print(f"\nNumber of job ads found: {jobs.count()}")
for job in jobs:
    print(f"Job: {job.job_title}, Company: {job.company_name}, ID: {job.id}") 