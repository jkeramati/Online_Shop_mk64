from django.contrib import admin
from django.urls import path, include

from comment.views import CommentView

urlpatterns = [
    path('', CommentView.as_view(), 'comment_view'),

]
