from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat


# Define the home view
def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


# class Cat:
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age


# cats = [
#     Cat('Lolo', 'tabby', 'foul little demon', 3),
#     Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#     Cat('Raven', 'black tripod', '3 legged cat', 4),
#     Cat('In Hat', 'siamese', 'hairless', 4)
# ]


def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', {'cats': cats})


def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', {'cat': cat})

# cuds crud
class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats/'
  
  
class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'