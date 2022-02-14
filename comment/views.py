

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from comment.models import Comment


class CommentView(ListView):
    model = Comment
    template_name = ''

