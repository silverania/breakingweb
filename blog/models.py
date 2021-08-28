from django.db import models
from django.utils import timezone

# from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from user.models import Profile
from django.utils.timezone import now

# Create your models here.


class PersonManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=author)


class Site(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def save(self, *args, **kwargs):
        today = date.today()
        self.slug = self.title + "_" + str(today)
        super(Site, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


class Comment(models.Model):
    STATUS_CHOICES = (
        ("rigettato", "Rigettato"),
        ("publicato", "Publicato"),
    )
    site = models.ForeignKey(
        Site,
        related_name="all_comments",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=40)
    slug = models.SlugField(
        max_length=250, unique_for_date="publish", blank=True, null=True
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="blog_posts",
        null=True,
        blank=True,
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    postType = models.CharField(max_length=10, default="post")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="bozza")

    def get_absolute_url(self):
        return reverse(
            "blog:newPost",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )

    objects = PersonManager()

    class Meta:
        unique_together = [["author", "created"]]

    def __str__(self):
        return self.title


class Resp(models.Model):
    STATUS_CHOICES = (
        ("rigettato", "Rigettato"),
        ("publicato", "Publicato"),
    )
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="resps")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    # post=models.CharField(max_length=250,default="post anonimo")
    commento = models.ForeignKey(
        Comment,
        related_name="risposte",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    postType = models.CharField(max_length=10, default="resp")

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.body
