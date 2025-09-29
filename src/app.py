import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model
model = tf.keras.models.load_model('model.h5')

# Preprocessing function
def preprocess_image(image):
    image = image.resize((224, 224))  # Match your model's input size
    image = np.array(image) / 255.0   # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Streamlit UI
st.title("🐶🐱 Pet Classifier: Cat or Dog?")
st.write("Upload an image of your pet and let the AI decide!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)

    st.write("Classifying...")
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)

    # Assuming output is a single sigmoid value: closer to 1 = Dog, closer to 0 = Cat
    label = "Dog 🐶" if prediction[0][0] > 0.5 else "Cat 🐱"
    confidence = prediction[0][0] if label == "Dog 🐶" else 1 - prediction[0][0]
    st.success(f"It's a {label} with {confidence:.2%} confidence!")
