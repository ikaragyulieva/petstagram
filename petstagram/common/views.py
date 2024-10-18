from django.shortcuts import render, redirect, resolve_url


from petstagram.common.forms import CommentForm
from petstagram.common.models import Like, Comment
from petstagram.photos.models import Photo

from pyperclip import copy


def home(request):
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    context = {
        'all_photos': all_photos,
        'comment_form': comment_form,
    }

    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, photo_id: int):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def copy_link_to_clipboard_functionality(request, photo_id: int):
    copy(request.META['HTTP_HOST'] + resolve_url('photo-details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')


def add_comment(request, photo_id):
    if request.method == 'POST':
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')

