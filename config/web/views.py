from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados

# Create your views here.
#Todas la vistas son funciones de Python
#letra en mayuscula para convencion de las funciones de  vistas
def Home(request):
    return render(request,'home.html')

def Platos(request):
    #ESTA VISTA va utilizar un formulario de django
    #DEBO CREAR ENTONCES UN OBJETO DE LA CLASE fORMULARIO PLATOS
    formulario=FormularioPlatos()
    #creamos un disccionario para enviar un formulario al html (template)
    data={
        'formulario':formulario
    }
    return render(request,'menuplatos.html',data)

def Empleados(request):
    formulario2=FormularioEmpleados()
    data2={
        'formulario2':formulario2
    }
    return render(request,"registrarempleados.html",data2)
