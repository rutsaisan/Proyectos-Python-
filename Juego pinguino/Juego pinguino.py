from flask import Flask, render_template

app = Flask(__name__)

# La ruta principal que sirve el juego HTML
@app.route('/')
def inicio():
    # Flask buscará 'index.html' en una carpeta llamada 'templates'
    # Por simplicidad, si el index.html contiene todo (HTML, CSS, JS),
    # simplemente lo renderiza.
    # Nota: Idealmente, el HTML se movería a una carpeta 'templates'.
    
    # Para este caso, si el HTML está en el mismo nivel, puedes usar
    # el método 'send_file' o mover el HTML a 'templates'
    
    # Asumiendo que has movido el index.html a una carpeta llamada 'templates':
    return render_template('Estilo cozy.html') 

if __name__ == '__main__':
    # Ejecutar el servidor en modo debug
    app.run(debug=True)