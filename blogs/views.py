from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Comment, Post
from .forms import PostForm, CommentForm
# Create your views here.

def index(request):
    posts =  Post.objects.all()
    return render(request,"blogs/index.html",{
        'posts': posts
    })

def newblogs(request):
    if request.method == "POST":
        form= PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form= PostForm()

    return render(request,'blogs/newpost.html', {'form':form})   

def individual(request,pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    
    if request.method == 'POST':
        add_comment = CommentForm(request.POST)
        if add_comment.is_valid():
            comment = add_comment.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('individual', pk=post.pk)
        
    else:
        add_comment = CommentForm(request.POST)
 
    return render(request,"blogs/individual.html", { 
        "post" : post,
        "comments": comments,
         "add_comment" : add_comment
         })
    

def editblogs(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post =form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('individual', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blogs/editblogs.html',{
            'form':form
        })
   
def deleteblog(request,pk):
    post =Post.objects.get(pk=pk)
    post.delete()
    return redirect('index')


def delcomment(request,pk):
    comment = Comment.objects.get(pk= pk)
    post_id = comment.post.id
    comment.delete()
    return redirect('individual', pk=post_id)
