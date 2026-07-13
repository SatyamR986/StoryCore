from django.contrib import admin
from .models import Story, Node, Choice

admin.site.register(Story)
admin.site.register(Node)
admin.site.register(Choice)