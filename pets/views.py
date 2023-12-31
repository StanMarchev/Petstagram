from django.shortcuts import render, redirect

from petstagram.pets.forms import PetAddForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.
def pet_add(request):
    if request.method == 'GET':
        form = PetAddForm()
    else:
        form = PetAddForm(request.POST)
    context = {
        "form": form,
    }

    return render(request, 'pets/pet-add-page.html', context=context)


def pet_details(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    all_photos = pet.photo_set.all()
    context = {
        "pet": pet,
        "all_photos": all_photos
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetAddForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetAddForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('profile details', username , pet_slug)

    context = {
        'form': form,
    }

    return render(request, template_name='pets/pet-edit-page.html', context=context)


def pet_delete(request, username, pet_slug):
    pet =Pet.objects.all(slug=pet_slug)
    if request.method =='POST':
        pet.delete()
        return redirect('profile details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {
        'form': form,
    }
    return render(request, template_name='pets/pet-delete-page.html', context=context)
