"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ejemplo.views import index, saludar_a, sumar, buscar, monstrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar, FamiliarDetalle
from django.views.generic import TemplateView  #Lo importo para mostrar el "success" que e sun template estático
from ejemplo_dos.views import (index, PostCrear, PostDetalle, PostListar, PostBorrar, 
                              PostActualizar, UserSignup, UserLogin, UserLogout, AvatarActualizar, UserActualizar, MensajeCrear,MensajeListar,MensajeDetalle, MensajeBorrar)
from django.contrib.admin.views.decorators import staff_member_required



urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludar/", index),
    path("saludar_a/<nombre>/", saludar_a),
    path("sumar/<int:a>/<int:b>/", sumar),
    path("buscar/", buscar),
    path("mi-familia/", monstrar_familiares),
    path("mi-familia/buscar", BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/', FamiliarList.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/crear', FamiliarCrear.as_view()),  #No olvidar poner la coma al final
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()), #Tenemos que pasar el id
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path("success_update_message/", TemplateView.as_view(template_name = "ejemplo/success_update_message.html")),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path("ejemplo-dos/", index, name= "ejemplo-dos-index"),
    path('ejemplo-dos/<int:pk>/detalle/', PostDetalle.as_view(), name="ejemplo-dos-detalle"),
    path('ejemplo-dos/listar/', PostListar.as_view(), name="ejemplo-dos-listar"),
    path('ejemplo-dos/crear/', staff_member_required(PostCrear.as_view()), name="ejemplo-dos-crear"),
    path('ejemplo-dos/<int:pk>/borrar/', staff_member_required(PostBorrar.as_view()), name="ejemplo-dos-borrar"),
    path('ejemplo-dos/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="ejemplo-dos-actualizar"),
    path("ejemplo-dos/signup/", UserSignup.as_view(), name = "ejemplo-dos-signup"),
    path("ejemplo-dos/login/", UserLogin.as_view(), name = "ejemplo-dos-login"),
    path("ejemplo-dos/logout/", UserLogout.as_view(), name = "ejemplo-dos-logout"),
    path("ejemplo-dos/avatares/<int:pk>/actualizar/", AvatarActualizar.as_view(), name = "ejemplo-dos-avatar-actualizar"),
    path("ejemplo-dos/user/<int:pk>/actualizar/", UserActualizar.as_view(), name = "ejemplo-dos-user-actualizar"),
    path("ejemplo-dos/mensajes/crear/", MensajeCrear.as_view(), name = "ejemplo-dos-mensajes-crear"),
    path("ejemplo-dos/mensajes/<int:pk>/detalle/", MensajeDetalle.as_view(), name = "ejemplo-dos-mensajes-detalle"),
    path("ejemplo-dos/mensajes/listar/", MensajeListar.as_view(), name = "ejemplo-dos-mensajes-listar"),
    path('ejemplo-dos/mensajes/<int:pk>/borrar/', MensajeBorrar.as_view(), name="ejemplo-dos-mensajes-borrar"),
    path('ejemplo-dos/about', TemplateView.as_view(template_name='ejemplo_dos/about.html'), name="ejemplo-dos-about"),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
