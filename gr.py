#punto1
import numpy as np
matriz_4d = np.random.rand(30, 20, 10, 2000)  
print(matriz_4d.size)

#punto#2
matriz_3d = matriz_4d.copy().squeeze()  

