import os
import matplotlib.pyplot as plt
from tensorflow import keras

from stable_diffusion_tf.stable_diffusion import StableDiffusion


class GenerateImage:

    def __init__(self, request):
        self.request = request
        self.generator = self.create_model()

    def create_model(self):
        # Récupérer les paramètres
        height = int(os.environ.get("WIDTH", 640))
        width = int(os.environ.get("WIDTH", 640))
        mixed_precision = os.environ.get("MIXED_PRECISION", "no") == "yes"

        if mixed_precision:
            keras.mixed_precision.set_global_policy("mixed_float16")

        # Entrainement du model
        generator = StableDiffusion(img_height=height, img_width=width, jit_compile=True, download_weights=True)

        return generator


    def generate_images(self):

        description = 'album cover ' + self.request.POST['image_description'] + ' ' + self.request.POST['image_type'] + ' ' + self.request.POST['image_aspect']

        # Génération des images
        images = self.generator.generate(description, batch_size=3, num_steps=20, unconditional_guidance_scale=7.5, temperature=1,)

        # Sauvegarde des images
        for i in range(len(images)):
            plt.imsave('static/assets/img/buffer_cover/' + str(i)+self.request.POST['image_name']+'.jpeg',images[i])
