from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _ 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(("الأسم : "),max_length=50)
    who_i = models.TextField(("من انا : "), max_length=250)
    price = models.IntegerField(("سعر الكشف : "), max_length=5)
    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return self.name

   
