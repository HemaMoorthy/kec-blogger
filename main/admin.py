from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleLike)
admin.site.register(ArticleReport)
admin.site.register(Follow)

admin.site.site_header = "KEConnect Admin"
admin.site.index_title = "Welcome to KEConnect"
admin.site.site_title = "KECoonect Admin Panel"