from django import forms
from ads.models import Ad, Comment
from ads.humanize import naturalsize
from django.core.files.uploadedfile import InMemoryUploadedFile


class AdForm(forms.ModelForm):
    max_upload_limit = 2*1024*1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    picture = forms.FileField(
        required=False, label='File to upload <='+max_upload_limit_text)
    upload_field_name = 'picture'

    class Meta:
        model = Ad
        fields = ("title", "price", "text", "picture","tags")

    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', 'file must be < ' +
                           self.max_upload_limit_text)

    def save(self, commit=True):
        instance = super(AdForm, self).save(commit=False)
        f = instance.picture
        if isinstance(f, InMemoryUploadedFile):
            bytearray = f.read()
            instance.picture = bytearray
        if commit:
            instance.save()
            self.save_m2m()

        return instance


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['text']


class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)