from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify





class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.PUBLISH)

class News(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'DRAFT'
        PUBLISH = 'PB', 'PUBLISH'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)



    objects = models.Manager()
    published = PublishManager()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return  self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[self.slug])

class Contact(models.Model):

    user = models.CharField(max_length=150)
    email = models.EmailField()
    msg = models.TextField()

    def __str__(self):
        return self.user