from app import create_app

app = create_app()

if __name__=="__main__":
    app.run(debug=True)
# __init__.py convierte cada carpeta en un paquete de python, y hace que Git suba las carpetas aunque esten vacias. 
# create_app() arma la aplicación. Más adelante aqui conectaremos la configuracion y las rutas.
# requirements.txt lista las librerias para mis compañeros las instalen. 