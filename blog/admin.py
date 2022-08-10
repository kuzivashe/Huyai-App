from django.contrib import admin
from .models import Post, Item
from embed_video.admin import AdminVideoMixin


admin.site.register(Post)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Item, MyModelAdmin)