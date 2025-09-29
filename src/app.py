import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Load the model
model = tf.keras.models.load_model('model.h5')



# Preprocessing function
def preprocess_image(image):
    image = image.resize((128, 128))  
    image = np.array(image) / 255.0   
    image = np.expand_dims(image, axis=0)  
    return image

# Streamlit UI
st.title("🐶🐱 Pet Classifier: Cat or Dog?")
st.markdown("#### Powered by [@najuvgz](https://github.com/najuvgz)")
st.write("Upload an image of your pet and let the AI decide!")

uploaded_file = st.file_uploader("📁 Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_container_width=True)

    st.write("🔍 Classifying...")
    processed_image = preprocess_image(image)
    

    prediction = model.predict(processed_image)
    predicted_class = np.argmax(prediction[0])  
   
    labels = ["Cat 🐱", "Dog 🐶"]  
    label = labels[predicted_class]
    confidence = prediction[0][predicted_class]

    st.success(f"🎉 It's a {label} with {confidence:.2%} confidence!")

