import modulos.menu as me
import modulos.registro as re
import modulos.ruta as rut
import modulos.prueba_ingreso as pi
import modulos.trainer as tr
import modulos.matriculas as ma 
import modulos.filtro as fi
import modulos.reportes as rep

campus = {
    'campers': {},
    'rutas': {
        'java': {
            'fundamentos': {},
            'web': {},
            'lengformal': {},
            'bd': {},
            'backend': {},
            },
        'nodejs': {
            'fundamentos': {},
            'web': {},
            'lengformal': {},
            'bd': {},
            'backend': {},
            },
        'netcore': {
            'fundamentos': {},
            'web': {},
            'lengformal': {},
            'bd': {},
            'backend': {},
            },
        },
    'areas': {
        'apolo': {
            'nombre': 'apolo',
            'capacidad': {
                '06:00': 33,
                '10:00': 33,
                '14:00': 33,
                '18:00': 33
                }
            },
        'sputnik': {
            'nombre': 'sputnik',
            'capacidad': {
                '06:00': 33,
                '10:00': 33,
                '14:00': 33,
                '18:00': 33
                }
            },
        'artemis': {
            'nombre': 'apolo',
            'capacidad': {
                '06:00': 33,
                '10:00': 33,
                '14:00': 33,
                '18:00': 33
                }
            }
        },
    'trainers': {},
    'matricula': {}
}

if __name__ == "__main__":
    IssAppRunning = True
    while IssAppRunning:
        op = me.Menu()
        if op == 1:
            re.Registro(campus)
        elif op == 2:
            pi.PruebaIngreso(campus)
        elif op == 3:
            rut.AddRuta(campus)
        elif op == 4:
            tr.AddTrainer(campus)
        elif op == 5:
            isValueTrue = True
            while isValueTrue:
                op = me.MenuMatriculas()
                if op == 1:
                    ma.AddMatricula(campus)
                elif op == 2:
                    ma.AddMatriculaStudent(campus)
                elif op == 3:
                    isValueTrue = False
                elif op > 4:
                    print('el valor ingresado no esta entre las opciones')
                    ma.os.system('pause')
        elif op == 6:
            fi.Filtro(campus)
        elif op == 7:
            isValueTrue = True
            while isValueTrue:
                op = me.MenuReportes()
                if op == 1:
                    rep.ReporteInscritos(campus)
                elif op == 2:
                    rep.AprobadosInicial(campus)
                elif op == 3:
                    rep.ListaTrainers(campus)
                elif op == 4:
                    rep.BajoRendimiento(campus)
                elif op == 5:
                    rep.AsociadoRuta(campus)
                elif op == 6:
                    rep.AproReproModulo(campus)
                elif op == 7:
                    isValueTrue = False
                elif op == 8:
                    print('el valor ingresado no esta entre las opciones')
                    ma.os.system('pause')
        elif op == 8:
            IssAppRunning = False
        else:
            print('estas ingresando un valor por fuera de las opciones')
            ma.os.system('pause')
        