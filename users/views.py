"""Users views."""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Perfil

# Forms
from users.forms import ProfileForm



# Create your views here.
def perfil_view(request):
    context={
       'user': user ,
        'website': website,
        'biography': biography,
        'number': phone_number,
        'picture': 'picture',
        'time':create,
    }
    return render(request, 'users/perfil.html')
    
def registro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/registro.html', {'error': 'No coinciden la contraseña y su confirmación'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/registro.html', {'error': 'El nombre de usuario no esta disponible'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        perfil = Perfil(user=user)
        perfil.save()

        return redirect('login')
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
            return render(request, 'users/inicio_sesion.html', {'error': 'La contraseña o el usuario no son validos'})
    
    return render(request, 'users/inicio_sesion.html')

def logout_view(request):
    logout(request)
    return redirect('login')
def update_profile(request):
    """Update a user's perfil view."""
    perfil = request.user.perfil

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            perfil.website = data['website']
            perfil.phone_number = data['phone_number']
            perfil.biography = data['biography']
            perfil.picture = data['picture']
            perfil.save()

            return redirect('feed')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'perfil': perfil,
            'user': request.user,
            'form': form
        }
    )

def editar_perfil(request):

    return render(request, 'users/cambiar_contrasena.html')



  



