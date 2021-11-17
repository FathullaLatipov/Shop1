from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView

from pages.forms import ContactModelForm
from products.models import ProductModel, CategoryModel, CategoryHomeModel


class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    extra_context = {'title': 'Contact'}

    def get_success_url(self):
        return reverse('contact:contact')


class HomeView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Home'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.objects.order_by('-pk')[:8]
        context['cats'] = CategoryModel.objects.order_by('-pk')[:1]

        return context


class AboutView(TemplateView):
    template_name = 'blog.html'
    extra_context = {'title': 'About'}


class LoginView(TemplateView):
    template_name = 'login.html'
    extra_context = {'title': 'Login'}


class RegisterView(TemplateView):
    template_name = 'registration_form.html'
    extra_context = {'title': 'Login'}


def registration_done(request):
    messages.add_message(request, messages.INFO, 'Success')
    return redirect(reverse('contact:register'))
