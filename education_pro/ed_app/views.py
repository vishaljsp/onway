from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse,HttpResponse
# Create your views here.
from . models import *
from django.core.paginator import Paginator

class Sendigdata:
    def __init__(self):
        self.cat = Category.objects.all()
        self.blog = Blog_post.objects.all().order_by('-id')
        self.coments=Comments_users.objects.all()
        self.count_cat_blog = {category: f'{category.category} ({count})' for category, count in {category: self.blog.filter(category=category).count() for category in self.cat}.items()}
        
    def pagnet(self,request):
        paginet=Paginator(self.blog,2)
        page=request.GET.get('page')
        blogs001=paginet.get_page(page)
        return blogs001
    
    def getingid(self,request):
        relativ_post_id=request.session.get("cat_id_post")        
        post=Blog_post.objects.filter(category_id=relativ_post_id)
        return post

    
class adminsion_data_form(View):
    def get(self, request):
        return render(request, "adminsion_data_form.html")

    def post(self, request):
        # admition form 
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("num")
        course = request.POST.get("course")
        massage = request.POST.get("mass")  # Corrected field name

        # comment data 
        coment = request.POST.get("coment")
        c_name = request.POST.get("name")
        c_email = request.POST.get("email")
        web = request.POST.get("web")
         # relative post 
        post_cat_id = request.POST.get("cat_id_relative_post")

        if name and email and number and course and massage:
           Admissionform(name=name, email=email, course=course, number=number, massage=massage).save()
           
        elif coment and name and email and web:
            Comments_users(name=c_name,email=c_email,web=web,commnet=coment,checkbtn=False).save()
        else:
            pass
        
        if post_cat_id:
            print(post_cat_id,"==++++++")
            request.session['cat_id_post']=post_cat_id
            
        return HttpResponse("ok")
    

class Homeslug(Sendigdata,View):
    def get(self,request,slug):
        blogs_slug=Blog_post.objects.filter(slug=slug).first()        
        data={
           
            "blogs":blogs_slug,       
            "cat0":self.count_cat_blog,
        }
        return render(request,"blogs.html",data)
        
        
class Home(View):
    def get(self, request):
       
    
        return render(request, "index.html")
    
class Category_gp(Sendigdata,View):
    def get(self, request, ct_slug):
        blogs_slug = Blog_post.objects.filter(category__ct_slug=ct_slug)
        
        r_post=self.getingid(request)
        data={
            "relative_post":r_post,            
            "cat0":self.count_cat_blog,
            'ct_blogs':blogs_slug
        }
        return render(request,"cat.html",data)
 
        
    
class Mbbsgeorgia(View):
    def get(self,request):
        return render(request,"mbbs-abroad/mbbs_gorga_india.html")
    
class Mbbschina(Sendigdata,View):
    def get(self,request):
        data={
            "comments":self.coments
        }
        return render(request,"mbbs-abroad/mbbs-in-china.html",data)

class Mbbsnepal(Sendigdata,View):
    def get(self,request):
        data={
            "comments":self.coments
        }
        return render(request,"mbbs-abroad/mbbs-in-nepal.html",data)

class Mbbsphilippines(View):
    def get(self,request):
        return render(request,"mbbs-abroad/mbbs-in-philippines.html")

class Mbbsukraine(View):
    def get(self,request):
        return render(request,"mbbs-abroad/mbbs-in-ukraine.html")
class Mbbsrussia(Sendigdata,View):
    def get(self,request):
        data={
            "comments":self.coments
        }
        return render(request,"mbbs-abroad/mbbs-in-russia.html",data)
class Mbbsbangladesh(View):
    def get(self,request):
        return render(request,"mbbs-abroad/mbbs-in-bangladesh.html")

class Mbbskazakhstan(View):
    def get(self,request):
        return render(request,"mbbs-abroad/mbbs-in-kazakhstan.html")

class Mbbsuzbekistan(View):
    def get(self,request):
        return render(request,"mbbs-abroad/mbbs-in-uzbekistan.html")

class Mbbsarmenia(Sendigdata,View):
    def get(self,request):
        data={
            "comments":self.coments
        }
        return render(request,"mbbs-abroad/mbbs-migration-to-armenia.html",data)


class Mbbskyrgyzstan(View):
    def get(self,request):
        return render(request,"mbbs-abroad/mbbs-in-kyrgyzstan.html")


################ study in india 

class Mdindia(Sendigdata,View):

    def get(self,request):

        r_post=self.getingid(request)
        data={
            "relative_post":r_post,            
            "cat0":self.count_cat_blog,
            "blog":self.blog
        }
        return render(request,"study_india/md-ms-admission-india.html",data)

class Cpsfcps(Sendigdata,View):
    def get(self,request):

        r_post=self.getingid(request)
        data={
            "relative_post":r_post,            
            "cat0":self.count_cat_blog,
            "blog":self.blog
        }
        return render(request,"study_india/cps-fcps.html",data)

class Studyindia(Sendigdata,View):
    def get(self,request):

        r_post=self.getingid(request)
        data={
            "relative_post":r_post,            
            "cat0":self.count_cat_blog,
            "blog":self.blog
        }
        return render(request,"study_india/study-bams-in-india.html",data)

class Studybhmsindia(Sendigdata,View):
    def get(self,request):

        r_post=self.getingid(request)
        data={
            "relative_post":r_post,            
            "cat0":self.count_cat_blog,
            "blog":self.blog
        }
        return render(request,"study_india/study-bhms-in-india.html",data)
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("num")
        course = request.POST.get("cors")
        
        Quick_Registration(name=name,number=number,email=email,course=course).save()
        return render(request,"study_india/study-bhms-in-india.html")

class Studybds(Sendigdata,View):
    def get(self,request):

        r_post=self.getingid(request)
        data={
            "relative_post":r_post,            
            "cat0":self.count_cat_blog,
            "blog":self.blog,
            "comments":self.coments
        }
        
        return render(request,"study_india/study-bds.html",data)

        
class Studybumsindia(Sendigdata,View):
    def get(self,request):

        r_post=self.getingid(request)
        data={
            "relative_post":r_post,            
            "cat0":self.count_cat_blog,
            "blog":self.blog,
            "comments":self.coments
            
        }
        return render(request,"study_india/study-bums-in-india.html",data)
    
    
############ after dropdown
    
class Mbbsinindia(Sendigdata,View):
    def get(self,request):
        data={
            "comments":self.coments
        }
        return render(request,"mbbs-in-india.html",data)

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("num")
        course = request.POST.get("cors")
        
        Quick_Registration(name=name,number=number,email=email,course=course).save()
        
        return render(request,"mbbs-in-india.html",)
        
    
class About(View):
    def get(self,request):
        return render(request,"about.html")
    
class Blog(Sendigdata,View):
    
    def get(self,request):
        search_val=request.GET.get("searchbar")
        cat_id=request.GET.get("cat_id")

        blog1=self.pagnet(request)

        if search_val:
            blog1=Blog_post.objects.filter(blog_title__icontains=search_val)
             
        elif cat_id:
            ct_id=Category.objects.filter(id=cat_id).first()
            blog_of_id=Blog_post.objects.filter(category=ct_id)
            blog1=blog_of_id
        # r_post=self.getingid(request)
        data={
            "relative_post":blog1,            
            "cat0":self.count_cat_blog,
            "blog":blog1,
        }
  
        return render(request,"blog.html",data)
    
    def post(self,request):
        
        
        return render(request,"blog.html")
        

class Contact(View):
    def get(self,request):
        return render(request,"contact.html")

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        ms = request.POST.get("massage")
        
        Contact_form(name=name, email=email, massage=ms).save()
        return render(request, "contact.html")

class Applyonline(View):
    def get(self,request):
        return render(request,"apply-online.html")
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("num")
        course = request.POST.get("course")
        massage = request.POST.get("mass")  # Corrected field name
        
        image = request.POST.get("img")  
        # image = request.FILES.get("img")  # Corrected field name
        
        Onlin_apply_form(name=name,number=number,email=email,course=course,massage=massage,customer_image=image).save()

        return render(request,"apply-online.html")

class Jeemains(View):
    def get(self,request):
        return render(request,"jee-mains.html")

class Management(View):
    def get(self,request):
        return render(request,"management.html")

class Bsc_nursing(Sendigdata,View):
    def get(self,request):
        data={
            "comments":self.coments
        }
        return render(request,"study_india/study-bsc-nursing.html",data)
     
# making html by backend,
class Html_sendigdata:
    def __init__(self):
        self.page = Html_maker.objects.all()
       
        # self.blogs=None
        for a in self.page:
            if str(a.slect_web_page) == "Top MBBS Colleges in Hyderabad":
                self.blogs=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_h=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()
            elif str(a.slect_web_page) ==  "Top MBBS Colleges in Pune":
                self.blogs_pune=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_h_pune=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()
            elif str(a.slect_web_page) ==  "Top MBBS Colleges in Lucknow":
                self.blogs_lucknow=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_h_lucknow=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()
            elif str(a.slect_web_page) ==  "Top MBBS Colleges in Pondicherry":
                self.blogspondicherry=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_hpondicherry=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()

            elif str(a.slect_web_page) ==  "Top MBBS Colleges in Dehradun":
                self.blogsDehradun=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_hDehradun=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()

            elif str(a.slect_web_page) ==  "Top MBBS Colleges in Bhopal":
                self.blogsBhopal=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_hBhopal=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()

            elif str(a.slect_web_page) ==  "Top MBBS Colleges in Kolkata":
                self.blogsKolkata=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_hKolkata=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()

            elif str(a.slect_web_page) ==  "Top MBBS Colleges in Chennai":
                self.blogsChennai=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_hChennai=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()

            elif str(a.slect_web_page) ==  "Top MBBS Colleges in Bhubaneswar":
                self.blogsBhubaneswar=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_hBhubaneswar=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()

            elif str(a.slect_web_page) ==  "Top MBBS Colleges in New Delhi":
                self.blogsDelhi=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_hDelhi=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()

            elif str(a.slect_web_page) ==  "Top MBBS Colleges in Mangalore":
                self.blogsMangalore=html_blogs_post.objects.filter(pg_category=a.slect_web_page)
                self.page_hMangalore=Html_maker.objects.filter(slect_web_page=a.slect_web_page).first()
        
class Colleges_hyderabad(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogs,
            "html_page_data":self.page_h
        }
        return render(request,"backendhtml/mbbs_hedrabad_college.html",data)
    
    
class top_mbbs_colleges_in_lucknow(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogs_lucknow,
            "html_page_data":self.page_h_lucknow,
        }
        return render(request,"backendhtml/top-mbbs-colleges-in-lucknow.html",data)
    
    
class top_mbbs_olleges_in_pondicherry(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogspondicherry,
            "html_page_data":self.page_hpondicherry
        }
        return render(request,"backendhtml/top-mbbs-olleges-in-pondicherry.html",data)
    
class top_mbbs_colleges_in_dehradun(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogsDehradun,
            "html_page_data":self.page_hDehradun
        }
        return render(request,"backendhtml/top_mbbs_colleges_in_dehradun.html",data)
    
class top_mbbs_colleges_in_bangalore(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogsBangalore,
            "html_page_data":self.page_hBangalore
        }
        return render(request,"backendhtml/top_mbbs_colleges_in_bangalore.html",data)
    
    
class top_mbbs_colleges_in_bhopal(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogsBhopal,
            "html_page_data":self.page_hBhopal
        }
        return render(request,"backendhtml/top_mbbs_colleges_in_bhopal.html",data)
    
class top_mbbs_colleges_in_kolkata(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogsKolkata,
            "html_page_data":self.page_hKolkata
        }
        return render(request,"backendhtml/top_mbbs_colleges_in_kolkata.html",data)
    
    
class top_mbbs_colleges_in_chennai(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogsChennai,
            "html_page_data":self.page_hChennai
        }
        return render(request,"backendhtml/top_mbbs_colleges_in_chennai.html",data)
    
class top_mbbs_colleges_in_bhubaneswar(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogsBhubaneswar,
            "html_page_data":self.page_hBhubaneswar
        }
        return render(request,"backendhtml/top_mbbs_colleges_in_bhubaneswar.html",data)
    
class top_mbbs_colleges_in_new_delhi(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogsDelhi,
            "html_page_data":self.page_hDelhi
        }
        return render(request,"backendhtml/top_mbbs_colleges_in_new_delhi.html",data)
    
class top_mbbs_colleges_in_mangalore(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogsMangalore,
            "html_page_data":self.page_hMangalore
        }
        return render(request,"backendhtml/top_mbbs_colleges_in_mangalore.html",data)
    
class top_mbbs_colleges_in_pune(Html_sendigdata,View):
    def get(self,request):
        data={
            "p_blogs":self.blogs_pune,
            "html_page_data":self.page_h_pune
        }
        return render(request,"backendhtml/top_mbbs_colleges_in_pune.html",data)
    
class page_blog_details(Sendigdata,View):
    def get(self,request,slug):
        pg_details=html_blogs_post.objects.filter(htmlbcslug=slug).first()
        # r_post=self.getingid(request)
        data={
            "blogs":pg_details,
           
            "cat0":self.count_cat_blog,
            "pg_dtails":pg_details,
        }
        return render(request,"backendhtml/details.html",data)
