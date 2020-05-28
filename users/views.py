from django.shortcuts import render

# Create your views here.
def perfil_view(request):
    return render(request, 'users/perfil.html')
def registro_view(request):
    return render(request, 'users/registro.html')
def login_view(request):
    return render(request, 'users/inicio_sesion.html')

