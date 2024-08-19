import streamlit as st

# Set the page title and favicon
st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿"
)

# Add a title with an emoji and custom styling
st.title("🌿 Welcome to the Plant Disease Detection and Recommendation System")

# Add a subtitle and some descriptive text with Markdown
st.markdown("""
**Welcome to our advanced Plant Disease Detection and Recommendation System!** 🌱

This tool is designed to help you:

- **Upload images** of plant leaves.
- **Get precise disease predictions** from the images.
- **Receive comprehensive recommendations** for treatment and prevention.

### How It Works:
1. **Navigate** to the **Diagnostic Tool** section.
2. **Upload** an image of a plant leaf.
3. **Receive predictions** and actionable recommendations instantly.

We aim to support you in keeping your plants healthy and thriving. Explore the features and take advantage of our tool to maintain the best care for your plants.

For any questions or additional help, check out the [FAQs](#) or contact us through the [Contact](#) page.

**Let's get started and ensure your plants are always in their best shape!** 🌟
""", unsafe_allow_html=True)

# Optionally, include a relevant image or logo
st.image("path_to_your_image_or_logo.png", caption="Your Plant Disease Detection Tool", use_column_width=True)

# Optionally, include a button to start using the diagnostic tool
if st.button("Go to Diagnostic Tool"):
    st.write("Redirecting you to the Diagnostic Tool...")
    # Add a redirect or navigation to the diagnostic tool page if needed
    # Note: Streamlit does not support direct redirection; you can use navigation if implemented in a multi-page app.
