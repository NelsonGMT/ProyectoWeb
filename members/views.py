from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import RegistroUsuarioForm

# ==============================
# Página de inicio (solo si ha iniciado sesión)
# ==============================
@login_required(login_url='login')
def inicio(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')
    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'paginas/Inicio.html', {'usuario': usuario})


# ==============================
# Otras páginas públicas
# ==============================
def cartelera(request):
    return render(request, "paginas/cartelera.html")

def proyecto_view(request):
    return render(request, "paginas/Proyecto.html")


# ==============================
# Páginas de películas
# ==============================
def proyecto_pag_wicked(request): return render(request, "paginas/ProyectoPagWicked.html")
def proyecto_pag_nosf(request): return render(request, "paginas/ProyectoPagNosf.html")
def proyecto_pag_wolvpool(request): return render(request, "paginas/ProyectoPagWolvPool.html")
def proyecto_pag_jackjill(request): return render(request, "paginas/ProyectoPagJackJill.html")
def proyecto_pag_flow(request): return render(request, "paginas/ProyectoPagFlow.html")
def proyecto_pag_ghostworld(request): return render(request, "paginas/ProyectoPagGhostWorld.html")
def proyecto_pag_gatobotas(request): return render(request, "paginas/ProyectoPagGatoBotas.html")
def proyecto_pag_shrek2(request): return render(request, "paginas/ProyectoPagShrek2.html")
def proyecto_pag_it(request): return render(request, "paginas/ProyectoPagIT.html")
def proyecto_pag_deadpool(request): return render(request, "paginas/ProyectoPagDeadpool.html")
def proyecto_pag_johnwick(request): return render(request, "paginas/ProyectoPagJohnWick.html")
def proyecto_pag_detectivepikachu(request): return render(request, "paginas/ProyectoPagDetectivePikachu.html")


# ==============================
# Registro de usuario
# ==============================
def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            # Guardar directamente en la base de datos
            form.save()
            messages.success(request, 'Registro exitoso. ¡Ahora puedes iniciar sesión!')
            return redirect('login')
        else:
            messages.error(request, 'Error en el registro. Verifica los datos.')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'register.html', {'form': form})



# ==============================
# Login personalizado
# ==============================
def login_usuario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario')
        contraseña = request.POST.get('contraseña')

        try:
            usuario = Usuario.objects.get(nombre_usuario=nombre_usuario, contraseña=contraseña)
            request.session['usuario_id'] = usuario.id
            messages.success(request, f'¡Bienvenido {usuario.nombre_usuario}!')
            return redirect('dashboard')
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, 'paginas/login.html')


# ==============================
# Dashboard (después del login)
# ==============================
def dashboard(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')

    usuario = Usuario.objects.get(id=usuario_id)
    return render(request, 'paginas/dashboard.html', {'usuario': usuario})
