import os

def Menu():
    os.system('cls')
    titulo="""
        +++++++++++++++++++++++++++++++++
        + SEGUIMIENTO ACADEMICO CAMPERS +
        +++++++++++++++++++++++++++++++++
    """
    print(titulo)
    menu= """
        1. Registrar candidato
        2. Realizar prueba de ingreso
        3. Registrar ruta
        4. Registrar trainer
        5. Gestor matriculas
        6. Realizar filtro
        7. reportes
        8. salir 
    """
    print(menu)
    try:
        op = int(input(')_'))
    except ValueError:
        print('no estas ingresando un numero')
        os.system('cls')
    else:
        return op
    
def MenuMatriculas():
    os.system('cls')
    titulo="""
        ++++++++++++++++++++++++
        + GESTOR DE MATRICULAS +
        ++++++++++++++++++++++++
    """
    print(titulo)
    menu= """
        1. Crear grupo
        2. Añadir estudiantes (cantidad)
        3. Salir
    """
    print(menu)
    try:
        op = int(input(')_'))
    except ValueError:
        print('no estas ingresando un numero')
        os.system('cls')
    else:
        return op

def MenuReportes():
    os.system('cls')
    titulo="""
        ++++++++++++++++++++
        + MENU DE REPORTES +
        ++++++++++++++++++++
    """
    print(titulo)
    menu= """
        1. Estudiantes inscritos
        2. Estudiantes que aprobaron Examen inicial
        3. Lista trainers
        4. Estudiantes con bajo rendimiento
        5. campers y entrenador asociados a una ruta
        6. aprobados y reprobados en modulo
        7. salir 
    """
    print(menu)
    try:
        op = int(input(')_'))
    except ValueError:
        print('no estas ingresando un numero')
        os.system('cls')
    else:
        return op