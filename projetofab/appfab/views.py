from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca, Veiculo
import requests

def home(request):
    return render(request, 'home.html') 

def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(request, "lista-marcas.html", {"marcas": marcas})

def cria_marca(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        pais = request.POST["pais_origem"]
        Marca.objects.create(nome=nome, pais_origem=pais)
        return redirect("lista_marcas")
    return render(request, "criar-marcas.html")

def atualiza_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        marca.nome = request.POST["nome"]
        marca.pais_origem = request.POST["pais_origem"]
        marca.save()
        return redirect("lista_marcas")
    return render(request, "criar-marcas.html", {"marca": marca})

def deleta_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        marca.delete()
        return redirect("lista_marcas")
    return render(request, "deletar-marca.html", {"marca": marca})

def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, "lista-veic.html", {"veiculos": veiculos})

def cria_veiculo(request):
    marcas = Marca.objects.all()
    if request.method == "POST":
        nome = request.POST["nome"]
        tipo = request.POST["tipo"]
        ano = request.POST["ano"]
        marca_pk = request.POST["marca"]
        marca = Marca.objects.get(pk=marca_pk)
        Veiculo.objects.create(nome=nome, tipo=tipo, ano=ano, marca=marca)
        return redirect("lista_veiculos")
    return render(request, "criar-veic.html", {"marcas": marcas})

def atualiza_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    marcas = Marca.objects.all()
    if request.method == "POST":
        veiculo.nome = request.POST["nome"]
        veiculo.tipo = request.POST["tipo"]
        veiculo.ano = request.POST["ano"]
        marca_pk = request.POST["marca"]
        veiculo.marca = Marca.objects.get(pk=marca_pk)
        veiculo.save()
        return redirect("lista_veiculos")
    return render(request, "criar-veic.html", {"veiculo": veiculo, "marcas": marcas})

def deleta_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == "POST":
        veiculo.delete()
        return redirect("lista_veiculos")
    return render(request, "deletar-veiculo.html", {"veiculo": veiculo})

def buscar_modelos(request):
    modelos = []
    marca = request.GET.get("marca")

    if marca:
        url = f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{marca}?format=json"
        response = requests.get(url)
        data = response.json()
        modelos = [m["Model_Name"] for m in data["Results"]]

    return render(request, "busc-model.html", {"modelos": modelos, "marca": marca})


