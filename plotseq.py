# SCRIPT PARA LEER IMAGENES DE BRUKER NMR

import matplotlib.pyplot as plt
import numpy as np
from brukerapi.dataset import Dataset as ds

path = "../data/213-222/216/pdata/1/2dseq"
dataset = ds(path)
data = dataset.data

im = data[:,:,0,0] # los primeros dos indices corren sobre x e y, el tercero indexa el  
                   # slide (creo) y el cuarto el lugar en la secuencia.

fig, ax = plt.subplots()

ax.imshow(im, cmap="gray")
plt.show()