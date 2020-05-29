"""Users views."""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Perfil

# Forms
from users.forms import ProfileForm

from posts.models import Post



# Create your views here.

    
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
            url= reverse('perfil', kwargs={'username':request.user.username})
            return redirect(url)

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


      
class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/perfil.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-create')
        return context


    

  



