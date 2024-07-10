from django.urls import path
from .views import GestionarObjetivosView, GestionarIndicadoresView, GestionarAGCView, GestionarUGCView, CrearUGCView, EditarUGCView, CrearObjetivoView, EditarObjetivoView, CrearIndicadorView, EditarIndicadorView, EliminarIndicadorView, CrearAGCView, EditarAGCView, EliminarAGCView, GestionarIndicadoresAGCView, CrearAcuerdoIndicadorView, EditarAcuerdoIndicadorView, EliminarAcuerdoIndicadorView, CustomLoginView,  inicio
from . import views


urlpatterns = [
    path('', inicio, name='inicio'),

    path('objetivos/', GestionarObjetivosView.as_view(), name='gestionar_objetivos'),
    path('objetivos/crear/', CrearObjetivoView.as_view(), name='crear_objetivo'),
    path('objetivos/editar/<int:id_objetivo>/', EditarObjetivoView.as_view(), name='editar_objetivo'),

    path('indicadores/', GestionarIndicadoresView.as_view(), name='gestionar_indicadores'),
    path('indicadores/crear/', CrearIndicadorView.as_view(), name='crear_indicador'),
    path('indicadores/editar/<int:pk>/', EditarIndicadorView.as_view(), name='editar_indicador'),
    path('indicadores/eliminar/<int:pk>/', EliminarIndicadorView.as_view(), name='eliminar_indicador'),

    path('agc/', GestionarAGCView.as_view(), name='gestionar_agc'),
    path('agc/crear/', CrearAGCView.as_view(), name='crear_agc'),
    path('agc/editar/<int:pk>/', EditarAGCView.as_view(), name='editar_agc'),
    path('agc/eliminar/<int:pk>/', EliminarAGCView.as_view(), name='eliminar_agc'),

    path('agc/<int:pk>/indicadores/', GestionarIndicadoresAGCView.as_view(), name='gestionar_indicadores_agc'),
    path('agc/<int:agc_pk>/indicadores/crear/', CrearAcuerdoIndicadorView.as_view(), name='crear_acuerdo_indicador'),
    path('indicadores/editar/<int:pk>/', EditarAcuerdoIndicadorView.as_view(), name='editar_acuerdo_indicador'),
    path('acuerdo_indicador/eliminar/<int:pk>/', EliminarAcuerdoIndicadorView.as_view(), name='eliminar_acuerdo_indicador'),

    path('ugc/', GestionarUGCView.as_view(), name='gestionar_ugc'),
    path('ugc/crear/', CrearUGCView.as_view(), name='crear_ugc'),
    path('ugc/editar/<int:id_ugc>/', EditarUGCView.as_view(), name='editar_ugc'),

    path('export/agc-excel/', views.export_agc_excel, name='export_agc_excel'),
    path('import/agc-excel/', views.import_agc_excel, name='import_agc_excel'),
    path('import_export/', views.import_export, name='import_export'),
    path('export/objetivo-template/', views.export_objetivo_template, name='export_objetivo_template'),
    path('import/objetivo-excel/', views.import_objetivo_excel, name='import_objetivo_excel'),

    path('login/', CustomLoginView.as_view(), name='login'),
]