from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login



# Create your views here.
def perfil_view(request):
    return render(request, 'users/Pagina_perfil.html')
    
def registro_view(request):
    return render(request, 'users/registro.html')
def login_view(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    return render(request, 'users/inicio_sesion.html')



  



