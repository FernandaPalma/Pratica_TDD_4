from django.shortcuts import render, redirect, get_object_or_404
from core.forms import LoginForm, AgendaForm
from core.models import Agenda
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# === AUTENTICAÇÃO ===

def login(request):
    if request.user.id is not None:
        return redirect("home")
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("home")
        context = {'acesso_negado': True}
        return render(request, 'core/login.html', {'form': form, 'acesso_negado': True})
    
    return render(request, 'core/login.html', {'form': LoginForm()})


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'core/logout.html')
    return redirect("home")


@login_required
def home(request):
    context = {}
    return render(request, 'core/index.html', context)


# === CRUD AGENDA ===

@login_required
def listar_contatos(request):
    contatos = Agenda.objects.all()
    return render(request, 'core/listar_contatos.html', {'contatos': contatos})


@login_required
def cadastrar_contato(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contatos')  
    else:
        form = AgendaForm()
    return render(request, 'core/cadastrar_contato.html', {'form': form})


@login_required
def atualizar_contato(request, contato_id):
    contato = get_object_or_404(Agenda, id=contato_id)
    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('listar_contatos') 
    else:
        form = AgendaForm(instance=contato)
    return render(request, 'core/atualizar_contato.html', {'form': form})


@login_required
def remover_contato(request, contato_id):
    contato = get_object_or_404(Agenda, id=contato_id)
    contato.delete()
    return redirect('listar_contatos') 
