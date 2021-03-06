from django.contrib.auth.mixins import LoginRequiredMixin #New
from django.http import request
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView

from .forms import VehicleCreateForm, VehicleEditForm
from .models import models
from .models import Client,Vehicle,Comment
from django.urls import reverse_lazy, reverse, resolve

class ClientListView(LoginRequiredMixin,ListView):
    model = Client
    template_name = 'client_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Super users can see all clients
        if self.request.user.is_superuser:
            print("entered superusercase")
            context['object_list'] = Client.objects.all()
        else:
            # Filtering the object list by the current user
            print("entered non superusercase")
            context['object_list'] = Client.objects.filter(author=self.request.user)
        return context

class ClientDetailView(LoginRequiredMixin,DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'

class ClientUpdateView(LoginRequiredMixin,UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'

class ClientDeleteView(LoginRequiredMixin,DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')

class ClientCreateView(LoginRequiredMixin,CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    #fields = ('make', 'model', 'vinnumber', 'dateofpurchase', 'dateoflastservice', 'color', 'capacity', 'description')
    template_name = 'vehicle_edit.html'

    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['clientPk'],))

    def get_form(self, form_class=VehicleEditForm):
        form = super(VehicleUpdateView, self).get_form(form_class)
        form.fields['make'].label = "Make"
        form.fields['model'].label = "Model"
        form.fields['vinnumber'].label = "VIN Number"
        form.fields['dateofpurchase'].label = "Date of Purchase"
        form.fields['dateoflastservice'].label = "Date of Last Service"
        return form


class VehicleDeleteView(LoginRequiredMixin,DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    #success_url = reverse_lazy('client_list')
    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['clientPk'],))


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    #fields = ('make', 'model', 'vinnumber', 'dateofpurchase', 'dateoflastservice', 'color', 'capacity', 'description')
    login_url = 'login'

    def get_form(self, form_class=VehicleCreateForm):
        form = super(VehicleCreateView, self).get_form(form_class)
        form.fields['make'].label = "Make"
        form.fields['model'].label = "Model"
        form.fields['vinnumber'].label = "VIN Number"
        form.fields['dateofpurchase'].label = "Date of Purchase"
        form.fields['dateoflastservice'].label = "Date of Last Service"
        return form

    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['pk'],))

    def form_valid(self, form):
        form.instance.client = get_object_or_404(Client, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('comment',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.client = get_object_or_404(Client, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['pk'],))


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ('comment',)
    template_name = 'comment_edit.html'

    def form_valid(self, form):
        form.instance.client = get_object_or_404(Client, pk=self.kwargs['clientPk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['clientPk'],))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['clientPk'],))
