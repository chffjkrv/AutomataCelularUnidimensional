import numpy as np
# Esta es una librería que renta para generar barras de progreso
# en la terminal, en el bucle que se quiera:
from tqdm import tqdm
import matplotlib.pyplot as plt

# Función para iterar una vez la línea de celdas
def iterate(rule, line):
    # Convierte la regla de un número en base 10 a una representación string
    # de un número en binario y con 8 digitos siempre (añade ceros por delante
    # si es necesario):
    rule = f'{rule:08b}'[::-1]
    # Topología cilíndrica. Expando la línea añadiendo al principio el final
    # y al final el principio:
    line_wraped = line[-1]+line+line[0]
    new_line = []
    for i in range(len(line_wraped)-2):
        # line_wraped[i:i+3] examina el estado binario de la celda y sus dos
        # vecinos, luego convierte ese string de tres dígitos binarios en un
        # número en base 10 con int( , 2), y finalmente busca la respuesta ante
        # dicha triada de valores en rule (cuyo indice n-ésimo se corresponde
        # a la respuesta de la celda ante la situación n-ésima escrita en binario).
        new_line.append(rule[int(line_wraped[i:i+3],2)])
    return ''.join(new_line)

# Función que evoluciona el autómata celular en el tiempo y
# guarda todo el desarrollo en una matriz, m.
def create_matrix(rule, first_line, num_it):
    m = np.zeros((num_it+1, len(first_line)))
    m[0] = np.array(list(first_line)).astype(int)
    line = first_line
    for i in range(1, num_it+1):
        line = iterate(rule, line)
        m[i] = np.array(list(line)).astype(int)
    return m

# Función para plotear la matrix resultante como una imagen y guardarla a cierta resolución.
def create_picture(name, matrix, resolution):
    plt.style.use('dark_background')    # Fondo negro y ejes en blanco
    plt.imshow(matrix, cmap = 'gray')   # Convertir matriz en imagen según una escala de grises (0 es negro y 1 es blanco)
    # Eliminar ejes, marcas y letreros de los ejes
    plt.xticks([])
    plt.yticks([])
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    # Guardar imagen en png
    plt.savefig(name+'.png', format = 'png', dpi = resolution, bbox_inches = 'tight', pad_inches = 0)
    plt.cla() # Limpiar de la memoria la figura para no ir lastrando si se hacen muchas

w = 100 # Numero de celdas en la primera línea (anchura de la imagen)
h = 80  # Número de iteraciones (altura de la imagen)

# Estados iniciales (primera línea escrita como un string de 0s y 1s)
init_states = ''.join(np.random.choice(['0', '1'], w)) # Estado inicial aleatorio
# init_states = '0'*int(w/2)+'1'+'0'*int(w/2)          # Estado inicial de todo ceros excepto un 1 en el centro

# Bucle para generar una galería de imágenes con todas las reglas
for i in tqdm(range(2**8), leave = False):
    m = create_matrix(i, init_states, h)
    create_picture('Rule_'+str(i).rjust(3, '0'), m, 300)
