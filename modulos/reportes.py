from tabulate import tabulate
import os

def ReporteInscritos(campus: dict):
    Inscritos = {}
    tabla = []
    for key, values in campus['campers'].items():
        if values['estado'] == 'inscrito':
            Inscritos.update({key: values})
    for key, values in Inscritos.items():
        os.system('cls')
        tabla.append(values)
        print(tabulate(tabla, headers='keys', tablefmt='grid'))
    os.system('pause')
    
def AprobadosInicial(campus: dict):
    aprobados = {}
    tabla = []
    for key, values in campus['campers'].items():
        if values['estado'] == 'aprobadoI' or values['estado'] == 'matriculado':
            aprobados.update({key: values})
    for key, values in aprobados.items():
        os.system('cls')
        tabla.append(values)
        print(tabulate(tabla, headers='keys', tablefmt='grid'))
    os.system('pause')
    
def ListaTrainers(campus: dict):
    tabla = []
    for key, values in campus['trainers'].items():
        os.system('cls')
        tabla.append(values)
        print(tabulate(tabla, headers='keys', tablefmt='grid'))
    os.system('pause')
    
def BajoRendimiento(campus: dict):
    eRiesgo = {}
    tabla = []
    for key in campus['matricula'].keys():
        for llave, valor in campus['matricula'][key]['estudiantes'].items():
            if valor['estado'] == 'riesgo' or valor['estado'] == 'riesgo_aprobado':
                eRiesgo.update({llave: valor})
    for key, values in eRiesgo.items():
        os.system('cls')
        tabla.append(values)
        print(tabulate(tabla, headers='keys', tablefmt='grid'))
    os.system('pause')
    
def AsociadoRuta(campus: dict):
    asociadoT = {}
    asociadoC = {}
    tablaT = []
    tablaC = []
    print ('selecciona la ruta')
    for key in campus['rutas'].keys():
        print(key)
    ruta = str(input(')_'))
    if ruta in campus['rutas'].keys():
        for key, values in campus['matricula'].items():
            if values['ruta'] == ruta:
                for key1, values1 in values['trainer'].items():
                    asociadoT.update({key1: values1})
                for key2, values2 in values['estudiantes'].items():
                    asociadoC.update({key2: values2})
        for key, values in asociadoT.items():
            os.system('cls')
            tablaT.append(values)
            print('triners asociados')
            print(tabulate(tablaT, headers='keys', tablefmt='grid'))
        os.system('pause')
        for key, values in asociadoC.items():
            os.system('cls')
            tablaC.append(values)
            print('campers asociados')
            print(tabulate(tablaC, headers='keys', tablefmt='grid'))
        os.system('pause')
    else:
        print('la ruta que ingresaste no existe')
        
def AproReproModulo(campus: dict):
    os.system('cls')
    aprobados= []
    reprobados= []
    grupo= {}
    
    print('en que ruta quieres ver los aprobados y reprobados')
    for key in campus['rutas'].keys():
        print(key)
    isValueTrue = True
    while isValueTrue:
        ruta = str(input(')_')).lower()
        if ruta in campus['rutas']:
            isValueTrue= False
        else:
            print('la ruta que ingresaste no existe')
            os.system('pause')

    os.system('cls')
    print('con que trainer (ingrese la id)')
    for key, values in campus['trainers'].items():
        nombre = values['nombre']
        print(f'{key}. {nombre}')
    isValueTrue = True
    while isValueTrue:
        idT = str(input(')_'))
        if idT in campus['trainers']:
            isValueTrue = False
        else:
            print('la id no esta asociada con ningun trainer')
            os.system('pause')
    
    for key, values in campus['matricula'].items():
        for keyC in values['trainer'].keys():
            idTC = keyC
        if values['ruta'] == ruta and  idTC == idT:
            for key1, values1 in campus['rutas'][ruta].items():
                for key2, values2 in campus['rutas'][ruta][key1].items():
                    aprobados= []
                    reprobados= []
                    confirm = dict(values1[key2][key]['estudiantes'])
                    for key3, values3 in confirm.items():
                        if values3['estado'] != 'reprobado':
                            aprobados.append(key)
                        else:
                            reprobados.append(key)
                    nombreModulo= values2['nombre']
                    if aprobados or reprobados:
                        largoA = len(aprobados)
                        largoR = len(reprobados)
                        print(f'en la ruta {ruta}, modulo {nombreModulo} aprobaron {largoA} estudiantes')
                        print(f'en la ruta {ruta}, modulo {nombreModulo} reprobaron {largoR} estudiantes')
                        os.system('pause')
                    else:
                        print(f'no se ha realizado el filtro del modulos {nombreModulo} en ningun grupo')
                        os.system('pause')