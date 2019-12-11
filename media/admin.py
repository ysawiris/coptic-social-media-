from django.contrib import admin
from media.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('slug', 'author', 'created')


admin.site.register(Post, PostAdmin)

