from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Página de inicio
    path('', views.inicio, name='inicio'),

    # Login / Logout personalizados
    path('login/', views.login_usuario, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Registro
path('register/', views.register, name='register'),

    # Dashboard (después del login)
    path('dashboard/', views.dashboard, name='dashboard'),

    # Recuperar contraseña (sistema de Django)
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(template_name="paginas/password_reset.html"),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name="paginas/password_reset_done.html"),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name="paginas/password_reset_confirm.html"),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name="paginas/password_reset_complete.html"),
        name='password_reset_complete'
    ),

    # Otras páginas
    path('cartelera/', views.cartelera, name='cartelera'),
    path('proyecto/', views.proyecto_view, name='proyecto'),

    # Proyectos/películas
    path('proyecto/wicked/', views.proyecto_pag_wicked, name='ProyectoPagWicked'),
    path('proyecto/nosf/', views.proyecto_pag_nosf, name='ProyectoPagNosf'),
    path('proyecto/wolvpool/', views.proyecto_pag_wolvpool, name='ProyectoPagWolvPool'),
    path('proyecto/jackjill/', views.proyecto_pag_jackjill, name='ProyectoPagJackJill'),
    path('proyecto/flow/', views.proyecto_pag_flow, name='ProyectoPagFlow'),
    path('proyecto/ghostworld/', views.proyecto_pag_ghostworld, name='ProyectoPagGhostWorld'),
    path('proyecto/gatobotas/', views.proyecto_pag_gatobotas, name='ProyectoPagGatoBotas'),
    path('proyecto/shrek2/', views.proyecto_pag_shrek2, name='ProyectoPagShrek2'),
    path('proyecto/it/', views.proyecto_pag_it, name='ProyectoPagIT'),
    path('proyecto/deadpool/', views.proyecto_pag_deadpool, name='ProyectoPagDeadpool'),
    path('proyecto/johnwick/', views.proyecto_pag_johnwick, name='ProyectoPagJohnWick'),
    path('proyecto/detectivepikachu/', views.proyecto_pag_detectivepikachu, name='ProyectoPagDetectivePikachu'),
]
