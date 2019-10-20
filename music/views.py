from django.views import generic
from music.forms import UserForm
from .models import Album, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


#generic views

class IndexView(generic.ListView):
    #specify what template we are using
    template_name = 'music/index.html' # plugging list of albums into this album
    context_object_name = 'all_albums'  #default name is object_list

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album # looking at the details of an album
    template_name = 'music/detail.html' # plugging album into this template

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class SongDelete(DeleteView):
    model = Song
    def get_success_url(self):
        return reverse_lazy('music:detail', kwargs={'pk': self.object.album_id})

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html' #html file forms gonna be included in

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False) # doesnt save user inputs yet

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form':form})

