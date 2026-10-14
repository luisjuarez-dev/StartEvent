"""Script que inicializa la aplicación de Flask e inicia la aplicación web."""

from src import crear_app

app = crear_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
