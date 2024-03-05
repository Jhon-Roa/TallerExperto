import os

def AddRuta(campus: dict):
    os.system('cls')
    print('seleccione la ruta a la que le va a añadir el stack')
    for key in campus['rutas']:
        print(f'{key}')
    isValueTrue = True
    while isValueTrue:
            op = str(input('ingrese la ruta :')).lower()
            if op in campus['rutas'].keys():
                isValueTrue= False
            else:
                print('la ruta que ingresaste no existe')
    os.system('cls')
    print('selecione a que parte de la ruta vas a añadir el stack')
    for key in campus['rutas'][op]:
        print(f'{key}')
    isValueTrue = True
    while isValueTrue:
            opI = str(input('ingrese la parte de la ruta :')).lower()
            if opI in campus['rutas'][op].keys():
                isValueTrue= False
            else:
                print('la parte de laruta que ingresaste no existe')
    if opI == 'bd':
        pass
    else:
        stack = str(input('ingresa el nombre del stack que quieres añadir :')).lower()
        myStack = {
            'id': str(len(campus['rutas'][op][opI])+1).zfill(2),
            'nombre': stack
        }
        campus['rutas'][op][opI].update({myStack['id']: myStack})
        os.system('pause')