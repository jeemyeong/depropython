from django.contrib import admin

# Register your models here.
from .models import category, board

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')

class BoardAdmin(admin.ModelAdmin):
    list_display = ('post_id','category_id', 'title', 'content', 'created_date')


admin.site.register(category, CategoryAdmin)
admin.site.register(board, BoardAdmin)
