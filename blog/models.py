from django.db import models
from django.utils import timezone
from user.models import Profile
from django.utils.text import slugify

# Create your models here.


class PersonManager(models.Manager):
    def get_by_natural_key(self, first_name, last_name):
        return self.get(first_name=author)


class Site(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    # def save(self, *args, **kwargs):
    #    super(Site, self).save(*args, **kwargs)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                             related_name="sites", null=True, blank=True)
    titleTagContent = models.CharField(
        max_length=200, default="empty")

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS_CHOICES = (
        ("rigettato", "Rigettato"),
        ("publicato", "Publicato"),
    )
    site = models.ForeignKey(
        Site,
        related_name="all_comments",
        on_delete=models.PROTECT
    )
    title = models.CharField(
        max_length=100, default="...", null=True, blank=True)
    slug = models.SlugField(
        max_length=250, blank=True, null=True
    )
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name="blog_posts",
        null=True,
        blank=True,
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    postType = models.CharField(max_length=10, default="post")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="bozza")
    tagTitleInPage = models.CharField(max_length=100, default="tag_value")
    """
    def get_absolute_url(self):
        return reverse(
            "blog:newPost",
            args=[self.publish.year, self.publish.month,
                  self.publish.day, self.slug],
        )
    """

    def __str__(self):
        return str(self.tagTitleInPage)

    objects = PersonManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.site)+str(self.publish))
        super(Comment, self).save(*args, **kwargs)

    class Meta:
        unique_together = [["author", "created"]]


class Resp(models.Model):
    STATUS_CHOICES = (
        ("rigettato", "Rigettato"),
        ("publicato", "Publicato"),
    )
    MESS_TYPE = (
        ("respToPost", "respToPost"),
        ("respToResp", "respToResp"),
    )
    author = models.ForeignKey(
            Profile, on_delete=models.CASCADE, related_name="resps")
    respToUser = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="userResps")
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
    resps = models.ManyToManyField("Resp", blank=True)
    idRespTo = models.CharField(max_length=50, default="0_0")
    postType = models.CharField(
            max_length=10, default="respToPost", choices=MESS_TYPE)
    site = models.ForeignKey(
        Site,
        related_name="all_resps",
        on_delete=models.PROTECT
    )

    class Meta:
        ordering = ("publish",)

    def __str__(self):
        return '{} - {} ({})'.format('id:'+str(self.pk), ':'+str(self.idRespTo), 'tipo:'+str(self.postType))
