from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from back.forms import FormularioCarros,FormularioCompra,FormularioPersonas,FormularioUsuarios,FormularioVenta
from back.models import Carros,Compra,Personas,Usuarios,Venta
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter, landscape,A4
from reportlab.platypus import TableStyle,Table,SimpleDocTemplate,Spacer,Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from django.views.generic import View,TemplateView,ListView,DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy


# Create your views here.

class Padre(TemplateView):
    template_name = 'padre.html'

    def get(self,request):
        usuarios = Usuarios.objects.all()
        return render(request,self.template_name,{'usuario':usuarios}) 

class Inicio(TemplateView):
        
    template_name = 'home.html'

    def get(self,request):
        personas = Personas.objects.all()
        ventas = Venta.objects.all()
        carros = Carros.objects.all()
        compras = Compra.objects.all()
        return render(request,self.template_name,{'personas':personas,'ventas':ventas,'carros':carros,'compras':compras}) 

#////////////////////////////////////////////////////////USUARIO/////////////////////////////////////////////////////////////////////////

class ListaUsuarios(ListView):    
    model = Usuarios
    template_name = 'Usuarios.html'
    context_object_name = 'usuarios'
    queryset = Usuarios.objects.all()

class CrearUsuario(CreateView):
    model = Usuarios
    template_name = 'agregar_usuario.html'
    form_class = FormularioUsuarios
    success_url = reverse_lazy('Usuario')

class ModificarUsuario(TemplateView):
        
    template_name = 'modificar_usuario.html'

    def get(self,request):
        usuarios = Usuarios.objects.all()
        return render(request,self.template_name,{'shelf':usuarios}) 

class ActualizarUsuario(UpdateView):

    model = Usuarios
    template_name = 'resultados_usua.html'
    form_class = FormularioUsuarios
    success_url = reverse_lazy('Usuario')

class EliminarUsuario(DeleteView):
    model = Usuarios
    template_name = 'resultados_usua.html'
    success_url = reverse_lazy('Usuario')

#////////////////////////////////////////////////////////PERSONAS/////////////////////////////////////////////////////////////////////////

class ListaPersonas(ListView):
        
    model = Personas
    template_name = 'cliente.html'
    context_object_name = 'personas'
    queryset = Personas.objects.all()

class ModificarPersona(TemplateView):
        
    template_name = 'modificar_cliente.html'

    def get(self,request):
        personas = Personas.objects.all()
        return render(request,self.template_name,{'shelf':personas}) 

class CrearPersona(CreateView):

    model = Personas
    template_name = 'agregar_cliente.html'
    form_class = FormularioPersonas
    success_url = reverse_lazy('Persona')


class ActualizarPersona(UpdateView):

    model = Personas
    template_name = 'resultados_cli.html'
    form_class = FormularioPersonas
    success_url = reverse_lazy('Persona')

class EliminarPersona(DeleteView):
    model = Personas
    template_name = 'resultados_cli.html'
    success_url = reverse_lazy('Persona')

#////////////////////////////////////////////////////////CARROS/////////////////////////////////////////////////////////////////////////
class ListaCarros(ListView):
    model = Carros
    template_name = 'carros.html'
    context_object_name = 'carro'
    queryset = Carros.objects.all()

class ModificarCarro(TemplateView):
        
    template_name = 'modificar_carro.html'

    def get(self,request):
        carros = Carros.objects.all()
        return render(request,self.template_name,{'shelf':carros}) 

class CrearCarro(CreateView):

    model = Carros
    template_name = 'agregar_carro.html'
    form_class = FormularioCarros
    success_url = reverse_lazy('Carro')

class ActualizarCarro(UpdateView):

    model = Carros
    template_name = 'resul_carro.html'
    form_class = FormularioCarros
    success_url = reverse_lazy('Carro')

class EliminarCarro(DeleteView):
    model = Carros
    template_name = 'resul_carro.html'
    success_url = reverse_lazy('Carro')

#////////////////////////////////////////////////////////VENTAS/////////////////////////////////////////////////////////////////////////

class ListaVentas(ListView):
        
    model = Venta
    template_name = 'ventas.html'
    context_object_name = 'ventas'
    queryset = Venta.objects.all()

class ModificarVenta(TemplateView):
        
    template_name = 'modificar_venta.html'

    def get(self,request):
        ventas = Venta.objects.all()
        return render(request,self.template_name,{'shelf':ventas}) 

class CrearVenta(CreateView):

    model = Venta
    template_name = 'agregar_venta.html'
    form_class = FormularioVenta
    success_url = reverse_lazy('Venta')

class ActualizarVenta(UpdateView):

    model = Venta
    template_name = 'resultados_venta.html'
    form_class = FormularioVenta
    success_url = reverse_lazy('Venta')

class EliminarVenta(DeleteView):
    model = Venta
    template_name = 'resultados_venta.html'
    success_url = reverse_lazy('Venta')

class FormularioVentaView(HttpRequest):

    def buscar(request):
    
        if request.GET["carro"]:

            carro=request.GET["carro"]
    
            carros=Carros.objects.filter(Marca__icontains=carro)

            return render(request,"resultados_pro.html",{"carros":carros,"query":carro})
    
        else:

            mensaje="No Hay Datos De Busqueda"    
     
        return HttpResponse(mensaje)        

#////////////////////////////////////////////////////////COMPRAS/////////////////////////////////////////////////////////////////////////

class ListaCompras(ListView):
        
    model = Compra
    template_name = 'compras.html'
    context_object_name = 'compras'
    queryset = Compra.objects.all()

class ModificarCompra(TemplateView):
        
    template_name = 'modificar_compra.html'

    def get(self,request):
        compras = Compra.objects.all()
        return render(request,self.template_name,{'shelf':compras}) 

class CrearCompra(CreateView):

    model = Compra
    template_name = 'agregar_compra.html'
    form_class = FormularioCompra
    success_url = reverse_lazy('AGRcarro')

class ActualizarCompra(UpdateView):

    model = Compra
    template_name = 'resultados_compra.html'
    form_class = FormularioCompra
    success_url = reverse_lazy('Compra')

class EliminarCompra(DeleteView):
    model = Compra
    template_name = 'resultados_compra.html'
    success_url = reverse_lazy('Compra')



#////////////////////////////////////////////////////////LOGIN/////////////////////////////////////////////////////////////////////////

class Login(TemplateView):

    template_name = 'login.html'

    def get(self,request):
        usuarios = Usuarios.objects.all()
        return render(request,self.template_name,{'shelf':usuarios}) 

def verificacion(request,Id_usario):
        Id_usario = int (Id_usario)
        try:
            usuario_sel = Usuarios.objects.get(Id_usario = Id_usario)

        except  Usuarios.DoesNotExist:
            return render(request, "loguin.html")
            
        miformulario = FormularioUsuarios(request.POST or None,instance= usuario_sel)            
        if miformulario.is_valid():
            miformulario.save()
            miformulario = FormularioUsuarios()
            mensaje=("Usuario Actualizado")
            return render(request,"home.html",{"mensaje":mensaje})
        return render(request,"home.html")

#////////////////////////////////////////////////////////Report/////////////////////////////////////////////////////////////////////////

class ReporteVenta(object):

    def __init__(self):
        self.buf = BytesIO()

    def run(self):
        self.doc = SimpleDocTemplate(self.buf)
        self.story = []
        self.encabezado()
        self.crearTabla()
        self.doc.build(self.story, onFirstPage=self.numeroPagina, 
            onLaterPages=self.numeroPagina)
        pdf = self.buf.getvalue()
        self.buf.close()
        return pdf

    def encabezado(self):
        self.story.append(Spacer(1,0.5*inch))
        p = Paragraph("Reporte Ventas", self.estiloPC())
        self.story.append(p)
        self.story.append(Spacer(1,0.5*inch))


    def crearTabla(self):

        data = [["Placa","Empleado","Cliente","Fecha","Precio"]] \
            +[[x.Placa, x.Vendedor, x.Comprador, x.Fecha, x.Precio] 
                for x in Venta.objects.all() ]
                            
        style = TableStyle([
            ('GRID', (0,0), (-1,-1), 0.25, colors.black),
            ('ALIGN',(0,0),(-1,-1),'CENTER'),
            ('VALIGN',(0,0),(-1,-1),'MIDDLE')])

        t = Table(data)
        t.setStyle(style)
        self.story.append(t)
    

    def estiloPC(self):
        return ParagraphStyle(name="centrado", alignment=TA_CENTER)

    def numeroPagina(self,canvas,doc):
        num = canvas.getPageNumber()
        text = "Pagina %s" % num
        canvas.drawRightString(200*mm, 20*mm, text)

    def reporte_ventas(request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="ventas.pdf"'
        r = ReporteVenta()
        response.write(r.run())
        return response
