from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from PIL import Image

CATEGORIES = (
    ('HTML', 'Html'),
    ('PYTHON', 'Python'),
    ('CSS', 'Css'),
    ('JS', 'Js'),
    ('DJANGO', 'Django'),
)


class CodeListing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        verbose_name=_("user"), 
        related_name='listings',
    )
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='code_listings/', blank=False, null=True)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    link = models.URLField(blank=False)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = _("listing")
        verbose_name_plural = _("listings")
        ordering = ['title', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("codes_detail", kwargs={"pk": self.pk})
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)