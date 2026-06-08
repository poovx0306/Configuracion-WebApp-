import web

urls = (
    '/', 'Index',
    '/calculadora', 'Calculadora'
)
app = web.application(urls, globals())
render = web.template.render('views')


class Index:
    def GET(self):
        return render.index()
    
class Calculadora:
    def GET(self):
        return render.calculadora()
    
    def POST(self):
        formulario = web.input()
        return f"Formulario: {formulario}"
    

if __name__ == "__main__":
    app.run()