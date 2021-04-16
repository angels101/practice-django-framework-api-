from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.

class Location(models.Model):
    country = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(null=True)
    address = models.IntegerField(null=True)

    def __str__(self):
        return self.country

class Followers(models.Model):
    follower = models.ForeignKey(User, related_name='followers', null=True,on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', null=True,on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)

    def follow_user(self, current_user, user_other):
        self.following = user_other
        self.follower = current_user
        self.save()

    def unfollow_user(self, user):
        fol = self.objects.get(follower=user)
        fol.delete()

    def __str__(self):
        return f'{self.follower.username} is now following {self.following.username}'

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', null=True,on_delete=models.CASCADE)
#    post = models.ForeignKey(Post, related_name='ratings', null=True,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    usability = models.FloatField(default=0.00, null=True)
    design = models.FloatField(default=0.00, null=True)
    creativity = models.FloatField(default=0.00, null=True)
    content = models.FloatField(default=0.00, null=True)
    mobile = models.FloatField(default=0.00, null=True)

    @property
    def average_judge_rating(self, null=True):
        rated = [i for i in [self.usability, self.design,
                             self.creativity, self.content, self.mobile] if i != None]
        if len(rated) == 0:
            return 0.00
        else:
            rating = sum(rated[0:len(rated)])/len(rated)
            return math.floor(rating * 100)/100.0

    @classmethod
    def average_usability(cls, post):
        post_ratings = Rating.objects.filter(post=post)
        _all = [ur.usability for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 100)/100.0

    @property
    def av_usability(self):
        post_ratings = Rating.objects.filter(post=self.post)
        _all = [ur.usability for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 10)/10.0

    @classmethod
    def average_design(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.design for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 100)/100.0

    @property
    def av_design(self):
        post_ratings = Rating.objects.filter(post=self.post)
        _all = [ur.design for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 10)/10.0

    @classmethod
    def average_creativity(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.creativity for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 100)/100.0

    @property
    def av_creativity(self):
        post_ratings = Rating.objects.filter(post=self.post)
        _all = [ur.creativity for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 10)/10.0

    @classmethod
    def average_content(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.content for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 100)/100.0

    @property
    def av_content(self):
        post_ratings = Rating.objects.filter(post=self.post)
        _all = [ur.content for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 10)/10.0

    @classmethod
    def average_mobile(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.mobile for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 100)/100.0

    @property
    def av_mobile(self):
        post_ratings = Rating.objects.filter(post=self.post)
        _all = [ur.mobile for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 10)/10.0

    @classmethod
    def average_rating(cls, post):
        post_ratings = cls.objects.filter(post=post)
        _all = [ur.average_judge_rating for ur in post_ratings]
        if len(_all) == 0:
            return 0.00
        else:
            average = sum(_all)/len(_all)
            return math.floor(average * 100)/100.0

    @property
    def get_last_post(self):
        return Rating.objects.last()





class User_profile(models.Model):
    """
    class that creates an instance of a user profile
    """
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=40)
    profile_pic = ImageField(blank=True,manual_crop="")
    email = models.EmailField() 
    phone_number = models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        return self.save()
    
    def delete_profile(self):
        profile=User_profile.objects.all().delete()
        return profile
    
    @classmethod
    def get_profile(cls,id):
        profile = User_profile.objects.get(user=id)
        return profile
        
    

class Projects(models.Model):
    """
    class that creates instance of a project
    """
    title = models.CharField(max_length=50)
    image = ImageField(blank=True,manual_crop="")
    description = models.TextField()
    project_link = models.URLField(max_length=250,default=None)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save_project(self):
        return self.save()
    
    def delete_project(self):
        proj = Projects.objects.all().delete()
        return proj
    
    '''
    method to search for projects
    '''
    @classmethod
    def search_project(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project
        
    @classmethod
    def get_one_project(cls,id):
        project=cls.objects.get(id=id)
        return project   
    
    class Meta:
        ordering = ['pub_date']
        
    @classmethod
    def get_project_id(cls,project_id):
        '''
        function that gets an project id    
        '''
        project_id=cls.objects.filter(id=project_id)
        return project_id
        
class Rate(models.Model):
    RATING_CHOICES = ((1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'),(6,'six'),(7,'seven'),(8,'eight'),(9,'nine'),(10,'ten'))
    design = models.PositiveSmallIntegerField('Rating(stars)',blank=True,default=0,choices=RATING_CHOICES)
    usability = models.PositiveSmallIntegerField('Rating(stars)',blank=True,default=0,choices=RATING_CHOICES)
    content = models.PositiveSmallIntegerField('Rating(stars)',blank=True,default=0,choices=RATING_CHOICES)
    score = models.PositiveSmallIntegerField('Rating(stars)',blank=True,default=0)
    post_rated = models.ForeignKey(Projects,on_delete=models.CASCADE,related_name='ratings',null=True)
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True) 
    
    class Meta:
        abstract = True
        
    @classmethod
    def get_ratings(cls,id):
        ratings = Rate.objects.filter(project_id=id).all()
        return ratings   
        
class Review(models.Model):
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)   
    comment = models.TextField()
    posted_by = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    
    def save_review(self):
        return self.save()
    
    def delete_review(self):
        return self.delete()
    
    def __str__(self):
        return self.comment
    
     
     
    @classmethod
    def get_review(cls,id):
        comments = cls.objects.filter(project_id__in=id)
        return comments