from django import forms

class FormularioPlatos(forms.Form):

    PLATOS=(
        (1,'Entrada'),
        (2,'Plato Fuerte'),
        (3,'Postre'),
    )

    nombre=forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    descripcion=forms.CharField(
        required=False,
        max_length=100,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})
    )
    fotografia=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    precio=forms.CharField(
        required=True,
        max_length=6,
        min_length=0,
        initial=10000,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )
    tipo=forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class':'form-control mb-3'}),
        choices=PLATOS
    )