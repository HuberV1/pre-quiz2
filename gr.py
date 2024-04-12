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
