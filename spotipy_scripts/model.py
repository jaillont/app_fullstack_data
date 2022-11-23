import keras_cv
def train_model():
    model = keras_cv.models.StableDiffusion(
        img_width=512,
        img_height=512,
        jit_compile=True
    )
    return model