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
        numero1=''
        numero2=''
        resultado=''
        return render.calculadora(numero1, numero2, resultado,operacion)
    
    def POST(self):
        formulario = web.input()
        numero1 = float(formulario['numero1'])
        numero2 = float(formulario['numero2'])
        operacion= formulario['operacion']

        if operacion == 'suma':
             resultado = numero1 + numero2

        if operacion == 'resta':
            resultado = numero1 - numero2


        return render.calculadora(numero1, numero2, resultado,operacion)
        
        
        
if __name__ == "__main__":
    app.run()