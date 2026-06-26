from PIL import Image
import numpy as np
array = np.array(Image.open("screenshot_2026-03-23_10-41-14.png"))

invert = 90 - array

Image.fromarray(np.rot90(invert)).save("in.png")