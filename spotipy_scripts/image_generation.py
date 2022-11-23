import settings
from model import train_model
#from tensorflow import keras
import keras_cv
import tensorflow as tf


def generate_image(description):
    if settings.first_call: 
        #settings.model = tf.keras.models.load_model('kcv_decoder.h5')
        tf.keras.mixed_precision.set_global_policy("mixed_float16")
        settings.model = keras_cv.models.StableDiffusion(jit_compile=True)
        settings.first_call = False
        print("model has been trained")
        ##image.save("image.png")
    image = settings.model.text_to_image(description, batch_size=1, num_steps=20)
    return image



