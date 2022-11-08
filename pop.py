import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

ImageAddress = 'pop/poppy.jpg'
ImageItself = Image.open(ImageAddress)
ImageNumpyFormat = np.asarray(ImageItself)
plt.imshow(ImageNumpyFormat)
plt.draw()
plt.pause(5) # pause how many seconds
plt.close()