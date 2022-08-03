# Lectura, parseo y muestreo por consola del contenido de un JSON

import json

file = open('resources\personas.json','r')
file = json.loads(file.read())

print(f'Son {len(file)} personas')
print('*' * 20)

for dato in file:
    print('ID:', dato['_id'])
    print('Nombre:', dato['name'])
    print('País:', dato['country'])
    print('Edad:', dato['age'])
    print('-' * 10)