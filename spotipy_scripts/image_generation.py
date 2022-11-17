import settings
from model import train_model
def generate_image(description):
    if settings.first_call: 
        settings.model = train_model()
        settings.first_call = False
        print("model has been trained")
        ##image.save("image.png")
    image = settings.model.text_to_image(description, batch_size=1)
    return image



