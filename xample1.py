estudiantes = [
    { 140721: {
        'nombre': 'Juan Perez',
        'direccion': 'Cra 81 #12-15',
        'telefono': [3392015, 3008102148, 3181014819],
        'correo': ['jperez@hotmail.co', 'juanp@gmail.com'],
        'programa': 'sistemas',
        'semestre': 6,
        'materias': [
           {'nombre': 'Calculo V', 'p1': 2.8, 'p2': 3.1, 'p3':3.6, 'def': 0.0},
           {'nombre': 'Fisica III', 'p1': 3.1, 'p2': 3.5, 'p3':3.1, 'def': 0.0},
           {'nombre': 'Base de Datos', 'p1': 4.0, 'p2': 3.9, 'p3':4.3, 'def': 0.0},
           {'nombre': 'Desarrollo Web', 'p1': 4.8, 'p2': 4.5, 'p3':4.1, 'def': 0.0},
           {'nombre': 'Arquitectura de Computadores', 'p1': 3.2, 'p2': 4.0, 'p3':3.5, 'def': 0.0}
        ]
      }
    },
    { 140831: {
        'nombre': 'Maria Lopez',
        'direccion': 'Cll 38 #25-91',
        'telefono': [4411512, 311483419],
        'correo': ['marialo@hotmail.es', 'lopezm@gmail.com'],
        'programa': 'industrial',
        'semestre': 4,
        'materias': [
           {'nombre': 'Calculo II', 'p1': 2.8, 'p2': 2.1, 'p3':3.6, 'def': 0.0},
           {'nombre': 'Fisica I', 'p1': 3.1, 'p2': 2.5, 'p3':2.1, 'def': 0.0},
           {'nombre': 'Procesos', 'p1': 3.0, 'p2': 3.0, 'p3':3.0, 'def': 0.0},
           {'nombre': 'Metodos y Tiempos', 'p1': 2.8, 'p2': 1.5, 'p3':1.1, 'def': 0.0},
           {'nombre': 'Diseno de Procesos', 'p1': 3.7, 'p2': 2.0, 'p3':3.1, 'def': 0.0}
        ]
      }
    }
]

for estudiante in estudiantes:
    codigo, datos = estudiante.popitem()
    print(datos['nombre'])
    tot_mat = 0
    cont_mat = 0
    for materia in datos['materias']:
        materia['def'] = 0.3*materia['p1'] + 0.3*materia['p2'] +0.4 *materia['p3']
        tot_mat += materia['def']
        cont_mat += 1
        print('{}: {:.2}'.format(materia['nombre'], materia['def']))
    prom_est = tot_mat / cont_mat
    print('promedio: {:.2}'.format(prom_est))
    print()