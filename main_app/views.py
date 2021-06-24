from django.shortcuts import render
from . models import Cat, CatToy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

#create your views here

def about(request):
    #3rd param with data will be added
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def cats_index(request):
    cats = Cat.objects.all()
    data = {
        'cats': cats 
    }
    return render(request, 'cats/index.html', data)

def cats_show(request, cat_id):
    #cat data 
    cat = Cat.objects.get(id=cat_id)
    data = {'cat': cat}
    return render(request, 'cats/show.html', data)

def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})

class CatCreate(CreateView):
    model = Cat
    # Update the line below - add 'cattoys'
    fields = ['name', 'breed', 'description', 'age', 'cattoys']

class CatUpdate(UpdateView):
    model = Cat
    # Update the line below - add 'cattoys'
    fields = ['name', 'breed', 'description', 'age', 'cattoys']
    
class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'

def cattoys_index(request):
    cattoys = CatToy.objects.all()
    return render(request, 'cattoys/index.html', {'cattoys': cattoys})

def cattoys_show(request, cattoy_id):
    cattoy = CatToy.objects.get(id=cattoy_id)
    return render(request, 'cattoys/show.html', {'cattoy': cattoy})

class CatToyCreate(CreateView):
    model = CatToy
    fields = '__all__'
    success_url = '/cattoys'

class CatToyUpdate(UpdateView):
    model = CatToy
    fields = ['name', 'color']
    success_url = '/cattoys'

class CatToyDelete(DeleteView):
    model = CatToy
    success_url = '/cattoys'