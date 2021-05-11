from django import forms
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Usuario',
            'password': 'Contraseña',
            'first_name': 'Nombres',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
}
