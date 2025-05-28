import streamlit as st
import spacy
from spacy import displacy

st.title("Lake Entity Recognition App 🌊")
st.write("Test your custom SpaCy model for recognizing lake-related entities.")

# Initialisation dans session_state
if "nlp" not in st.session_state:
    st.session_state.nlp = None

model_path = st.text_input("Model path (e.g., ./my_model):", "./my_model")

if st.button("Load Model"):
    try:
        st.session_state.nlp = spacy.load(model_path)
        st.success("Model loaded successfully!")
    except Exception as e:
        st.error(f"Failed to load model: {e}")

if st.session_state.nlp:
    text_input = st.text_area("Enter text to analyze:", "Lake Victoria is located in Tanzania near Owen Falls.")

    if st.button("Analyze"):
        doc = st.session_state.nlp(text_input)

        st.subheader("Named Entities:")
        if doc.ents:
            for ent in doc.ents:
                st.markdown(f"- **{ent.text}** ({ent.label_})")
        else:
            st.write("No entities found.")

        # Affichage des entités surlignées
        html = displacy.render(doc, style="ent", jupyter=False)
        st.markdown(html, unsafe_allow_html=True)
