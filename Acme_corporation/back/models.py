from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.

#Usuarios

class Usuarios(models.Model):

    Username = models.CharField(max_length = 50,unique = True)
    Email = models.EmailField(max_length = 254,unique = True)
    Nombres = models.CharField(max_length = 200,blank = True,null = True)
    Apellidos = models.CharField(max_length = 200,blank = True,null = True)
    Imagen_Perfil = models.ImageField('Imagen Perfil',upload_to = 'Imagen_Perfil/',max_length = 200,blank = True,null = True)
    Fecha_Nacimiento = models.DateField()
    Password = models.CharField(max_length=20)
    Usuario_activo = models.BooleanField(default = True)
    
    def __str__(self):
       return self.Username    

#_____________________________________________________________________________________________
#Personas

class Personas(models.Model):

    Nombres = models.CharField(max_length = 100,null = False)
    Apellidos = models.CharField(max_length=100,null= False)
    Cedula = models.CharField(primary_key = True,max_length = 40,null = False)
    Telefono = models.CharField(max_length = 20,null = True)
    Fecha = models.DateField("Fecha (Año/Mes/Dia)", default = timezone.now)

 #Metada
    class Meta:
        ordering = ["Cedula"]
    
    def __str__(self):
        return self.Nombres

#_____________________________________________________________________________________________

class Marcas(models.Model):

    Id_Marca = models.AutoField(primary_key = True)
    Nombre = models.CharField(max_length = 50 , null=False)
    Imagen = models.URLField(max_length = 600)
    Fecha = models.DateField("Fecha (Año/Mes/Dia)", default = timezone.now)

 #Metada
    class Meta:
        ordering = ["Nombre"]
    
    def __str__(self):
        return self.Nombre


#Carros
class Carros(models.Model):
    
    Status=((('Nuevo','Nuevo')),(('Usado','Usado')))

    Marca = models.ForeignKey(Marcas,on_delete = models.CASCADE)
    Modelo = models.CharField(max_length= 50,null=False)
    Placa = models.CharField(primary_key = True,max_length = 10,null = False)
    Dueño = models.ForeignKey(Personas,on_delete = models.CASCADE,default = "Acme")
    Fechapublicacion = models.DateField()
    Precio = models.IntegerField(null = False)
    Imagen = models.URLField(max_length = 600)
    Estado = models.CharField(
        max_length = 15,choices = Status,default = 'Nuevo'
    )

     #Metada
    class Meta:
        ordering = ["Marca"]

    def __str__(self):
        return "{0}  {1}".format(self.Placa,self.Marca)

#_____________________________________________________________________________________________
#Venta
class Venta(models.Model):

    Id_venta = models.AutoField(primary_key = True)
    Placa = models.ForeignKey(Carros,on_delete = models.CASCADE)
    Marca = Carros.Marca
    Vendedor = models.ForeignKey(Usuarios,on_delete = models.CASCADE)
    Comprador = models.ForeignKey(Personas,on_delete = models.CASCADE)
    Fecha = models.DateField(default = timezone.now)
    Precio = models.IntegerField()
    
    #Metada
    class Meta:
        ordering = ["Fecha"]

    def __str__(self):
        return self.Id_venta

#_____________________________________________________________________________________________
#Compras
class Compra(models.Model):

    Id_compra = models.AutoField(primary_key = True)
    Placa = models.ForeignKey(Carros,on_delete = models.CASCADE)
    Marca = Carros.Marca
    Vendedor = models.ForeignKey(Personas,on_delete = models.CASCADE)
    Comprador = models.ForeignKey(Usuarios,on_delete = models.CASCADE)
    Fecha = models.DateField(default = timezone.now)
    Precio = models.IntegerField()
    

    #Metada
    class Meta:
        ordering = ["Fecha"]

    def __str__(self):
        return self.Comprador

class Intermediario(models.Model):
    
    Id_intermediario = models.AutoField(primary_key= True)
    Intermediario = models.ForeignKey(Usuarios,on_delete = models.CASCADE)
    Placa = models.ForeignKey(Carros,on_delete = models.CASCADE)
    Marca = Carros.Marca
    Comprador = models.ForeignKey(Personas,on_delete = models.CASCADE)
    Dueño = Personas.Nombres
    Fecha = models.DateField(default = timezone.now)
    Precio = models.IntegerField()
    
    class Meta:
        ordering = ["Fecha"]

    def __str__(self):
        return self.Comprador
