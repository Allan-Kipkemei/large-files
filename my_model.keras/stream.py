import streamlit as st
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from PIL import Image
import numpy as np
import json

# Function to create the model
def create_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(39, activation='softmax')
    ])
    return model

# Function to load model weights
def load_weights(model, weights_path):
    model.load_weights(weights_path)

# Function to preprocess the uploaded image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Function to make predictions
def predict_image(model, preprocessed_image):
    prediction = model.predict(preprocessed_image)
    predicted_class = np.argmax(prediction, axis=1)
    class_labels = [
        "Apple___Apple_scab",
        "Apple___Black_rot",
        "Apple___Cedar_apple_rust",
        "Apple___healthy",
        "Background_without_leaves",
        "Blueberry___healthy",
        "Cherry___Powdery_mildew",
        "Cherry___healthy",
        "Corn___Cercospora_leaf_spot Gray_leaf_spot",
        "Corn___Common_rust",
        "Corn___Northern_Leaf_Blight",
        "Corn___healthy",
        "Grape___Black_rot",
        "Grape___Esca_(Black_Measles)"
    ]
    predicted_label = class_labels[predicted_class[0]]
    return predicted_label

# Function to load recommendations
def load_recommendations(json_path):
    with open(json_path, 'r') as f:
        recommendations = json.load(f)
    return recommendations

# Function to get recommendation based on prediction
def get_recommendation(predicted_label, recommendations):
    return recommendations.get(predicted_label, {"Description": "No recommendations available for this class."})

# Main function to run the app
def main():
    st.title("Plant Disease Detection and Recommendation System")

    # Home Section
    st.header("Home")
    st.write("Welcome to the Plant Disease Detection and Recommendation System. Upload an image of a plant and get immediate recommendations for potential diseases.")

    # About Section
    st.header("About")
    st.write("This app helps in detecting plant diseases based on images and provides actionable recommendations to treat or manage the diseases.")

    # Diagnostic Tool Section
    st.header("Diagnostic Tool")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

        # Load the model and weights
        model = create_model()
        load_weights(model, './model.weights.h5')

        # Preprocess the image and make a prediction
        preprocessed_image = preprocess_image(image)
        predicted_label = predict_image(model, preprocessed_image)

        # Load the JSON file with recommendations
        recommendations = load_recommendations('./PlantVillageRecommendations.json')
        recommendation = get_recommendation(predicted_label, recommendations)

        # Display the prediction and recommendations
        st.subheader(f"Predicted class: {predicted_label}")
        st.subheader("Recommendation:")
        st.write(f"**Description:** {recommendation['Description']}")
        st.write(f"**Diagnosis:** {recommendation['Diagnosis']}")
        st.write(f"**Recommended Action:** {recommendation['Recommended_Action']}")
        st.write(f"**Treatment:** {recommendation['Treatment']}")
        st.write(f"**Treatment Timing:** {recommendation['Treatment_Timing']}")
        st.write(f"**Prevention:** {recommendation['Prevention']}")
        st.write(f"**Monitoring:** {recommendation['Monitoring']}")
        st.write(f"**Cultural Practices:** {recommendation['Cultural_Practices']}")
        st.write(f"**Physical Controls:** {recommendation['Physical_Controls']}")
        st.write(f"**Biological Controls:** {recommendation['Biological_Controls']}")

    # FAQs Section
    st.header("FAQs")
    st.write("""
    **Q: How accurate is the plant disease detection?**
    A: The accuracy depends on the quality of the image and the variety of diseases in the dataset.

    **Q: Can this app detect all types of plant diseases?**
    A: The app is trained on a specific dataset, so it may not cover all possible plant diseases.

    **Q: How can I improve the accuracy of detection?**
    A: Ensure that the uploaded image is clear, focused, and captures the relevant parts of the plant.
    """)

    # Contact Section
    st.header("Contact")
    st.write("""
    If you have any questions or feedback, feel free to contact us at:

    **Email:** support@plantdiseaseapp.com
    **Phone:** +123-456-7890
    """)

if __name__ == "__main__":
    main()
