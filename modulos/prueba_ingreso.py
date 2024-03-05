import os

def PruebaIngreso(campus = dict):
    titulo= """
        +++++++++++++++++++++
        + PRUEBA DE INGRESO +
        +++++++++++++++++++++
    """
    print(titulo)
    for values in campus['campers'].values():
        if values['estado'] != 'inscrito':
            continue
        os.system('cls')
        nombre = values['nombre']
        apellido = values['apellido']
        identificacion = values['identificacion']
        print(f'Candidato: {nombre} {apellido} con identificacion {identificacion}')
        isValueTrue = True
        while isValueTrue:
            try:
                practica= int(input(f'ingrese la nota practica :'))
            except ValueError:
                print('no estas ingresando un valor entero')
                os.system('pause')
            else:
                if practica < 0 and practica >100:
                    print('la nota debe ser entre 1 y 100')
                else:
                    isValueTrue= False
        isValueTrue = True
        while isValueTrue:
            try:
                teorica= int(input('ingrese la nota teorica :'))
            except ValueError:
                print('no estas ingresando un valor entero')
                os.system('pause')
            else:
                if teorica < 0 and teorica >100:
                    print('la nota debe ser entre 1 y 100')
                else:
                    isValueTrue= False
        promedio = (practica + teorica) / 2
        if promedio >= 60:
            values['estado']= 'aprobadoI'
        else:
            values['estado']= 'desaprobado'

