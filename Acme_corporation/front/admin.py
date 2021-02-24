from django.contrib import admin

from back import models
# Register your models here.
admin.site.register(models.Usuarios)
admin.site.register(models.Carros)
admin.site.register(models.Intermediario)
admin.site.register(models.Personas)
admin.site.register(models.Compra)
admin.site.register(models.Venta)
admin.site.register(models.Marcas)

