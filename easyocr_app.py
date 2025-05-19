import streamlit as st
import easyocr
from PIL import Image
import numpy as np

st.title("🧠 OCR con EasyOCR y Streamlit")
archivo = st.file_uploader("Sube una imagen", type=['jpg', 'jpeg', 'png'], key="uploader")

if archivo:
    imagen = Image.open(archivo).convert('RGB')
    st.image(imagen, caption="Imagen subida", use_column_width=True)

    reader = easyocr.Reader(['es'])
    resultado = reader.readtext(np.array(imagen))

    st.subheader("📝 Texto Detectado:")
    if resultado:
        for _, texto, confianza in resultado:
            st.write(f"- {texto} (Confianza: {confianza:.2f})")
    else:
        st.warning("No se detectó texto.")
