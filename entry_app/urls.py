from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # path('', views.home, name='home'),
    path('entries/', views.PersonalInfoListView.as_view(), name='list_entries'),
    path('entries/add/', views.PersonalInfoCreateView.as_view(), name='add_entry'),
    path('entries/<int:pk>/edit/', views.PersonalInfoUpdateView.as_view(), name='edit_entry'),
    path('entries/<int:pk>/delete/', views.PersonalInfoDeleteView.as_view(), name='delete_entry'),
    path('business/<int:pk>/ad/', views.business_ad_view, name='business_ad'),
    path('business-ads/', views.business_ads_list, name='business_ads_list'),
    path('job-ads/', views.job_ads_list, name='job_ads_list'),
    path('job-ads/create/', views.job_ad_create, name='job_ad_create'),
] 