from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(
            2, "Title must be greater than 2 characters")]
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    comments = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name='comments_owned', through='Comment')
    picture = models.BinaryField(null=True, blank=True, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(validators=[MinLengthValidator(
        3, 'Comment must be greater than 3 characters')])
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text if len(self.text)<15 else self.text[:10]+' ...'

    