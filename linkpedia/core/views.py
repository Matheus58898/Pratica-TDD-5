from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import LinkModel
from core.forms import LinkModelForm

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar')
        else:
            error = 'Usuário ou senha inválidos.'
    return render(request, 'login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def listar(request):
    links = LinkModel.objects.all()
    return render(request, 'linkpedia/list.html', {'links': links})

@login_required
def cadastrar(request):
    form = LinkModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'linkpedia/form.html', {'form': form})

@login_required
def atualizar(request, pk):
    link = get_object_or_404(LinkModel, pk=pk)
    form = LinkModelForm(request.POST or None, instance=link)
    if form.is_valid():
        form.save()
        return redirect('listar')
    return render(request, 'linkpedia/form.html', {'form': form})

@login_required
def remover(request, pk):
    link = get_object_or_404(LinkModel, pk=pk)
    if request.method == 'POST':
        link.delete()
        return redirect('listar')
    return render(request, 'linkpedia/form.html', {'form': None, 'objeto': link})