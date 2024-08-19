import streamlit as st

st.title("Frequently Asked Questions")

# Define FAQ questions and answers
faqs = [
    {
        "question": "How accurate is the disease detection?",
        "answer": "The model is trained on a large dataset and has a high accuracy. However, it is always recommended to consult a professional for a more accurate diagnosis."
    },
    {
        "question": "Can I use this tool for any type of plant?",
        "answer": "The tool is currently trained on specific plant diseases. Please refer to the list of supported plants for more information."
    },
    {
        "question": "How do I upload an image?",
        "answer": "Navigate to the Diagnostic Tool section in the sidebar, and you will find an option to upload an image."
    }
]

# Style the FAQs
st.markdown("""
<style>
    .faq {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .faq h3 {
        margin: 0;
    }
    .faq p {
        margin: 5px 0;
    }
</style>
""", unsafe_allow_html=True)

# Display FAQs
for faq in faqs:
    st.markdown(f'<div class="faq"><h3>{faq["question"]}</h3><p>{faq["answer"]}</p></div>', unsafe_allow_html=True)
