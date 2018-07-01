from django.shortcuts import render
from .forms import MemberForm
from django.shortcuts import redirect

# Create your views here.
def main(request):
    return render(request, 'wise_saying/main.html', {})

def login(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = MemberForm()
    return render(request, 'wise_saying/register.html', {'form': form})

def register(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
            
    form = MemberForm()
    return render(request, 'wise_saying/register.html', {'form': form})


def home(request):
    return render(request, 'wise_saying/home.html', {})

