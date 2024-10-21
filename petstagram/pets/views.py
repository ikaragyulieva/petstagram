from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


# Create your views here.

# CBV Add View
class AddPetView(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-add-page.html'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})


# FBV Add View
def add_pet(request):
    form = PetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)
    else:
        context = {
            'form': form,
        }

    return render(request, template_name='pets/pet-add-page.html', context=context)


# CBV Detail View
class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pets/pet-details-page.html'
    context_object_name = 'pet'
    slug_url_kwarg = 'pet_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_photos'] = self.object.photo_set.all()
        context['comment_form'] = CommentForm()
        return context


# FBV Detail View
def pet_details(request, username: str, pet_slug: str):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()
    context = {
        'pet': pet,
        'all_photos': all_photos,
        'comment_form': comment_form,
    }

    return render(request, template_name='pets/pet-details-page.html', context=context)


# CBV Edit View
class EditPetView(UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet-edit-page.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_success_url(self):
        return reverse_lazy(
            'pet-details',
            kwargs={
                'username': self.kwargs['username'],
                'pet_slug': self.kwargs['pet_slug']
            }
        )


# FBV Edit View
def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)

    context = {
        'form': form,
    }
    return render(request, template_name='pets/pet-edit-page.html', context=context)


# CBV Edit View
class DeletePetView(DeleteView):
    model = Pet
    template_name = 'pets/pet-delete-page.html'
    context_object_name = 'pet'
    success_url = reverse_lazy('profile-details', kwargs={'pk': 1})

    def get_object(self, queryset=None):
        return Pet.objects.get(slug=self.kwargs['pet_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PetDeleteForm(initial=self.object.__dict__)
        return context

    def delete(self, request, *args, **kwargs):
        pet = self.get_object()
        pet.delete()
        return redirect(self.success_url)


# FBV Delete View
def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)

    form = PetDeleteForm(instance=pet, initial=pet.__dict__)
    context = {
        'form': form,
    }

    return render(request, template_name='pets/pet-delete-page.html', context=context)
