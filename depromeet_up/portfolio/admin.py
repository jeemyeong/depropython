from django.contrib import admin

# Register your models here.
from .models import category, board, imghandler

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')

class BoardAdmin(admin.ModelAdmin):
    list_display = ('post_id','category_id', 'title', 'content', 'created_date')

class imgAdmin(admin.ModelAdmin):
    list_display = ('upload_path','image', 'image_url', 'post_id')

admin.site.register(category, CategoryAdmin)
admin.site.register(board, BoardAdmin)
admin.site.register(imghandler, imgAdmin)