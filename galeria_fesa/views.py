from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render 


def home_page(request):
   return render(request, 'posts/post_list.html')


