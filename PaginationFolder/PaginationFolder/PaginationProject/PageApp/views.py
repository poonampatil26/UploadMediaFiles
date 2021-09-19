from django.shortcuts import render, redirect
from .models import Mobile
from .forms import MobileForm

# Create your views here.

def add_mobile(request):
    form = MobileForm()
    if request.method == 'POST':
        form = MobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # image.save()
            return redirect('show')
    template_name = 'PageApp/add_mobile.html'
    context = {'form':form}
    return render(request, template_name, context)

def update_mobile(request,id):
    order = Mobile.objects.get(id=id)
    form = MobileForm(instance=order)
    if request.method == 'POST':
        form = MobileForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'PageApp/add_mobile.html'
    context = {'form':form}
    return render(request, template_name, context)

def delete_mobile(request, id):
    order = Mobile.objects.get(id=id)
    order.delete()
    return redirect('show')

def show_mobile(request):
    record = Mobile.objects.all()
    return render(request, 'PageApp/show.html', {'record':record})

def home(request):
    return render(request, 'PageApp/home.html', {})
