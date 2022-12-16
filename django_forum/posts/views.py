from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # if the method is POST 
    if request.method == 'POST':
        form = PostForm(request.POST) 
        # if the for is valid
        if form.is_valid():
            # Yes, save
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')
        else:
            # No, show Error
            return HttpResponseRedirect(form.errors.as_json())
    
    
    #get all posts, limit = 20
    posts = Post.objects.all().order_by('created_at')[:20]
    
    # show
    return render(request, 'post.html',
                   {'posts': posts})

# Create your views here.

def delete(request, post_id):
    # Find post
    
    post =Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

