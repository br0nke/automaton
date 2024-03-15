from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext as _
from PIL import Image
import os


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), verbose_name=_("user"), on_delete=models.CASCADE)
    picture = models.ImageField(_("picture"), upload_to='user_profile/', blank=True, null=True)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("user_detail_current", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if self.picture and os.path.exists(self.picture.path):
            image = Image.open(self.picture.path)
            if image.size[0] > 300 or image.size[1] > 300:
                image.resize((300, 300))
                image.save(self.picture.path)