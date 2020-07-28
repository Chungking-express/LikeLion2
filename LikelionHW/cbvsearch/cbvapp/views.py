from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import cbv

class index(ListView):
    template_name = 'index.html'
    context_object_name = 'cbv_list'
    def get_queryset(self):
        return cbv.objects.all

class detail(DetailView):
    model = cbv
    template_name = 'detail.html'
    context_object_name = 'cbv'

class delete(DetailView):
    model = cbv
    template_name = 'delete.html'
    context_object_name = 'cbv'
    success_url = reverse_lazy('index')

class update(UpdateView):
    model = cbv
    template_name = 'update.html'
    fields = ['title','text']
    success_url = reverse_lazy('index')

class create(CreateView):
    model = cbv
    template_name = 'create.html'
    fields = ['title','text']
    def form_valid(self,form):
        cbv = form.save(commit=False)
        cbv.author = self.request.user
        cbv.save()

        return HttpResponseRedirect(self.request.POST.get('next','/'))
