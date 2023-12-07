# check_permissions.py
from django.contrib.auth.models import User

user = User.objects.get(username='CarmenSandoval')  # Reemplaza 'tu_usuario' con tu nombre de usuario
print(user.has_perm('ensueño.view_pagina_personalizada'))
