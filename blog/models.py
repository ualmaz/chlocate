from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(_("city"), max_length=64, default="Zanesville")
    zip_code = models.CharField(_("postal code"), max_length=15)
    address = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
