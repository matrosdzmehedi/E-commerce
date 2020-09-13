from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from .forms import UserupdateForm, ProfileUpdateForm


class ProfileView(TemplateView):
    model = User
    template_name = 'account/profile.html'
    context_object_name = 'user'




class Profiledit(TemplateView):
    model = User
    template_name = 'account/profile_edit.html'
    context_object_name = 'user'

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