from django.db import models

# Create your models here.


class Blog(models.Model):

    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()
    
    def __str__(self):
        return self.blog_title


class Comment(models.Model):


    #NOTE refer to  the related_name='comments' in the serializers
    blog = models.ForeignKey('Blog', related_name='comments', on_delete=models.CASCADE) #the CASCADE means on delet of a particular blook ID, all the comments under that particluar blog id should also delete  
    comment = models.TextField()  

    def __str__(self):
        return self.comment