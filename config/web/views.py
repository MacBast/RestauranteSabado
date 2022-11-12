from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados
from web.models import Platos
from web.models import Empleados

# Create your views here.
#Todas la vistas son funciones de Python
#letra en mayuscula para convencion de las funciones de  vistas
def Home(request):
    return render(request,'home.html')

def PlatosView(request):

    # platosConsultados=Platos.objects.all()
    # print(platosConsultados)

    #ESTA VISTA va utilizar un formulario de django
    #DEBO CREAR ENTONCES UN OBJETO DE LA CLASE fORMULARIO PLATOS
    formulario=FormularioPlatos()
    #creamos un disccionario para enviar un formulario al html (template)
    data={
        'formulario':formulario,
        'bandera':False,
        # 'platos':platosConsultados
    }
    if request.method=="POST":
        datosformulario=FormularioPlatos(request.POST)
        if datosformulario.is_valid():
            print("holi soy la funcion")
            datoslimpios=datosformulario.cleaned_data
            print (datoslimpios)

            platoNuevo=Platos(
                nombre=datoslimpios["nombre"],
                descripcion=datoslimpios["descripcion"],
                fotografia=datoslimpios["fotografia"],
                precio=datoslimpios["precio"],
                tipo=datoslimpios["tipo"]
            )
            try:
                platoNuevo.save()
                data["bandera"]=True
                print("Exito Guardando")
            except Exception as error:
                print("Paila papi no se guardo", error)

    return render(request,'menuplatos.html',data)

def EmpleadosView(request):
    formulario2=FormularioEmpleados()
    data2={
        'formulario2':formulario2,
        'bandera':False
    }
    if request.method=="POST":
        datosformularioEmpleados=FormularioEmpleados(request.POST)
        if datosformularioEmpleados.is_valid():
            datoslimpios=datosformularioEmpleados.cleaned_data
            print (datoslimpios)

            empleadoNuevo=Empleados(
                nombre=datoslimpios["nombre"],
                apellido=datoslimpios["apellido"],
                foto=datoslimpios["foto"],
                cargo=datoslimpios["cargo"],
                salario=datoslimpios["salario"],
                contacto=datoslimpios["contacto"]
            )
            try:
                empleadoNuevo.save()
                data2["bandera"]=True
                print("Exito Guardando")
            except Exception as error:
                print("Paila papi no se guardo", error)

    return render(request,"registrarempleados.html",data2)
