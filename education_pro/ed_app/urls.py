from django.contrib import admin
from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # path("/<slug>",Home.as_view(),name="home"),
    path("", Home.as_view(), name="home"),
    path("<slug>/",Homeslug.as_view(),name="Homeslug"),
    path("category/<ct_slug>", Category_gp.as_view(), name="category"),

    path("mbbs-in-georgia",Mbbsgeorgia.as_view(),name="mbbsgeorgia"),
    path("mbbs-in-china",Mbbschina.as_view(),name="mbbschina"),
    path("mbbs-in-nepal",Mbbsnepal.as_view(),name="mbbsnepal"),
    path("mbbs-in-philippines",Mbbsphilippines.as_view(),name="mbbsphilippines"),
    path("mbbs-in-ukraine",Mbbsukraine.as_view(),name="mbbsukraine"),
    path("mbbs-in-russia",Mbbsrussia.as_view(),name="mbbsrussia"),
    path("mbbs-in-bangladesh",Mbbsbangladesh.as_view(),name="mbbsbangladesh"),
    path("mbbs-in-kazakhstan",Mbbskazakhstan.as_view(),name="mbbskazakhstan"),
    path("mbbs-in-uzbekistan",Mbbsuzbekistan.as_view(),name="mbbsuzbekistan"),
    path("mbbs-migration-to-armenia",Mbbsarmenia.as_view(),name="mbbsarmenia"),
    path("mbbs-in-kyrgyzstan",Mbbskyrgyzstan.as_view(),name="mbbskyrgyzstan"),
    path("md-ms-admission-india",Mdindia.as_view(),name="mdindia"),
    path("cps-fcps",Cpsfcps.as_view(),name="cpsfcps"),
    path("study-bams-in-india",Studyindia.as_view(),name="studyindia"),
    path("study-bhms-in-india",Studybhmsindia.as_view(),name="studybhmsindia"),
    path("study-bds",Studybds.as_view(),name="studybds"),
    path("study-bums-in-india",Studybumsindia.as_view(),name="studybumsindia"),


    path("mbbs-in-india",Mbbsinindia.as_view(),name="mbbsinindia"),
    path("about",About.as_view(),name="about"),
    path("blog",Blog.as_view(),name="blog"),
    path("contact",Contact.as_view(),name="contact"),
    path("apply-online",Applyonline.as_view(),name="applyonline"),
    path("jee-mains",Jeemains.as_view(),name="jeemains"),
    path("management",Management.as_view(),name="management"),
    path("study-bsc-nursing",Bsc_nursing.as_view(),name="bsc_nursing"),
    path("adminsion_data_form",adminsion_data_form.as_view(),name="adminsion_data_form"),
    path("top-mbbs-colleges-in-hyderabad",Colleges_hyderabad.as_view(),name="Colleges_hyderabad"),
    path("top-mbbs-colleges-in-lucknow",top_mbbs_colleges_in_lucknow.as_view(),name="top_mbbs_colleges_in_lucknow"),    
    path("top-mbbs-olleges-in-pondicherry",top_mbbs_olleges_in_pondicherry.as_view(),name="top_mbbs_olleges_in_pondicherry"),    
    path("top-mbbs-colleges-in-dehradun",top_mbbs_colleges_in_dehradun.as_view(),name="top_mbbs_colleges_in_dehradun"),    
    path("top-mbbs-colleges-in-bangalore",top_mbbs_colleges_in_bangalore.as_view(),name="top_mbbs_colleges_in_bangalore"),    
    path("top-mbbs-colleges-in-bhopa",top_mbbs_colleges_in_bhopal.as_view(),name="top_mbbs_colleges_in_bhopal"),
    path("top-mbbs-colleges-in-kolkata",top_mbbs_colleges_in_kolkata.as_view(),name="top_mbbs_colleges_in_kolkata"),    
    path("top-mbbs-colleges-in-chennai",top_mbbs_colleges_in_chennai.as_view(),name="top_mbbs_colleges_in_chennai"),    
    path("top-mbbs-colleges-in-bhubaneswar",top_mbbs_colleges_in_bhubaneswar.as_view(),name="top_mbbs_colleges_in_bhubaneswar"),    
    path("top-mbbs-colleges-in-new-delhi",top_mbbs_colleges_in_new_delhi.as_view(),name="top_mbbs_colleges_in_new_delhi"),    
    path("top-mbbs-colleges-in-mangalore",top_mbbs_colleges_in_mangalore.as_view(),name="top_mbbs_colleges_in_mangalore"),    
    path("top-mbbs-colleges-in-pune",top_mbbs_colleges_in_pune.as_view(),name="top_mbbs_colleges_in_pune"),    
     
    path("top-mbbs-in/<slug>",page_blog_details.as_view(),name="page_blog_details"),    
     
]


# handler404 = 'ed_app.views.error_400'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
