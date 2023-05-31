from django.db import models
from froala_editor.fields import FroalaField
from autoslug import AutoSlugField
# Create your models here.
class Admissionform(models.Model):
    name =models.CharField(max_length=300)
    number =models.IntegerField()
    email =models.EmailField()
    course=models.CharField(max_length=300)
    massage=models.TextField(max_length=300)

    def __str__(self) -> str:
        return self.name
    
    
class Category(models.Model):
    category=models.CharField(max_length=1000)
    ct_slug=AutoSlugField(populate_from='category',unique=True, max_length=800,default="")
    def __str__(self) -> str:
        return self.category

class Blog_post(models.Model):
    author=models.CharField(max_length=550)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    blog_hesed=models.TextField(blank=True)
    blog_image=models.ImageField(upload_to="letestblog/")
    blog_title=models.CharField(max_length=250)
    blog_alt_name=models.CharField(max_length=500)
    
    blog_meta_discreption=models.CharField(max_length=500,null=True,blank=True)
    blog_meta_og_discreption=models.CharField(max_length=500,null=True,blank=True)
    blog_meta_keyword=models.CharField(max_length=500,null=True,blank=True)
    
    blog_small_content=FroalaField()
    blog_content=FroalaField()
    blog_url=models.CharField(max_length=250)
    slug=AutoSlugField(populate_from='blog_url',unique=True, max_length=1000,default='')
    date=models.DateTimeField()
    

class Contact_form(models.Model):
    name =models.CharField(max_length=300)
    email =models.EmailField()
    massage=models.TextField()
    
    def __str__(self) -> str:
        return self.name
 

class Onlin_apply_form(models.Model):
    name =models.CharField(max_length=300)
    number =models.IntegerField()
    email =models.EmailField()
    course=models.CharField(max_length=300,blank=True,null=True)
    massage=models.TextField(max_length=300,blank=True,null=True)
    
    customer_image=models.ImageField(upload_to="media/user_admison/",blank=True,null=True)

    def __str__(self) -> str:
        return self.name
    
class Quick_Registration(models.Model): 
    name =models.CharField(max_length=300)
    number =models.IntegerField()
    email =models.EmailField()
    course=models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name

class Comments_users(models.Model): 
    name =models.CharField(max_length=300)
    email =models.EmailField()
    web=models.CharField(max_length=300)
    commnet=models.TextField(max_length=200)
    checkbtn=models.BooleanField("Show this comment")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Page_catrgery(models.Model):
    
    html_page_name=models.CharField(max_length=500)
    def __str__(self) -> str:
        return self.html_page_name
   


class html_blogs_post(models.Model):
    author=models.CharField(max_length=550)
    pg_category=models.ForeignKey(Page_catrgery,on_delete=models.CASCADE)
    post_image=models.ImageField(upload_to="html_page/")
    post_title=models.CharField(max_length=250)
    post_alt_name=models.CharField(max_length=500)
    post_meta_discreption=models.CharField(max_length=500,null=True,blank=True)
    description=FroalaField()
    date=models.DateField()
    htmlbcslug=AutoSlugField(populate_from='post_title',unique=True, max_length=1000,default='')
    def __str__(self) -> str:
        return self.post_title
    
 
class Html_maker(models.Model):

    slect_web_page=models.ForeignKey(Page_catrgery,on_delete=models.CASCADE)
    page_title=models.CharField(max_length=550)
    first_heding_h1tag=models.CharField(max_length=100)
    meta_des=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.page_title
    
    
   
    