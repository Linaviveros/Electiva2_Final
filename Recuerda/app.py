from flask import Flask

app = Flask(__name__)

@app.route('/recordatorio')
def recordatorio():
    pill_name = "Aspirina"  # Nombre de la pastilla, puedes ajustarlo según sea necesario
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Recordatorio de Medicación</title>
        <style>
            body {{
                font-family: "Open Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial, sans-serif;
            }}
        </style>
        <script>
            alert('Recordatorio: No olvides tomar tu pastilla de {pill_name}');
            window.onload = function() {{
                document.body.innerHTML = '<h1>Recordatorio: Tomar {pill_name}</h1><p>Este mensaje se cerrará automáticamente.</p>';
                setTimeout(function() {{ window.close(); }}, 5000); // Cierra la ventana automáticamente después de 5 segundos
            }};
        </script>
    </head>
    <body>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(debug=True)
