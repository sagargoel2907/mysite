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
    favorites = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name='favorite_ads', through='Fav')
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
        return self.text if len(self.text) < 15 else self.text[:10]+' ...'


class Fav(models.Model):
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        unique_together=['ad','user']
    
    def __str__(self):
        return f'{self.user.username} likes {self.ad.title[:10]}'

    
