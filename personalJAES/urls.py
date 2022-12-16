from django.urls import path
from . import views

urlpatterns = [
    path('unidades/', views.UnidadViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='unidades'),
    path('unidades/<int:pk>/', views.UnidadViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='unidad-detail'),
    path('departamentos/', views.DepartamentoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='departamentos'),
    path('departamentos/<int:pk>/', views.DepartamentoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='departamento-detail'),
    path('negociados/', views.NegociadoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='negociados'),
    path('negociados/<int:pk>/', views.NegociadoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='negociado-detail'),
    path('personas/', views.PersonaViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='personas'),
    path('personas/<int:pk>/', views.PersonaViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }), name='persona-detail'),
]
