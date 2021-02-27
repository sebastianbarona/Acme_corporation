from django import forms
from django.forms import ModelForm ,CharField,PasswordInput
from back.models import Usuarios,Personas,Carros,Compra,Venta,Intermediario
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
      input_type = 'date'


class FormularioUsuarios(forms.ModelForm):

  class Meta:

      model = Usuarios

      fields= '__all__'
      widgets= {'Fecha_Nacimiento':DateInput(),'Email':forms.EmailInput(),'Password':PasswordInput}

#----------------------------------------------------------------------------------------------------------
         
class FormularioPersonas(forms.ModelForm):

 class Meta:
  
      model = Personas
      fields = '__all__'
      widgets= {'Fecha':DateInput()}

#----------------------------------------------------------------------------------------------------------
      
class FormularioCarros(forms.ModelForm):

 class Meta:
  
      model = Carros
      fields = '__all__'
      widgets= {'Fechapublicacion':DateInput()}

#----------------------------------------------------------------------------------------------------------
class FormularioCompra(forms.ModelForm):

 class Meta:

  
      model = Compra
      fields = '__all__'

#----------------------------------------------------------------------------------------------------------
 
class FormularioVenta(forms.ModelForm):

 class Meta:

  
      model = Venta
      fields = '__all__'
      widgets= {'Fecha':DateInput()}

#----------------------------------------------------------------------------------------------------------
class FormularioIntermediario(forms.ModelForm):

 class Meta:

  
      model = Intermediario
      fields = '__all__'

