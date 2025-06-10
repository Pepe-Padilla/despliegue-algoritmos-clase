from flask import Flask, request, render_template_string , render_template
  
app = Flask(__name__)  
font_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form</title>
</head>
<body>
    <h1>Form</h1>
    <form action="/predict" method="post">
        <label for="IMPORTE_PROPUESTA">Importe Propuesta:</label>
        <input type="number" name="IMPORTE_PROPUESTA" required><br><br>

        <label for="TIPO_PROPUESTA">Tipo Propuesta:</label>
        <input type="text" name="TIPO_PROPUESTA" required><br><br>

        <label for="PROP_VINCULADA">Prop Vinculada:</label>
        <input type="text" name="PROP_VINCULADA" required><br><br>

        <label for="PORCENTAJE_QUITA">Porcentaje Quita:</label>
        <input type="number" name="PORCENTAJE_QUITA" required><br><br>

        <label for="DEUDA_INICIAL">Deuda Inicial:</label>
        <input type="number" name="DEUDA_INICIAL" required><br><br>

        <label for="DIAS_IMPAGO">Dias Impago:</label>
        <input type="number" name="DIAS_IMPAGO" required><br><br>

        <label for="PRODUCTO_AGRUPADO">Producto Agrupado:</label>
        <input type="text" name="PRODUCTO_AGRUPADO" required><br><br>

        <label for="REL_PER_CUE">Rel Per Cue:</label>
        <input type="text" name="REL_PER_CUE" required><br><br>

        <label for="MARCA_IND_SME">Marca Ind SME:</label>
        <input type="text" name="MARCA_IND_SME" required><br><br>

        <label for="JUDICIALIZADO">Judicializado:</label>
        <input type="text" name="JUDICIALIZADO" required><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        # Render the form template
        return render_template_string(font_html)  # assuming you have a template named form.html
    
    # Capture form data
    input_data = {
        'IMPORTE_PROPUESTA': request.form.get('IMPORTE_PROPUESTA', type=float),
        'TIPO_PROPUESTA': request.form.get('TIPO_PROPUESTA'),
        'PROP_VINCULADA': request.form.get('PROP_VINCULADA'),
        'PORCENTAJE_QUITA': request.form.get('PORCENTAJE_QUITA', type=int),
        'DEUDA_INICIAL': request.form.get('DEUDA_INICIAL', type=float),
        'DIAS_IMPAGO': request.form.get('DIAS_IMPAGO', type=int),
        'PRODUCTO_AGRUPADO': request.form.get('PRODUCTO_AGRUPADO'),
        'REL_PER_CUE': request.form.get('REL_PER_CUE'),
        'MARCA_IND_SME': request.form.get('MARCA_IND_SME'),
        'JUDICIALIZADO': request.form.get('JUDICIALIZADO')
    }

    # Print input data to the console
    print(input_data)
    ##load_model()
    ##model.predict()
    input_data_modified = input_data['IMPORTE_PROPUESTA'] * 100
    # For now, just return a simple confirmation message
    return {"El importe de la propuesta es": input_data_modified}
@app.route('/user_data', methods=['GET'])
def user_data():
    # Access the data from the GET request
    data = request.args
    # Print the data
    print(data)
    # Return a response
    return {"User Data": data}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # We will run Flask on port 8080
