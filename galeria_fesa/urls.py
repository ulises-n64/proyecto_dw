"""galeria_fesa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from galeria_fesa import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', posts_views.list_posts, name='home'),
    path('posts/', posts_views.list_posts, name='feed' ),
    path('perfil/', users_views.perfil_view, name='perfil'),
    path('registro/', users_views.registro_view, name='registro'),
    path('login/', users_views.login_view, name='login' ),
    path('logout/', users_views.logout_view, name='logout' ),
    path('posts/create', posts_views.posts_create , name='posts_crate'),
    path('me/perfil/', users_views.update_profile, name='update_profile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

