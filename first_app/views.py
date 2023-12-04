from django.shortcuts import render
from . form import ExampleForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
            form = ExampleForm(request.POST)

    return render(request, 'home.html', {'form': form})