from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:

            return HttpResponse('Ja existe esse usuario com esse username')

        user = User.objects.create_user(
            username=username, email=email, password=senha)
        user.save()
        mensagem = 'Usuário cadastrado com sucesso. <a href="/login">Ir para a tela de LOGIN</a>'
        return HttpResponse(mensagem)
    
def login(request):

    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)     
            messages.success(request, 'Login realizado com sucesso.')  
            return redirect('plataforma')
        else:
            messages.error(request, 'Email ou senha inválidos.')
            return render(request, 'login.html')



# pode ser usado dessa forma abaixo tb.
# @login_required(login_url="/auth/login/")
def plataforma(request):
    
        if request.user.is_authenticated:
          return render(request, 'plataforma.html')
        else:
            messages.error(request, 'Você precisa está logado.')
            return render(request, 'login.html')
  #  return render(request, 'plataforma.html')


def inicio(request):

    return render(request, 'inicio.html')


