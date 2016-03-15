from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
import hashlib
from .models import board, category

# Create your views here.

def write(request):
    return render(request, 'post.html')

def post(request):

    today = datetime.today()

    category_id = request.POST['category_id']

    title = request.POST['title']
    content = request.POST['content']
    created_date = today

    post = board(title=title, content=content, created_date=created_date)

    cate = category.objects.get(category_id=category_id)
    post.category_id = cate
    post.save()

    return HttpResponseRedirect(reverse('home'))