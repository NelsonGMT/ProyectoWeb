from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from members import views   # Importar las vistas de la app members

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('members.urls')),   # Incluye las rutas de la app

    # login/logout usando vistas de Django
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

# Recuperar contraseña
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



    # registro y dashboard
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
