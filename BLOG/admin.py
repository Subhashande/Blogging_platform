from django.shortcuts import render
from .models import Post
# Create your views here.
# admin.py
from django.contrib import admin

admin.site.register(Post)