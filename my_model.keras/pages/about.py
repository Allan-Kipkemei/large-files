import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Plant Disease Detection & Recommendations",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define your custom CSS styles
css = """
<style>
/* General Styles */
body {
    background-color: #f4f7f6;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #333;
}

/* Page Title */
.title {
    text-align: center;
    color: #2c3e50;
    font-size: 3rem;
    font-weight: 700;
    margin-top: 40px;
}

/* Header */
.header {
    text-align: center;
    color: #34495e;
    font-size: 2rem;
    margin-top: 20px;
    font-weight: 600;
}

/* Description Text */
.description {
    font-size: 1.2rem;
    color: #34495e;
    line-height: 1.8;
    text-align: justify;
    margin: 30px auto;
    max-width: 800px;
}

/* Key Features */
.features {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    margin: 30px auto;
    max-width: 900px;
}

.features h3 {
    color: #27ae60;
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 20px;
}

.features ul {
    list-style-type: disc;
    margin-left: 40px;
    color: #2c3e50;
}

.features ul li {
    margin-bottom: 10px;
    font-size: 1.1rem;
}

/* Contact Information */
.contact {
    font-size: 1.1rem;
    color: #555;
    margin: 30px auto;
    max-width: 800px;
}

.contact h3 {
    color: #2980b9;
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 20px;
}

.contact ul {
    list-style-type: none;
    padding-left: 0;
}

.contact ul li {
    margin-bottom: 10px;
    font-size: 1.1rem;
}

.contact ul li a {
    color: #2980b9;
    text-decoration: none;
}

.contact ul li a:hover {
    text-decoration: underline;
}

/* Button */
button {
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 10px 20px;
    font-size: 1rem;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
</style>
"""

# Inject CSS styles
st.markdown(css, unsafe_allow_html=True)

# Title and content with applied CSS classes
st.markdown('<div class="title">About Us</div>', unsafe_allow_html=True)
st.markdown('<div class="header">Welcome to the Plant Disease Detection and Recommendation System</div>', unsafe_allow_html=True)

st.markdown("""
<div class="description">
This system is designed to assist farmers, gardeners, and plant enthusiasts in identifying and managing plant diseases.
Leveraging state-of-the-art deep learning models trained on extensive datasets, the system offers precise disease detection and tailored recommendations.
Our goal is to enhance plant health and productivity through early diagnosis and effective treatments.
</div>
""", unsafe_allow_html=True)

st.image("https://example.com/path_to_image.jpg", caption="Plant Disease Detection", use_column_width=True)

st.markdown("""
<div class="features">
    <h3>Key Features</h3>
    <ul>
        <li>Accurate Disease Detection: Uses advanced machine learning algorithms to identify plant diseases from images.</li>
        <li>Detailed Recommendations: Provides actionable recommendations based on the detected disease.</li>
        <li>User-Friendly Interface: Easy-to-navigate web interface for quick access and efficient use.</li>
        <li>Regular Updates: Continuously updated with new data and recommendations to ensure accuracy and relevance.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="contact">
    <h3>Contact Us</h3>
    For more information or assistance, please reach out to us at:
    <ul>
        <li><strong>Email:</strong> <a href="mailto:support@example.com">support@example.com</a></li>
        <li><strong>Phone:</strong> (123) 456-7890</li>
        <li><strong>Website:</strong> <a href="http://www.example.com" target="_blank">www.example.com</a></li>
    </ul>
</div>
""", unsafe_allow_html=True)

if st.button('Learn More'):
    st.write("Thank you for your interest! We'll get back to you soon.")
