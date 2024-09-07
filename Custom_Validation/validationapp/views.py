
from django.shortcuts import render
from .form import AnagramForm

def index(request):
    if request.method == 'POST':
        form = AnagramForm(request.POST)
        if form.is_valid():
            # Process  data if needed
            return render(request, 'myapps/index.html', {'form': form})
    else:
        form = AnagramForm()
    return render(request, 'myapps/index.html', {'form': form})