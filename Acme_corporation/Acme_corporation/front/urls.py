from django.urls import path
from back.views import Login,Padre,CrearCarroUsado
from back.views import FormularioVentaView,ReporteVenta
from back.views import verificacion,CrearPersona,ListaPersonas,ModificarPersona,ActualizarPersona,EliminarPersona
from back.views import ListaUsuarios,CrearUsuario,ActualizarUsuario,ModificarUsuario,EliminarUsuario
from back.views import Inicio,ListaCompras,CrearCompra,ActualizarCompra,ModificarCompra,EliminarCompra
from back.views import ListaCarros,CrearCarro,ActualizarCarro,ModificarCarro,EliminarCarro
from back.views import ListaVentas,CrearVenta,ActualizarVenta,ModificarVenta,EliminarVenta
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',Login.as_view()),
    path('verificacion/<str:Id_usuario>',verificacion,name="Verificacion"),
    path('home',Inicio.as_view(),name="Home"),
    path('padre',Padre.as_view(),name="Padre"),

    #Personas________________________________________________________________________________________________

    path('persona',ListaPersonas.as_view(),name="Persona"),
    path('agregarpersona',CrearPersona.as_view(),name="AGRpersona"),
    path('modipersona',ModificarPersona.as_view(),name="MODpersona"),
    path('eliminarpersona/<int:pk>',EliminarPersona.as_view()),
    path('resulmodipersona/<int:pk>',ActualizarPersona.as_view()),

    #Compras________________________________________________________________________________________________
    
    path('compra',ListaCompras.as_view(),name="Compra"),
    path('agregarcompra',CrearCompra.as_view(),name="AGRcompra"),
    path('modicompra',ModificarCompra.as_view(),name="MODcompra"),
    path('eliminarcompra/<int:pk>',EliminarCompra.as_view()),
    path('resulmodicompra/<int:pk>',ActualizarCompra.as_view()),
    
    #Carro________________________________________________________________________________________________

    path('carro',ListaCarros.as_view(),name="Carro"),
    path('agregarcarro',CrearCarro.as_view(),name="AGRcarro"),
    path('modicarro',ModificarCarro.as_view(),name="MODcarro"),
    path('eliminarcarro/<str:pk>',EliminarCarro.as_view()),
    path('resulmodicarro/<str:pk>',ActualizarCarro.as_view()),
    path('carrousado',CrearCarroUsado.as_view(),name="CRRusado"),

    #Ventas________________________________________________________________________________________________

    path('venta',ListaVentas.as_view(),name="Venta"),    
    path('agregarventa',CrearVenta.as_view(),name="AGRventa"),
    path('modiventa',ModificarVenta.as_view(),name="MODventa"),
    path('resulmodiventa/<int:pk>',ActualizarVenta.as_view()),
    path('eliminarventa/<int:pk>',EliminarVenta.as_view()),
    path('reporte_ventas',ReporteVenta.reporte_ventas),
   
    #Usuarios________________________________________________________________________________________________

    path('usuario',ListaUsuarios.as_view(),name="Usuario"),
    path('agregarusuario',CrearUsuario.as_view(),name="AGRusuario"),
    path('modiusuario',ModificarUsuario.as_view(),name="MODusuario"),
    path('eliminarusuario/<int:pk>',EliminarUsuario.as_view()),
    path('resulmodiusuario/<int:pk>',ActualizarUsuario.as_view()),

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)