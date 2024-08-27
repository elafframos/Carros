from django.shortcuts import render, redirect
from .models import Car
from .form import formulario


def cars_view(request):
    car = Car.objects.all()
    search = request.GET.get('search')

    if search:
        car = Car.objects.filter(model__contains= search)
    return render(request, 'cars.html', {'car': car})

def form_view(request):
    if request.method == 'POST':
        form = formulario(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('cars_view')
    else:
        form = formulario()
    return render(request, 'cars_form.html', {'form': form})
