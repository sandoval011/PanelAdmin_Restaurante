from django import forms
from .models import MenuDiario

class MenuDiarioForm(forms.ModelForm):
    class Meta:
        model = MenuDiario
        fields = '__all__'

    def clean_menu(self):
        menu = self.cleaned_data.get('menu')
        existe_menu_diario = MenuDiario.objects.filter(menu=menu).exists()

        if existe_menu_diario:
            raise forms.ValidationError("Este menú ya ha sido añadido como Menú Diario.")

        return menu