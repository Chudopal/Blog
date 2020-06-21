from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """The model of post
    name -- name of the post,
    body -- content of the post,
    author -- the user, who wrote the post,
    comments -- other users can comment this post
    like -- number of likes
    date -- the date of creating the post
    """
    name = models.CharField(
        max_length=100,
        help_text="Enter the name of your post"
    )
    body = midels.TextField(
        max_length=2000,
        help_text="Enter the content of your post"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    comments = models.ManyToManyField(
        Comment,
        blank=True
    )
    likes = models.IntegerField()
    date = models.DataField(auto_now=True)

    class Meta():
        ordering = ["date"]

    def __str__(self):
        return self.name

    
class Comment(models.Model):
    """The model for comment
    body -- the content of the comment
    author -- the user, who wrote the comment,
    date -- the date of creating the comment
    """
    body = midels.TextField(
        max_length=500,
        help_text="Enter the content of your comment"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL
    )
    date = models.DateField(
        auto_now=True
    )
    class Meta():
        ordering = ["date"]

    def __str__(self):
        return self.body    
