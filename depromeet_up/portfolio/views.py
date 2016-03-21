# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime
import hashlib
from .models import board, category, imghandler
from HTMLParser import HTMLParser


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

    #글 속의 이미지 등록
    class ImageParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'img':
                return
            if not hasattr(self, 'result'):
                self.result = []
            for name, value in attrs:
                if name == 'src':
                    self.result.append(value)

    parser = ImageParser()

    try:
        parser.feed(content)
        cnt = 0
        for x in parser.result:
            if cnt == 0 :
                img = imghandler(image_url=x)
                pst = board.objects.get(post_id=post.post_id)
                img.post_id = pst
                img.save()
                cnt += 1

            else : break
    except AttributeError:
        pass


    return HttpResponseRedirect(reverse('home'))