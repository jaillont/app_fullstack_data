import settings
import matplotlib.pyplot as plt
from image_generation import generate_image
settings.init()

def image(description,filename):
    im = generate_image(description)
    plt.imsave(''+filename+'.png',im[0])

print(settings.first_call)