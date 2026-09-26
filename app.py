from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Atividade PaaS</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
                background-color: #f5f5f5;
            }
            .card {
                background: white;
                max-width: 700px;
                margin: auto;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.15);
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Aplicação PaaS em execução</h1>
            <h2>Arquitetura de Computação em Nuvem</h2>
            <p>Aplicação Python/Flask implantada na plataforma Render.</p>
            <p><strong>Modelo de serviço:</strong> Platform as a Service (PaaS)</p>
        </div>
    </body>
    </html>
    """
