from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
from .models import User
from user.models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
#custom modelmanager classe per visualizzare tutorial  in admin


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset().filter(status='pubblicato')

#custo modelmanager classe per visualizzare tutorial bozza in admin


class BozzaManager(models.Manager):
    def get_queryset(self):
        return super(BozzaManager,
                     self).get_queryset().filter(status='bozza')


class Category(models.Model):
    CATEGORY = (
        ('linux', 'Linux'),
        ('web', 'Web'),
        ('django', 'Django'),
        ('generica', 'Generica'),
        ('download', 'Download')
    )
    linux = 'Linux'
    web = 'Web'
    django = 'Django'
    generica = 'Generica'
    download = "Download"
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50,
                                choices=CATEGORY,
                                default=generica)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "%s" % (self.title)


class Tutorial(models.Model):
    STATUS_CHOICES = (
        ('bozza', 'Bozza'),
        ('pubblicato', 'Pubblicato'),)
    #post=models.ForeignKey(Comment,related_name='comments',on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=250)
    overview = models.TextField(default="tutorial")
    slug = models.SlugField(max_length=250, null=True, blank=True)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="tutorials")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='bozza')
    visite = models.PositiveIntegerField(default=1)
    photos = models.ImageField(upload_to='media/tuorial/images/', blank=True, null=True)
#post=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="comments",null=True,blank=True)
    # decommentare una delle seguenti tre righe per selezionare un custom model manager
    #objects = models.Manager() # The default manager.
    #bozza=BozzaManager() # Our bozza solo manager
    #published = PublishedManager() # Our publicato custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return "%s" % (self.title)+", letto "+str(self.visite)+" volte"

    def get_absolute_url(self):
        return reverse('homepage:tutorial_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


@receiver(post_save, sender=Tutorial)
def update_tutorial(sender, instance, **kwargs):
    instance.slug = instance.title.replace(" ", "_").lower()
    print(str(instance.slug))
    post_save.disconnect(update_tutorial, sender=Tutorial)
    instance.save(update_fields=['slug'])
    post_save.connect(update_tutorial, sender=Tutorial)

# la classe category definisce le categorie in cui sarannno inseriti i singoli tutorials
# ad esempio sara creata la categoria linux, web , ecc..
