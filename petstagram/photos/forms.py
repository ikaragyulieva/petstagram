from django import forms

from petstagram.photos.models import Photo


class PhotoCreationForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'


class PhotoEdirForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['photo']


# class PhotoDeleteForm(PhotoEdirForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for (_, field) in self.fields.items():
#             field.widget.attrs['disabled'] = 'disabled'
#             field.widget.attrs['readonly'] = 'readonly'
