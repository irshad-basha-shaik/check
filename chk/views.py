from django.shortcuts import render

from .models import Empower
from .forms import EmpowerForm


def index(request):
    list = Empower.objects.all()
    return render(request, 'list.html',{"list":list})

def new(request):
    context = {}
    context['form'] = EmpowerForm()
    if request.method == 'POST':
        form = EmpowerForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return index(request)
        else:
            print("---error---start---")
            print(request.POST)
            print(form.errors)
            print("---error---end---")

    return render(request, "index.html", context)