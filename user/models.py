from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #post=models.ForeignKey('blog.Comment',related_name="commenti",blank=True,null=True,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(default="media/images/user-secret-solid.svg')",
                              upload_to='users/%Y/%m/%d/', blank=True, null=True)
    first_name = models.CharField(max_length=100, default="anonimo")
    last_name = models.CharField(max_length=100, blank=True, null=True)
    #profile_reg_to_application = models.CharField(max_length=100)

    class Meta:
        unique_together = [['first_name', 'last_name']]

    def __str__(self):
        return f' {self.user.username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
