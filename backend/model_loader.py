# backend/model_loader.py

import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("../model/trained_models/aptos_dr_model.keras")

def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def predict(image):
    img = preprocess_image(image)
    preds = model.predict(img)

    class_index = np.argmax(preds)

    return str(class_index)