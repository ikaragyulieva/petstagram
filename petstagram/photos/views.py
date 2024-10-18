from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Like
from petstagram.photos.forms import PhotoCreationForm, PhotoEdirForm
from petstagram.photos.models import Photo


# Create your views here.


def add_photo(request):
    form = PhotoCreationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home-page')

    context = {
        'form': form,
    }

    return render(request, template_name='photos/photo-add-page.html', context=context)


def photo_details(request, pk: int):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentForm()

    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, template_name='photos/photo-details-page.html', context=context)


def edit_photo(request, pk: int):
    photo = Photo.objects.get(pk=pk)

    if request.method == 'POST':
        form = PhotoEdirForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo-details', pk)
    else:
        form = PhotoEdirForm(instance=photo, initial=photo.__dict__)

    context = {
        'form': form,
    }

    return render(request, template_name='photos/photo-edit-page.html', context=context)


def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home-page')

