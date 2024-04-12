import pandas as pd
#punto1
import numpy as np
matriz_4d = np.random.rand(30, 20, 10, 2000)  
print(matriz_4d.size)

#punto#2
matriz_3d = matriz_4d.copy().squeeze()  

#punto3
print("Dimensiones:", matriz_3d.ndim)
print("Forma:", matriz_3d.shape)
print("Tamaño:", matriz_3d.size)
#punto4
matriz_2d = matriz_3d.reshape(-1, matriz_3d.shape[-1])
#punto5 
def matriz_a_dataframe(matriz):
    return pd.DataFrame(matriz)
#punto6
import scipy.io

def cargar_matriz(file_path):
    return scipy.io.loadmat(file_path)

def cargar_csv(file_path):
    return pd.read_csv(file_path)
#punto7
def suma(matriz, axis=None):
    return np.sum(matriz, axis=axis)

def resta(matriz1, matriz2):
    return matriz1 - matriz2

def multiplicacion(matriz1, matriz2):
    return np.multiply(matriz1, matriz2)

def division(matriz1, matriz2):
    return np.divide(matriz1, matriz2)

def logaritmo(matriz):
    return np.log(matriz)

def promedio(matriz, axis=None):
    return np.mean(matriz, axis=axis)

def desviacion_estandar(matriz, axis=None):
    return np.std(matriz, axis=axis)
#punto8 
# Cargar el archivo CSV descargado previamente
dataframe_patologia = pd.read_csv("archivo_patologia.csv")
# ejemplo de como usar las funciones
def suma_pandas(dataframe, columnas):
    return dataframe[columnas].sum(axis=1)