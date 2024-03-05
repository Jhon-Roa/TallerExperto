import os

def AddMatricula(campus: dict):
    os.system('cls')
    print('quien va a ser el trainer (ingresa la ID) ')
    ID = 1
    for key, values in campus['trainers'].items():
        nombre = values['nombre']
        Id = key
        print(f'{Id}. {nombre}')
    isValuetrue = True
    while isValuetrue:
        if len(campus['trainers']) == 0:
            print('no hay trainers, debes ingresar al menos uno')
            os.system('pause')
            return
        else:
            isValuetrue = False
    id = str(input(')_ '))
    if id in campus['trainers']:
        for values in campus['matricula'].values():
            if values['trainer'][0] == campus['trainers'][id]['nombre'][0]:
                ID += 1
        inicial = campus['trainers'][id]['nombre'][0].capitalize()
        nombreGrupo = (f'{inicial}{ID}')
        trainer = campus['trainers'][id]['nombre']
        campus['matricula'].update({nombreGrupo: {'trainer': {id: campus['trainers'][id]}}})
    else:
        print('este trainer no existe')
        os.system('pause')
        AddMatricula(campus)
        
    os.system('cls')
    
    print ('en que area se van a realizar las clases')
    for key in campus['areas']:
        print(key)
    isValuetrue = True
    while isValuetrue:
        area= str(input(')_'))
        if area in campus['areas']:
            isValuetrue = False
        else:
            print('ingresa un area valida')
            
    os.system('cls')
            
    print('en que horario deseas realizar las clases')
    for key in campus['areas'][area]['capacidad'].keys():
        print(key)
    isValuetrue = True
    while isValuetrue:
        horario= str(input(')_'))
        if horario in campus['areas'][area]['capacidad'].keys():
            for values in campus['matricula'].values():
                try:
                    horarios = values['horario']
                    areas = values['area']
                except KeyError:
                    if campus['trainers'][id]['horario']:
                        for item in campus['trainers'][id]['horario']:
                            if item == horario:
                                print('el trainer ya tiene este horario')
                                break
                            else:
                                campus['matricula'][nombreGrupo].update({'area': area, 'horario': horario})
                                campus['trainers'][id]['horario'].append(horario)
                                isValuetrue = False
                                break
                    else:
                        campus['matricula'][nombreGrupo].update({'area': area, 'horario': horario})
                        campus['trainers'][id]['horario'].append(horario)
                        isValuetrue = False
                        break
                else:
                    if horario == horarios and area == areas:
                        print('este horario ya esta en uso')
                        os.system('pause')
                        break
                    elif campus['trainers'][id]['horario']:
                        for item in campus['trainers'][id]['horario']:
                            if item == horario:
                                print('el trainer ya tiene este horario')
                                break
                            else:
                                campus['matricula'][nombreGrupo].update({'area': area, 'horario': horario})
                                campus['trainers'][id]['horario'].append(horario)
                                isValuetrue = False
                                break
                    else:
                        campus['matricula'][nombreGrupo].update({'area': area, 'horario': horario})
                        campus['trainers'][id]['horario'].append(horario)
                        isValuetrue = False
                        break
                    
                
        else:
            print('ingresa un horario valida')
    
    os.system('cls')
    
    print('que ruta deseas realizar')
    for key in campus['rutas']:
        print(key)
    isValuetrue= True
    while isValuetrue:
        ruta = str(input(')_'))
        if ruta in campus['rutas'].keys():
            campus['matricula'][nombreGrupo].update({'ruta': ruta})
            campus['matricula'][nombreGrupo].update({'estudiantes': {}})
            campus['matricula'][nombreGrupo].update({'limite': 0})
            campus['matricula'][nombreGrupo].update({'stack': '01'})
            campus['matricula'][nombreGrupo].update({'pRuta': 'fundamentos'})
            try:
                contenido = campus['matricula'][nombreGrupo]
                campus['rutas'][ruta]['fundamentos']['01'].update({nombreGrupo: contenido})
                isValuetrue = False
            except KeyError:
                print('aun no has ingresado rutas de entrenamiento en fundamentos')
                del(campus['matricula'][nombreGrupo])
                os.system('pause')
                return
        else:
            print('la ruta que ingresaste no existe')
            os.system('pause')
    
            

def AddMatriculaStudent(campus: dict):
    os.system('cls')
    
    Aprobados = {}
    for key, values in campus['campers'].items():
        if values['estado'] == 'aprobadoI':
            Aprobados.update({key: campus['campers'][key]})
    if len(Aprobados) == 0:
        print('no hay ningun estudiante para ingresar')
        return
            
    print('a que grupo quieres ingresar los estudiantes :')
    if campus['matricula']:
        for key in campus['matricula'].keys():
            print(key)
        isValueTrue = True
        while isValueTrue:
            grupo = str(input(')_')).upper()
            if grupo in campus['matricula'].keys():
                if campus['matricula'][grupo]['pRuta'] == 'fundamentos' and campus['matricula'][grupo]['stack'] == '01':
                    isValueTrue = False
                else:
                    print('el curso ya inicio \n no se pueden añadir mas estudiantes')
                    os.system('pause')
                    return
            else:
                print('el grupo que ingresaste no existe')
                
        print('ingrese cuantos campers desea asignar la ruta')
        isValueTrue = True
        while isValueTrue:
            try: 
                cantAprobados = len(Aprobados)
                print(f'la cantidad de estudiantes que puedezs ingresar es {cantAprobados}')
                cantidad = int(input(')_ '))
                limite = campus['matricula'][grupo]['limite'] 
                limite += cantidad
                area = campus['matricula'][grupo]['area']
                horario = campus['matricula'][grupo]['horario']
                ruta = campus['matricula'][grupo]['ruta']
            except ValueError:
                print('debe ser un numero entero')
                os.system('pause')
            else:
                if cantidad > 33:
                    print('la cantidad de campers que deseas ingresar, supera la capacidad del area')
                elif cantidad > len(Aprobados):
                    print('la cantidad de estudiantes que quieres ingresar es superior a la cantidad de aprobados')
                elif limite > campus['areas'][area]['capacidad'][horario]:
                    print(f'la cantidad de estudiantes que deseas ingresar supera el limite de {area}')
                else:
                    isValueTrue = False
        campus['matricula'][grupo]['limite'] += limite
        
        cantidadmax = 0
        for key in Aprobados.keys():
            cantidadmax += 1
            eGrupo = Aprobados[key].copy()
            campus['matricula'][grupo]['estudiantes'].update({key: eGrupo})
            campus['campers'][key]['estado']= 'matriculado'
            if cantidadmax == cantidad:
                break
        contenido= campus['matricula'][grupo].copy()
        campus['rutas'][ruta]['fundamentos']['01'].update({grupo: contenido})
        
    else:
        print('aun no hay grupos registrados')
        os.system('pause')
        return
