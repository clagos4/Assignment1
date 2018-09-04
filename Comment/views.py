from django.shortcuts import render
from .models import Comment

def list_comments(request):
    comments = Comment.objects.all()
    return render(request, 'Comment/comment_list.html', { 'comments': comments })