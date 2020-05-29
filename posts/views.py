
#post_views

from datetime import datetime
# Create your views here.



# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post

@login_required
<<<<<<< HEAD
def list_posts(request):
	posts = Post.objects.all().order_by('-create')
	return render(request, 'posts/feed2.html', {'posts': posts})
=======

def list_posts(request):
	return render(request,'posts/post_list.html')
>>>>>>> 416cf15fe86b1887006b23f6ece33f2e3b183d0a



@login_required
def posts_create(request):
	
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed2')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'perfil': request.user.perfil
        }
    )