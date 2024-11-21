import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import json
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="RecycleVision AI",
    page_icon="♻️",
    layout="wide"
)

# Function to classify items
def classify_item(image):
    """Quick classification of recyclable items"""
    try:
        # Convert image to RGB and resize
        image = image.convert('RGB')
        image = image.resize((224, 224))
        
        # Convert to numpy array and normalize
        img_array = np.array(image) / 255.0
        
        # Simple color-based classification
        avg_color = np.mean(img_array, axis=(0, 1))
        brightness = np.mean(avg_color)
        
        # Simple classification rules
        if brightness > 0.7:  # Light colored items
            return "Recyclable", "Paper/Cardboard", 0.85
        elif brightness < 0.3:  # Dark items
            return "Recyclable", "Plastic", 0.75
        else:  # Medium brightness
            return "Recyclable", "Metal/Glass", 0.80
            
    except Exception as e:
        st.error(f"Error in classification: {str(e)}")
        return "Unknown", "Error", 0.0

# Function to show results
def show_results(predicted_class, material_type, confidence):
    st.markdown(f"### Results")
    st.markdown(f"**Classification:** {predicted_class}")
    st.markdown(f"**Material Type:** {material_type}")
    st.markdown(f"**Confidence:** {confidence*100:.1f}%")
    
    # Add recycling instructions
    if predicted_class == "Recyclable":
        st.markdown("### Recycling Instructions:")
        st.markdown("""
        1. Clean the item
        2. Remove any non-recyclable parts
        3. Place in appropriate recycling bin
        """)
    else:
        st.markdown("### Disposal Instructions:")
        st.markdown("Please dispose of this item in regular waste.")

# Title and description
st.title("♻️ RecycleVision AI")
st.markdown("""
    Identify recyclable items using AI! Choose whether to upload an image or take a photo.
""")

# Create two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### Choose Input Method")
    input_choice = st.radio("Select how you want to provide the image:", 
                           ["Upload an Image", "Take a Photo"])
    
    if input_choice == "Upload an Image":
        uploaded_file = st.file_uploader("Upload your image here", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            
            if st.button("Analyze Image"):
                with col2:
                    st.markdown("### Analysis Results")
                    # Immediate classification
                    predicted_class, material_type, confidence = classify_item(image)
                    show_results(predicted_class, material_type, confidence)
    
    else:  # Take a Photo option
        camera_photo = st.camera_input("Take a photo")
        if camera_photo is not None:
            image = Image.open(camera_photo)
            st.image(image, caption="Captured Photo", use_container_width=True)
            
            if st.button("Analyze Photo"):
                with col2:
                    st.markdown("### Analysis Results")
                    # Immediate classification
                    predicted_class, material_type, confidence = classify_item(image)
                    show_results(predicted_class, material_type, confidence)

with col2:
    if 'image' not in locals():
        st.markdown("### Results will appear here")
        st.write("Upload an image or take a photo to see the analysis")