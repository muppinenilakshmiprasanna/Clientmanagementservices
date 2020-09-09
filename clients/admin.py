from django.contrib import admin

from .models import Client, Comment,Vehicle


class CommentInline(admin.TabularInline):
    model = Comment

class VehicleInline(admin.TabularInline):
    model = Vehicle


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        VehicleInline
    ]
    list_display = ('name','email','author')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'author', 'client')


admin.site.register(Client, ClientAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Vehicle)
