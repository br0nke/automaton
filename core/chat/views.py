from django.shortcuts import render, get_object_or_404, redirect
from .models import Discussion, Post
from django.contrib.auth.decorators import login_required
from .forms import DiscussionForm, PostForm
from django.http import HttpRequest, HttpResponse
from . import models

@login_required
def discussion_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.starter = request.user
            discussion.save()
            return redirect('chat:discussion_list')
    else:
        form = DiscussionForm()
    discussions = Discussion.objects.all().order_by('-created_at')
    return render(request, 'chat/discussion_list.html', {'discussions': discussions, 'form': form})

@login_required
def discussion_detail(request: HttpRequest, pk) -> HttpResponse:
    discussion = get_object_or_404(Discussion, pk=pk)
    context = {'discussion': discussion}
    return render(request, 'chat/discussion_detail.html', context)

def discussion_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'chat/discussion_list.html', {'discussions': Discussion.objects.all()})

@login_required
def add_post(request: HttpRequest, discussion_id) -> HttpResponse:
    discussion = get_object_or_404(Discussion, pk=discussion_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.discussion = discussion
            post.save()
            return redirect('chat:discussion_detail', discussion_id)
    else:
        form = PostForm()
    return render(request, 'chat/discussion_detail.html', {'discussion': discussion, 'form': form})

