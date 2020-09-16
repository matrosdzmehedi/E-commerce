from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from .forms import UserupdateForm, ProfileUpdateForm
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy




class ProfileView(TemplateView,LoginRequiredMixin, UserPassesTestMixin):
    model = User
    template_name = 'account/profile.html'
    context_object_name = 'user'
    
    
    def get(self, request, *args, **kwargs):
        item = Product.objects.filter( user_id=request.user.id)
        return render(request, self.template_name,{'item':item})


   


class Profiledit(TemplateView,LoginRequiredMixin, UserPassesTestMixin):
    model = User
    template_name = 'account/profile_edit.html'
    context_object_name = 'user'


    def get(self, request, *args, **kwargs):
        u_form=UserupdateForm(instance=request.user)
        p_form=ProfileUpdateForm (instance=request.user.userprofile)
        return render(request, 'account/profile_edit.html', {'update': u_form, 'profileup': p_form})
    

    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            u_form = UserupdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,  request.FILES, instance=request.user.userprofile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
        else:
            u_form=UserupdateForm(instance=request.user)
            p_form=ProfileUpdateForm (instance=request.user.userprofile)
        return render(request, 'account/profile_edit.html', {'update': u_form, 'profileup': p_form})


class Item( CreateView,LoginRequiredMixin, UserPassesTestMixin):
    model = Product
    template_name = 'mainsite/item.html'
    fields = ('item_name','catagory','price','descrip','status','item_image')
    login_url = 'login'

    def form_valid(self, form):  # new
        form.instance.user = self.request.user
        return super().form_valid(form)

class ItemDetailView(DetailView):
    model = Product
    template_name = 'mainsite/item_detail.html'



class ItemUpdateView(UpdateView):
    model = Product
    template_name = 'mainsite/item_edit.html'
    fields = ['item_name','catagory','price','descrip','status']


class ItemDeleteView(DeleteView):
    model = Product
    template_name = 'mainsite/item_delete.html'
    success_url = reverse_lazy('profile')



class ItemDetailUserView(DetailView):
    model = Product
    template_name = 'mainsite/item_detail_user.html'
