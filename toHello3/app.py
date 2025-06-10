import streamlit as st
import requests

# Configuración de Streamlit
st.title('¿Es probable que se cumpla?:')

# Formulario de entrada de Streamlit
IMPORTE_PROPUESTA = st.number_input("Importe Propuesta", 0.0)
TIPO_PROPUESTA = st.selectbox("Tipo propuesta", ['PROMESA', 'CAL_PAGO'])
PROP_VINCULADA = st.selectbox("Propuesta vinculada", ['NO','QUITA'])
PORCENTAJE_QUITA = st.slider("Porcentaje de Quita", 0, 70)
DEUDA_INICIAL = st.number_input("Deuda Inicial", 0.0)
DIAS_IMPAGO = st.number_input("Dias de impago", 0, 7500)
PRODUCTO_AGRUPADO = st.selectbox("Tipo producto", ['consumo', 'empresas', 'hipotecas', 'resto'])
REL_PER_CUE = st.selectbox("Tipo relacion", ['TIT', 'AVA', 'OTROS'])
MARCA_IND_SME = st.selectbox("Tipo de cliente", ['INDIVIDUALS', 'SME', 'SECURED'])
JUDICIALIZADO = st.selectbox("Judicializado", ['NO','SI'])

# Botón de predicción
if st.button('Predicción'):
    input_data = {
        'IMPORTE_PROPUESTA': IMPORTE_PROPUESTA,
        'TIPO_PROPUESTA': TIPO_PROPUESTA,
        'PROP_VINCULADA': PROP_VINCULADA,
        'PORCENTAJE_QUITA': PORCENTAJE_QUITA,
        'DEUDA_INICIAL': DEUDA_INICIAL,
        'DIAS_IMPAGO': DIAS_IMPAGO,
        'PRODUCTO_AGRUPADO': PRODUCTO_AGRUPADO,
        'REL_PER_CUE': REL_PER_CUE,
        'MARCA_IND_SME': MARCA_IND_SME,
        'JUDICIALIZADO': JUDICIALIZADO
    }
    
    # Realizar la solicitud POST a la API de predicción
    response = requests.post('http://localhost:8501/api/predict', json=input_data)
    
    # Verificar el código de estado de la respuesta
    if response.status_code == 200:
        result = response.json()
        if 'error' in result:
            st.error('Error al realizar la predicción: {}'.format(result['error']))
        else:
            if result['prediction'] == 1:
                st.success('Es probable que cumpla :thumbsup:')
            else:
                st.error('Es improbable que cumpla :thumbsdown:')
    else:
        st.error('Error al realizar la predicción. Código de estado: {}'.format(response.status_code))