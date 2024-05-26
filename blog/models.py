from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinLengthValidator

contentValidator=MinLengthValidator(limit=300,message="content should have a limit of 300")

class Blog(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=300)
    content=models.TextField(validators=[contentValidator])
    date_published=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={'pk': self.pk})