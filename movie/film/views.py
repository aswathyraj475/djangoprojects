from django.shortcuts import render
from film.models import Film
def home(request):
        k = Film.objects.all()
        return render(request, 'home.html', {'b': k})

def add(request):
    if (request.method == "POST"):
        n = request.POST['n']
        d = request.POST['d']
        c = request.FILES['c']
        b = Film.objects.create(name=n, desc=d,cover=c)
        b.save()
        return home(request)
    return render(request,'add.html')

def view_cinema(request,p):
    b=Film.objects.get(id=p)
    return render(request,'view.html',{'b':b})


