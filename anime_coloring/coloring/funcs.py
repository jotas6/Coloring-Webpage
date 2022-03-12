import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def obtener_imagen(nombre_archivo):

    imagen = Image.open(nombre_archivo)

    return np.array(imagen)/255

def ver_imagen(imagen):
    
    plt.style.use("default")
    plt.imshow(imagen)
    plt.axis("off")
    plt.show()

def transforma_color_base(color_base, resta):

    iter = ((color_base[i] - resta) if(color_base[i] - resta > 0) else(0) for i in range(3))
    color = np.fromiter(iter, dtype=float)

    return color

def cambia_color_base(nombre_archivo, color_base, umbral = 0.9, directo = True):
    
    """La imagen debe estar en formato .jpg"""

    """Directo = False hace que el coloreado haga de forma invertida. Las partes oscuras del original
    apareceran más claras y las partes claras del original aparecerán más oscuras"""

    """El umbral se puede ajustar manualmente, pero si no se especifica toma el valor de 0.9
    A este parámetro se le debe dar un valor entre 0 y 1 y cuánto más alto sea más oscura parecerá
    la imagen"""
    
    imagen = obtener_imagen(nombre_archivo)

    filas = np.size(imagen, 0)
    columnas = np.size(imagen, 1)
    
    lienzo = np.full((filas, columnas, 3), np.array([1.0,1.0,1.0]))
    
    for i in range(filas):
        
        for j in range(columnas):
            
            promedio = np.mean(imagen[i,j])
            resta = (-umbral*promedio) + umbral
            
            if(directo == False):
                
                resta = umbral*promedio
                
            color = transforma_color_base(color_base, resta)
            lienzo[i,j] = color
            
    return lienzo

def f_bn(x, y, z):

    """
    if(z == 0):

        return np.mean([z, z+1, z+2])

    elif(z == 1):

        return np.mean([z-1, z, z+1])

    else:

        return np.mean([z-2, z-1, z])
    """
    return np.mean(z)

def blanco_negro(nombre_archivo):
    
    imagen = obtener_imagen(nombre_archivo)

    filas = np.size(imagen, 0)
    columnas = np.size(imagen, 1)
    imagen = np.reshape(imagen, filas*columnas*3)
    lienzo = np.copy(imagen)

    for i in range(0, np.size(imagen)-3, 3):

        lienzo[i:i+3] = np.mean(imagen[i:i+3])

    lienzo = np.reshape(lienzo, (filas, columnas, 3))
    
    return lienzo

def cambia_fondo(nombre_archivo, color_fondo, umbral = 0.45):
    
    imagen = obtener_imagen(nombre_archivo)

    filas = np.size(imagen, 0)
    columnas = np.size(imagen, 1)

    imagen_fondo = np.full((filas, columnas, 3), color_fondo)
    imagen_transformada = np.full((filas, columnas, 3), np.array([1.0,1.0,1.0]))

    for i in range(filas):
    
        for j in range(columnas):
                   
            color_promedio = np.mean(imagen[i,j])

            if(color_promedio < umbral):
            
                imagen_transformada[i,j] = imagen[i,j]
            
            else:
            
                imagen_transformada[i,j] = imagen_fondo[i,j]
            
    return imagen_transformada

def hex_to_rgb(value):
    value = value.lstrip('#')
    return list(int(value[i:i+2], 16) for i in (0, 2, 4))
