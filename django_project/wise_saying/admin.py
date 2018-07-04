from django.contrib import admin
from .models import Member, Saying, Like

# Register your models here.
admin.site.register(Member)
admin.site.register(Saying)
admin.site.register(Like)