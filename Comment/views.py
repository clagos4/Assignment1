from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
import logging

def list_comments(request):
    comments = Comment.objects.all()
    return render(request, 'Comment/comment_list.html', { 'comments': comments })

def create_comment(request):
    logger = logging.getLogger(__name__)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        ip = request.META['REMOTE_ADDR']
        form.author_ip = ip
        form.save()
        return redirect('list_comments')
    
    return render(request, 'Comment/comments-form.html', { 'form': form })
    
