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
        numero1 = ''
        numero2 = ''
        resultado = ''
        return render.calculadora(numero1, numero2, resultado)
    
    def POST(self):
        formulario = web.input()
        numero1 = float(formulario['numero1'])
        numero2 = float(formulario['numero2'])
        operacion = formulario['operacion']
        resultado=''

        if operacion == 'sumar':
            resultado = numero1 + numero2
        if operacion == 'restar':
            resultado = numero1 - numero2
        if operacion == 'multiplicar':
            resultado = numero1*numero2
        if operacion == 'dividir':
            if numero2!=0:
                resultado = numero1/numero2
        if operacion == 'raiz':
            resultado = numero1 ** (1/numero2)
        if operacion=='potencia':
            resultado = numero1 ** numero2
        if operacion == 'modulo':
            resultado = numero1 % numero2
        if operacion == 'limpiar':
            numero1=''
            numero2=''
            resultado=''

        return render.calculadora(numero1, numero2, resultado)

if __name__ == "__main__":
    app.run()