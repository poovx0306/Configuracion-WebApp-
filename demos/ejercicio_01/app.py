# Muestra las páginas web usando el framework web.py
import web

# --- RUTAS (URLs) ---
# "Si entran a tal enlace, ejecuta tal clase". Va en pares: ruta, clase.
urls = (
    '/',          'Inicio',
    '/clientes',  'Clientes',
    '/usuarios',  'Usuarios',
)

# Crea la aplicación y prepara la carpeta de plantillas.
app = web.application(urls, globals())
render = web.template.render('templates')


# --- POO: una clase por página ---
# Cada GET saca su HTML de la carpeta templates y lo muestra.

class Inicio:
    def GET(self):
        return render.index()

class Clientes:
    def GET(self):
        return render.clientes()

class Usuarios:
    def GET(self):
        return render.usuarios()


# Arranca el servidor (por defecto en http://localhost:8080/)
if __name__ == "__main__":
    app.run()
