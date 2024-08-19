from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from PIL import Image
import numpy as np
import json

# Recreate the Model Architecture with Correct Output Layer
def create_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(39, activation='softmax')  # Adjust this number to match your model's output classes
    ])
    return model

def load_weights(model, weights_path):
    try:
        model.load_weights(weights_path)
        print("Weights loaded successfully.")
    except ValueError as e:
        print("Error loading weights:", e)

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))  # Resize to match model's input shape
    image = np.array(image) / 255.0  # Convert to numpy array and normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

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
    ]  # List of class names in the same order as model output
    predicted_label = class_labels[predicted_class[0]]
    print("Predicted class:", predicted_label)
    return predicted_label

def load_recommendations(json_path):
    with open(json_path, 'r') as f:
        recommendations = json.load(f)
    return recommendations

def get_recommendation(predicted_label, recommendations):
    if predicted_label in recommendations:
        return recommendations[predicted_label]
    else:
        return {"Description": "No recommendations available for this class."}

if __name__ == "__main__":
    weights_path = './model.weights.h5'
    image_path = './image (35).JPG'
    json_path = './PlantVillageRecommendations.json'

    model = create_model()
    model.summary()  # Print model summary to verify architecture
    load_weights(model, weights_path)

    preprocessed_image = preprocess_image(image_path)
    predicted_label = predict_image(model, preprocessed_image)

    recommendations = load_recommendations(json_path)
    recommendation = get_recommendation(predicted_label, recommendations)

    print("Recommendation based on prediction:")
    print(json.dumps(recommendation, indent=4))
