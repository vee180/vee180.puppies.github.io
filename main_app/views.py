from django.shortcuts import render, redirect 

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.
# Add the following import
from django.http import HttpResponse

from .models import Puppy, Toy

from .forms import FeedingForm

class PuppyCreate(CreateView):
  model = Puppy
  fields = '__all__'

class PuppyUpdate(UpdateView):
  model = Puppy
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class PuppyDelete(DeleteView):
  model = Puppy
  success_url = '/puppies/'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'




def assoc_toy(request, puppy_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Puppy.objects.get(id=puppy_id).toys.add(toy_id)
  return redirect('detail', puppy_id=puppy_id)





def puppies_index(request):
    # key 'puppies' will be the variable name in the puppies/index.html
    # puppies will be the array that we are storing in the puppies variable

    puppies = Puppy.objects.all()  # finding all the cats from the database!
    return render(request, 'puppies/index.html', {'puppies': puppies})


def puppies_detail(request, puppy_id):
  puppy = Puppy.objects.get(id=puppy_id)
  # instantiate FeedingForm to be rendered in the template
  toys_puppy_doesnt_have = Toy.objects.exclude(id__in = puppy.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'puppies/detail.html', {
    'puppy': puppy, 'feeding_form': feeding_form,
    # Add the toys to be displayed
    'toys': toys_puppy_doesnt_have
  })

def add_feeding(request, puppy_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the puppy_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.puppy_id = puppy_id
    new_feeding.save()
  return redirect('detail', puppy_id=puppy_id)





# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    # django is configured to know automatically
    # to look inside of a templates folder for the html files
    return render(request, 'about.html')
