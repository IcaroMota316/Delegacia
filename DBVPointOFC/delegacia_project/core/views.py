from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Policial, Ocorrencia, Vitima, Suspeito, Evidencia
from .forms import PolicialForm, OcorrenciaForm, VitimaForm, SuspeitoForm, EvidenciaForm

# ================= POLICIAL =================

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def listar_policiais(request):
    policiais = Policial.objects.all()
    paginator = Paginator(policiais, 5)
    page = request.GET.get('page')
    policiais = paginator.get_page(page)
    return render(request, 'core/policial_list.html', {'policiais': policiais})

@login_required
def criar_policial(request):
    form = PolicialForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_policiais')
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Novo Policial'})

@login_required
def editar_policial(request, id):
    policial = get_object_or_404(Policial, id=id)
    form = PolicialForm(request.POST or None, instance=policial)
    if form.is_valid():
        form.save()
        return redirect('listar_policiais')
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Editar Policial'})

@login_required
def excluir_policial(request, id):
    policial = get_object_or_404(Policial, id=id)
    if request.method == 'POST':
        policial.delete()
        return redirect('listar_policiais')
    return render(request, 'core/confirm_delete.html', {'obj': policial})

# ================= OCORRÊNCIA =================
@login_required
def listar_ocorrencias(request):
    ocorrencias = Ocorrencia.objects.all()
    paginator = Paginator(ocorrencias, 5)
    page = request.GET.get('page')
    ocorrencias = paginator.get_page(page)
    return render(request, 'core/ocorrencia_list.html', {'ocorrencias': ocorrencias})

@login_required
def criar(request):
    form = OcorrenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_ocorrencias')
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Nova Ocorrência'})

@login_required
def editar_ocorrencia(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, id=id)
    form = OcorrenciaForm(request.POST or None, instance=ocorrencia)
    if form.is_valid():
        form.save()
        return redirect('listar_ocorrencias')
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Editar Ocorrência'})

@login_required
def excluir_ocorrencia(request, id):
    ocorrencia = get_object_or_404(Ocorrencia, id=id)
    if request.method == 'POST':
        ocorrencia.delete()
        return redirect('listar_ocorrencias')
    return render(request, 'core/confirm_delete.html', {'obj': ocorrencia})

# ================= VÍTIMA =================
@login_required
def listar_vitimas(request):
    vitimas = Vitima.objects.all()
    paginator = Paginator(vitimas, 5)
    page = request.GET.get('page')
    vitimas = paginator.get_page(page)
    return render(request, 'core/vitima_list.html', {'vitimas': vitimas})

@login_required
def criar_vitima(request):
    form = VitimaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_vitimas')
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Nova Vítima'})

@login_required
def editar_vitima(request, id):
    vitima = get_object_or_404(Vitima, id=id)
    form = VitimaForm(request.POST or None, instance=vitima)
    if form.is_valid():
        form.save()
        return redirect('listar_vitimas')
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Editar Vítima'})

@login_required
def excluir_vitima(request, id):
    vitima = get_object_or_404(Vitima, id=id)
    if request.method == 'POST':
        vitima.delete()
        return redirect('listar_vitimas')
    return render(request, 'core/confirm_delete.html', {'obj': vitima})


# ================= SUSPEITO =================
@login_required
def listar_suspeitos(request):
    suspeitos = Suspeito.objects.all()
    paginator = Paginator(suspeitos, 5)
    page = request.GET.get('page')
    suspeitos = paginator.get_page(page)
    return render(request, 'core/suspeito_list.html', {'suspeitos': suspeitos})

@login_required
def criar_suspeito(request):
    form = SuspeitoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_suspeitos')
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Novo Suspeito'})

@login_required
def editar_suspeito(request, id):
    suspeito = get_object_or_404(Suspeito, id=id)
    form = SuspeitoForm(request.POST or None, instance=suspeito)
    if form.is_valid():
        form.save()
        return redirect('listar_suspeitos')
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Editar Suspeito'})

@login_required
def excluir_suspeito(request, id):
    suspeito = get_object_or_404(Suspeito, id=id)
    if request.method == 'POST':
        suspeito.delete()
        return redirect('listar_suspeitos')
    return render(request, 'core/confirm_delete.html', {'obj': suspeito})


# ================= EVIDÊNCIA =================
@login_required
def listar_evidencias(request):
    evidencias = Evidencia.objects.all()
    paginator = Paginator(evidencias, 5)
    page = request.GET.get('page')
    evidencias = paginator.get_page(page)
    return render(request, 'core/evidencia_list.html', {'evidencias': evidencias})

@login_required
def criar_evidencia(request):
    form = EvidenciaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_evidencias')
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Nova Evidência'})

@login_required
def editar_evidencia(request, id):
    evidencia = get_object_or_404(Evidencia, id=id)
    form = EvidenciaForm(request.POST or None, request.FILES or None, instance=evidencia)
    if form.is_valid():
        form.save()
        return redirect('listar_evidencias')
    return render(request, 'core/form.html', {'form': form, 'titulo': 'Editar Evidência'})

@login_required
def excluir_evidencia(request, id):
    evidencia = get_object_or_404(Evidencia, id=id)
    if request.method == 'POST':
        evidencia.delete()
        return redirect('listar_evidencias')
    return render(request, 'core/confirm_delete.html', {'obj': evidencia})

