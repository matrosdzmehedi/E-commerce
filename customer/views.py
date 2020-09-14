from django.shortcuts import render
from seller.models import Product
from django.views.generic import TemplateView,ListView


class Home(ListView):
    model=Product
    template_name='mainsite/home.html'
    #paginate_by = 20


    

   