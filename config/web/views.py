from django.shortcuts import render

# Create your views here.
#Todas la vistas son funciones de Python
#letra en mayuscula para convencion de las funciones de  vistas
def Home(request):
    return render(request,'home.html')
