from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import FileSizeValidator


# Create your models here.


class Photo(models.Model):
    photo = models.ImageField(
        upload_to='images',
        validators=(
            FileSizeValidator(5),
        ),
    )

    description = models.TextField(
        max_length=300,
        validators=(
            MinLengthValidator(10),
        ),
        blank=True,
        null=True,
    )

    location = models.TextField(
        max_length=30,
        blank=True,
        null=True,
    )

    tagged_pet = (
        models.ManyToManyField(
            Pet,
            blank=True,
        )
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return self.description
