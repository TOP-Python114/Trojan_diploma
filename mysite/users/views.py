from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.shortcuts import redirect
from .forms import CustomUserCreationForm



class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('/auth/login/')


class UserRegistrationView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = '/auth/login/'

    def form_valid(self, form: CustomUserCreationForm):
        form.save()
        return redirect(self.get_success_url())


