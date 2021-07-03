from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


class ProfileView(generic.TemplateView):
    template_name = 'profile.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        return context



def signup_view(request):

    if request.method != "POST":
        form = UserCreationForm
    else:
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect(reverse('client:home'))
    
    context = {'form': form, 'title': "Sign up"}
    return render(request, 'signup.html', context)

