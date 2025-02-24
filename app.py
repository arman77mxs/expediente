import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Expediente Médico", layout="wide")

# Imagen del header
imagen_path = "imagen.png"  # Ruta relativa, el archivo está en la misma carpeta que app.py
# Cargar imagen y redimensionar al 40%
image = Image.open(imagen_path)
width, height = image.size
new_width = int(width * 0.4)
new_height = int(height * 0.4)
st.image(imagen_path, width=new_width)

# Título de la aplicación
st.title("Formulario de Expediente Médico")

# Crear un formulario
with st.form("expediente_medico"):
    # Información personal del paciente
    st.header("Información Personal")
    col1, col2 = st.columns(2)
    
    with col1:
        nombre = st.text_input("Nombre completo")
        fecha_nacimiento = st.date_input("Fecha de nacimiento")
        sexo = st.selectbox("Sexo", ["Masculino", "Femenino", "Otro"])
    
    with col2:
        identificacion = st.text_input("Número de identificación")
        telefono = st.text_input("Teléfono")
        email = st.text_input("Correo electrónico")
    
    direccion = st.text_area("Dirección")
    
    # Antecedentes médicos
    st.header("Antecedentes Médicos")
    
    # Enfermedades previas
    st.subheader("Enfermedades previas")
    enfermedades = st.multiselect(
        "Seleccione las enfermedades que ha padecido",
        ["Diabetes", "Hipertensión", "Asma", "Cáncer", "Enfermedades cardíacas", 
         "Enfermedades respiratorias", "Enfermedades renales", "Otras"]
    )
    
    if "Otras" in enfermedades:
        otras_enfermedades = st.text_area("Especifique otras enfermedades")
    
    # Alergias
    st.subheader("Alergias")
    tiene_alergias = st.radio("¿Tiene alergias?", ["Sí", "No"])
    
    if tiene_alergias == "Sí":
        alergias = st.text_area("Describa sus alergias")
    
    # Cirugías
    st.subheader("Cirugías")
    tiene_cirugias = st.radio("¿Ha tenido cirugías?", ["Sí", "No"])
    
    if tiene_cirugias == "Sí":
        cirugias = st.text_area("Describa las cirugías realizadas y sus fechas")
    
    # Medicamentos actuales
    st.subheader("Medicamentos actuales")
    toma_medicamentos = st.radio("¿Toma medicamentos actualmente?", ["Sí", "No"])
    
    if toma_medicamentos == "Sí":
        medicamentos = st.text_area("Liste los medicamentos que toma actualmente")
    
    # Antecedentes familiares
    st.header("Antecedentes Familiares")
    antecedentes_familiares = st.text_area("Describa enfermedades importantes en su familia")
    
    # Hábitos
    st.header("Hábitos")
    col1, col2 = st.columns(2)
    
    with col1:
        fuma = st.radio("¿Fuma?", ["Sí", "No"])
        if fuma == "Sí":
            cantidad_cigarrillos = st.number_input("Cigarrillos por día", min_value=0)
    
    with col2:
        alcohol = st.radio("¿Consume alcohol?", ["Sí", "No"])
        if alcohol == "Sí":
            frecuencia_alcohol = st.selectbox(
                "Frecuencia de consumo", 
                ["Ocasional", "Semanal", "Diario"]
            )
    
    # Consulta actual
    st.header("Motivo de Consulta Actual")
    motivo_consulta = st.text_area("Describa el motivo de su consulta")
    sintomas = st.text_area("Describa sus síntomas actuales")
    inicio_sintomas = st.date_input("Fecha de inicio de los síntomas")
    
    # Notas adicionales
    st.header("Notas Adicionales")
    notas = st.text_area("Información adicional relevante")
    
    # Botón de envío
    submitted = st.form_submit_button("Guardar Expediente")
    
    if submitted:
        st.success("Expediente guardado correctamente")
        # Aquí se podría añadir código para guardar los datos en una base de datos

# Si el formulario fue enviado, mostrar un resumen
if 'submitted' in locals() and submitted:
    st.header("Resumen del Expediente")
    st.write(f"**Nombre:** {nombre}")
    st.write(f"**Identificación:** {identificacion}")
    st.write(f"**Fecha de nacimiento:** {fecha_nacimiento}")
    st.write(f"**Sexo:** {sexo}")
    # Se podría mostrar más información del formulario aquí