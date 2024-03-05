import os

def AddTrainer(campus: dict):
    os.system('cls')
    titulo= """
        ++++++++++++++++++
        + AÑADIR TRAINER +
        ++++++++++++++++++
    """
    print(titulo)
    nombre = str(input('ingrese el nombre de el trainer :')).lower()
    ID = str(len(campus['trainers']) + 1).zfill(2)
    campus['trainers'].update({ID: {'id': ID, 'nombre' : nombre, 'horario': []}})
    