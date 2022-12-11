from keras.models import load_model
from PIL import Image, ImageOps 
import numpy as np
import streamlit as st

model = load_model('keras.h5', compile=False)

cheese_types = ['Blue Danish', 'Brie', 'Cottage', 'Feta', 'Parmesan']

data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
image = st.file_uploader("Upload a picture of cheese to classify", type=["png","jpg"])
if image:
   st.image(image)

   image = Image.open(image).convert('RGB')
   size = (224, 224)
   image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
   image_array = np.asarray(image)
   normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
   data[0] = normalized_image_array

   prediction = model.predict(data)
   index = np.argmax(prediction)


   st.write(cheese_types[index])
