from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Affiche les variables d'environnement utiles pour debug
    print("HOST:", os.environ.get("DB_HOST"))
    print("USER:", os.environ.get("DB_USER"))
    print("PASSWORD:", os.environ.get("DB_PASSWORD"))
    print("DB NAME:", os.environ.get("DB_NAME"))

    try:
        connection = mysql.connector.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', ''),
            database=os.environ.get('DB_NAME', '')
        )
        if connection.is_connected():
            message = "Connexion à MySQL réussie !"
        else:
            message = "Échec de la connexion à MySQL."
    except Exception as e:
        message = f"Erreur : {e}"

    return render_template("index.html", message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
