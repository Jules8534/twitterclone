from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser

# Create your models here.
class TwitterUser(AbstractUser):
    display_name = models.CharField(max_length=150, null=True, blank=True)
    # REQUIRED_FIELDS = ["display_name"]
    homepage = models.URLField(max_length=150, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, unique=True)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)
