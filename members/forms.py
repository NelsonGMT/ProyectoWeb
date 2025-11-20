from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'correo_electronico', 'contraseña']
        widgets = {
            'nombre_usuario': forms.TextInput(attrs={'placeholder': 'Escribe tu nombre de usuario'}),
            'correo_electronico': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'contraseña': forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        }
