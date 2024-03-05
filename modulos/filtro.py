import os

def Filtro(campus: dict):
    os.system('cls')
    print('a que grupo deseas realizar el filtro')
    if campus['matricula']:
        for key in campus['matricula']:
            print(key)
        isValueTrue = True
        while isValueTrue:
            grupo = str(input(')_')).upper()
            if grupo in campus['matricula']:
                if campus['matricula'][grupo]:
                    isValueTrue = False
                else:
                    print('este grupo no tiene estudiantes')
                    os.system('pause')
                    return
            else:
                print('el grupo que ingresaste no existe')
        if campus['matricula'][grupo]['estudiantes']:
            grupoM = campus['matricula'][grupo]
            if grupoM['pRuta']  != 'finalizado':
                ruta = grupoM['ruta']
                pRuta = grupoM['pRuta']
                stack = grupoM['stack']
                grupoR = campus['rutas'][ruta][pRuta][stack][grupo]
                for key, values in grupoR['estudiantes'].items():
                    os.system('cls')
                    nombre = values['nombre']
                    apellido = values['apellido']
                    identificacion = values['apellido']
                    print(f'camper: {nombre} {apellido} con identificacion {identificacion}')
                    isValueTrue = True
                    while isValueTrue:
                        try:
                            teorica = int(input('ingrese una nota teorica :'))
                            practica = int(input('ingrese una nota practica :'))
                            trabajos = int(input('ingrese la nota obtenida del promedio de trabajos :'))
                        except ValueError:
                            print('una de las notas que estas ingresando no es un numero entero')
                            os.system('pause')
                        else:
                            if teorica > 100 or teorica < 0 or practica > 100 or practica < 0 or trabajos > 100 or teorica < 0:
                                print('una de las notas que estas ingresando es o mayor que 100 o menor que 0')
                                os.system('pause')
                            else:
                                if grupoR['stack'] == stack:
                                    notaF = (teorica * 0.30) + (practica * 0.60) + (trabajos * 0.10)
                                    if notaF < 60 and grupoM['estudiantes'][key]['estado'] == 'riesgo' or grupoM['estudiantes'][key]['estado'] == 'riesgo_aprobado':
                                        grupoM['estudiantes'][key].update({'estado': 'reprobado'})
                                        grupoR['estudiantes'][key].update({'estado': 'reprobado'})
                                    elif notaF >= 60 and grupoM['estudiantes'][key]['estado'] == 'riesgo' or grupoM['estudiantes'][key]['estado'] == 'riesgo_aprobado':
                                        grupoM['estudiantes'][key].update({'estado': 'riesgo_aprobado'})
                                        grupoR['estudiantes'][key].update({'estado': 'riesgo_aprobado'})
                                    elif notaF >= 60:
                                        grupoM['estudiantes'][key].update({'estado': 'aprobado'})
                                        grupoR['estudiantes'][key].update({'estado': 'aprobado'})
                                    elif notaF < 60:
                                        grupoM['estudiantes'][key].update({'estado': 'riesgo'})
                                        grupoR['estudiantes'][key].update({'estado': 'riesgo'})
                                isValueTrue = False
                os.system('cls')
                print('filtro realizado')
                os.system('pause')
                
                isValueTrue = True
                while isValueTrue:
                    stackI = int(grupoM['stack'])
                    stackI += 1
                    stack = str(stackI).zfill(2)
                    grupoM['stack'] = stack
                    grupoR['stack'] = stack
                    stack = grupoR['stack']
                    pRuta = grupoR['pRuta']
                    contenido= grupoR.copy()
                    try:
                        campus['rutas'][ruta][pRuta][stack].update({grupo: contenido})
                    except KeyError:
                        if grupoR['pRuta'] == 'fundamentos':
                            grupoR['pRuta'] = 'web'
                            grupoR['stack'] = '00'
                            grupoM['pRuta'] = 'web'
                            grupoM['stack'] = '00'
                        elif grupoR['pRuta'] == 'web':
                            grupoR['pRuta'] = 'lengformal'
                            grupoR['stack'] = '00'
                            grupoM['pRuta'] = 'lengformal'
                            grupoM['stack'] = '00'
                        elif grupoR['pRuta'] == 'lengformal':
                            grupoR['pRuta'] = 'bd'
                            grupoR['stack'] = '00'
                            grupoM['pRuta'] = 'bd'
                            grupoM['stack'] = '00'
                        elif grupoR['pRuta'] == 'bd':
                            grupoR['pRuta'] = 'backend'
                            grupoR['stack'] = '00'
                            grupoM['pRuta'] = 'backend'
                            grupoM['stack'] = '00'
                        elif grupoR['pRuta'] == 'backend':
                            grupoR['pRuta'] = 'finalizado'
                            grupoR['stack'] = 'finalizado'
                            grupoM['pRuta'] = 'finalizado'
                            grupoM['stack'] = 'finalizado'
                            print('ruta finalizada')
                            os.system('pause')
                            return
                    else:
                        isValueTrue= False
                eAprobadosR = {}
                eAprobadosM = {}
                for key, values in grupoR['estudiantes'].items():
                    if values['estado'] != 'reprobado':
                        values_copy= values.copy()
                        eAprobadosR.update({key: values_copy})
                        eAprobadosM.update({key: values_copy})
                del(grupoR['estudiantes'])
                grupoR.update({'estudiantes': eAprobadosR})
                grupoM.update({'estudiantes': eAprobadosM})
            else:
                print('este grupo ya finalizo')
                os.system('pause')
                return
        else:
            print('aun no has ingresado estudiantes')
            os.system('pause')
            return
    else:
        print('no hay grupos existentes')
        os.system('pause')
        return