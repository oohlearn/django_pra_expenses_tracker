from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data["username"],
                                password=data["password"])
            if user is not None:
                login(request, user)
                return redirect("/")
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('/users/login')
    
# class UserLogoutView(LogoutView):

#     def get(self, request):
#         logout(request)
#         # return render(request, "registration/logout.html")
#         return redirect('login')
