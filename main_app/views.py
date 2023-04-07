from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse


# Add the Cat class & list and view function below the imports
class Puppy:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, gender, description, age):
    self.name = name
    self.breed = breed
    self.gender = gender
    self.description = description
    self.age = age
    

puppies = [
  Puppy('Penny', 'poodle','girl', 'cuddly puppy', 2),
  Puppy('Leo', 'siberian husky','boy', 'playful', 0),
  Puppy('Blue', 'akita','girl', '3 legged puppy', 3)
]












# Add new view
def puppies_index(request):
  return render(request, 'puppies/index.html', { 'puppies': puppies })





# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    #django is configured to know automatically
    #to look inside of a templates folder for the html files
    return render(request, 'about.html')
