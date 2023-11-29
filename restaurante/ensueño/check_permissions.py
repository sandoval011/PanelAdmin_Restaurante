# check_permissions.py
from django.contrib.auth.models import User

user = User.objects.get(username='CarmenSandoval')  
print(user.has_perm('ensueño.view_pagina_personalizada'))
