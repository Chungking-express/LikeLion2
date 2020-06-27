from django.shortcuts import render,get_object_or_404, redirect
from .models import upload
from .forms import createForm



def home(request):
    uploads = upload.objects
    return render(request, 'home.html', {"uploads":uploads})

def create(request):
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = createForm()
    return render(request, 'create.html', {'form':form})

def update(request, update_id):
    updates = get_object_or_404 (upload, pk=update_id)
    if request.method == 'POST':
        form = createForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse ('home', args=(update_id)))
    else:
        form = createForm()
    return render(request, 'update.html',{'updates':updates})
