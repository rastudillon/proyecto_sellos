import streamlit as st
from paddleocr import PaddleOCR
from PIL import Image
import tempfile
import os

# Inicializar OCR
ocr = PaddleOCR(use_angle_cls=True, lang='es')  # Español

st.title("Reconocimiento de carácteres en sellos")
st.write("Sube una imagen y detectaremos el texto usando PaddleOCR")

# Subida de imagen
imagen_subida = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

if imagen_subida is not None:
    # Mostrar imagen
    imagen = Image.open(imagen_subida).convert('RGB')
    st.image(imagen, caption="Imagen subida", use_column_width=True)

    # Guardar temporalmente la imagen
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp_file:
        imagen.save(temp_file.name)
        ruta_temporal = temp_file.name

    # Procesar con PaddleOCR
    resultado = ocr.ocr(ruta_temporal, cls=True)
    os.remove(ruta_temporal)

    st.subheader("📝 Texto Detectado:")
    if resultado and resultado[0]:
        for linea in resultado[0]:
            texto = linea[1][0]
            confianza = linea[1][1]
            st.write(f"- {texto} (Confianza: {confianza:.2f})")
    else:
        st.warning("No se detectó texto.")
