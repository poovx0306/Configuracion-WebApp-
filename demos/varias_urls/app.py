import web

urls = (
    '/', 'Index',
    '/clientes', 'Clientes'
    )

app = web.application(urls, globals())

class Index:
    def GET(self):
        return 'Hola mundo desde web.py'

class Clientes:
    def GET(self):
        return 'Está es la página de CLIENTES'

if __name__ == "__main__":
    app.run()