from django.contrib import admin
from .models import Curso,Compra,Capitulo,Leccion,LoqueAprenderas,Tutoriales,comentarios

class loque(admin.TabularInline):
    model = LoqueAprenderas

class cursoAdmin(admin.ModelAdmin):
    inlines = [loque]

admin.site.register(Compra)
admin.site.register(Capitulo)
admin.site.register(Leccion)
admin.site.register(Curso,cursoAdmin)
admin.site.register(Tutoriales)
admin.site.register(comentarios)