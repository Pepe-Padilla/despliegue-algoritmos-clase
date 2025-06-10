

import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from datetime import datetime


def transform_data(data):
    # Transformación de JUDICIALIZADO a 0 o 1
    data['JUDICIALIZADO'] = data['JUDICIALIZADO'].apply(lambda x: 1 if x == 'SI' else 0).astype(int)
    
    
    # Sustitución de valores en INDICE_MOROSIDAD
    data['INDICE_MOROSIDAD'] = data['PRODUCTO_AGRUPADO'].copy()
    data['INDICE_MOROSIDAD'] = data['INDICE_MOROSIDAD'].apply(lambda x: 
        0.0406430139678757 if x == 'empresas' 
        else (0.026078479161589 if x == 'hipotecas' 
        else (0.0428074328823858 if x == 'consumo' else 0.0672567492526397)))
   
   

    # Aplicar OneHotEncoder a las variables categóricas
    categorical_cols = ['TIPO_PROPUESTA', 'PROP_VINCULADA', 'MARCA_IND_SME', 'PRODUCTO_AGRUPADO', 'REL_PER_CUE']
    for col in categorical_cols:
        encoder = OneHotEncoder(sparse_output=False)
        encoded_values = encoder.fit_transform(data[[col]])
        encoded_df = pd.DataFrame(encoded_values, columns=encoder.get_feature_names_out([col]))
        data = pd.concat([data, encoded_df], axis=1)
        data.drop(col, axis=1, inplace=True)

    # Transformación de MONTH y YEAR
    now = datetime.now()
    data['MONTH'] = now.month
    data['YEAR'] = now.year

    # Lista de columnas necesarias en el output
    Columns = ['IMPORTE_PROPUESTA', 'PORCENTAJE_QUITA', 'DEUDA_INICIAL','DIAS_IMPAGO', 'JUDICIALIZADO', 'INDICE_MOROSIDAD',
'TIPO_PROPUESTA_CAL_PAGO', 'TIPO_PROPUESTA_PROMESA', 'PROP_VINCULADA_NO', 'PROP_VINCULADA_QUITA',
'MARCA_IND_SME_INDIVIDUALS', 'MARCA_IND_SME_SECURED', 'MARCA_IND_SME_SME',
'PRODUCTO_AGRUPADO_consumo', 'PRODUCTO_AGRUPADO_empresas', 'PRODUCTO_AGRUPADO_hipotecas',
'PRODUCTO_AGRUPADO_resto', 'REL_PER_CUE_AVA', 'REL_PER_CUE_OTROS', 'REL_PER_CUE_TIT', 'YEAR', 'MONTH']

    # Asegurarse de que todas las columnas estén presentes en el DataFrame final
    for col in Columns:
        if col not in data.columns:
            data[col] = 0

    # Ordenar las columnas de acuerdo a la lista Columns
    data = data[Columns]

    return data





#columns = ['IMPORTE_PROPUESTA','TIPO_PROPUESTA','PROP_VINCULADA','PORCENTAJE_QUITA','DEUDA_INICIAL','DIAS_IMPAGO','PRODUCTO_AGRUPADO','REL_PER_CUE','MARCA_IND_SME','JUDICIALIZADO','INDICE_MOROSIDAD', 'YEAR', 'MONTH']

Columns = ['IMPORTE_PROPUESTA','TIPO_PROPUESTA_CAL_PAGO','TIPO_PROPUESTA_PROMESA','MARCA_IND_SME_SECURED','MARCA_IND_SME_SME','MARCA_IND_SME_INDIVIDUALS','PROP_VINCULADA_NO','PROP_VINCULADA_QUITA','PORCENTAJE_QUITA','DEUDA_INICIAL','DIAS_IMPAGO','PRODUCTO_AGRUPADO_consumo','PRODUCTO_AGRUPADO_empresas','PRODUCTO_AGRUPADO_hipotecas','PRODUCTO_AGRUPADO_resto','REL_PER_CUE_AVA','REL_PER_CUE_OTROS','REL_PER_CUE_TIT','JUDICIALIZADO','INDICE_MOROSIDAD', 'YEAR', 'MONTH']