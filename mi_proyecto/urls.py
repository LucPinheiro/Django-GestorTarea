from django.contrib import admin
from django.urls import path
from tareas import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(
        template_name='tareas/login.html'
    ), name='login'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('crear/', views.crear_tarea, name='crear_tarea'),
    path('editar/<int:id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('exportar/', views.exportar_csv, name='exportar_csv'),
    path('importar/', views.importar_csv, name='importar_csv'),
    path('detalle/<int:id>/', views.detalle_tarea, name='detalle_tarea'),
    path('cambiar-estado/<int:id>/<str:estado>/',
         views.cambiar_estado_simple,
         name='cambiar_estado_simple'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('eliminar-seleccionadas/', views.eliminar_tareas_seleccionadas, name='eliminar_tareas_seleccionadas'),
    path('tareas/<int:id>/prioridad/<int:prioridad>/',views.cambiar_prioridad,name='cambiar_prioridad'
),
]
