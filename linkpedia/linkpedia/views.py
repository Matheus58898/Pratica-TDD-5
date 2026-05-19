from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import LinkModel
from core.forms import LinkModelForm

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