from django.shortcuts import render

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


# Create your views here.

def add_pet(request):
    return render(request, template_name='pets/pet-add-page.html')


def pet_details(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }

    return render(request, template_name='pets/pet-details-page.html', context=context)


def edit_pet(request):
    return render(request, template_name='pets/pet-edit-page.html')


def delete_pet(request):
    return render(request, template_name='pets/pet-delete-page.html')
