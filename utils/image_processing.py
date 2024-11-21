import tensorflow as tf
import numpy as np

def preprocess_image(image):
    """Preprocess image for model prediction"""
    # Resize image to 224x224 (standard size for many models)
    img = image.resize((224, 224))
    
    # Convert to array and normalize
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array = img_array / 255.0
    
    return img_array

def get_prediction(model, image):
    """Get prediction for image"""
    # Class names for our model
    class_names = ['Recyclable', 'Non-Recyclable', 'Organic']
    
    # Make prediction
    predictions = model.predict(image)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))
    
    return predicted_class, confidence