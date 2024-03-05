import os

def Registro(campus: dict):
    os.system('cls')
    titulo = """
    +++++++++++++++++++++++
    + REGISTRO DE CAMPERS +
    +++++++++++++++++++++++
    """
    print(titulo)
    print('ingrese la siguiente informacion para el camper que desea registrar')
    isValueTrue= True
    while isValueTrue:
        identificacion = str(input('Numero de identificacion :'))
        if len(campus['campers']) == 0:
            break
        for key, val in campus['campers'].items():
            if identificacion == key:
                print('este camper ya se encuantra registrado')
                os.system('pause')
            else:
                isValueTrue= False
    nombre = str(input('ingrese el nombre del camper :')).lower()
    apellido = str(input('ingrese el apellido del camper :')).lower()
    direccion = str(input('ingrese la direccion del camper :')).lower()
    acudiente = str(input('quien es el acudiente del camper :')).lower()
    isValueTrue = True
    while isValueTrue:
        try: 
            nroCelular = int(input('ingrese el numero de celular del camper :'))
            nroFijo = int(input('ingrese el numero fijo del camper :'))
        except ValueError:
            print('el numero de celular/fijo no puede contener letras')
            os.system('pause')
        else:
            isValueTrue = False
    campus['campers'].update({
        identificacion: {
            'identificacion': identificacion, 
            'nombre': nombre, 
            'apellido': apellido, 
            'direccion': direccion, 
            'acudiente': acudiente, 
            'nroCelular': nroCelular, 
            'nroFijo': nroFijo, 
            'estado': 'inscrito'
        }
    })