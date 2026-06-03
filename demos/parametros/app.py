import web

urls = (
    '/', 'Index',
    '/parametros', 'Parametros'
    
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()

class Parametros:
    def GET(self):
        titulo="Título desde Python"
        descripcion="""Lorem ipsum dolor sit amet consectetur adipiscing elit et ultricies, sodales vitae cras aliquet eros fusce pulvinar turpis augue, commodo dignissim netus himenaeos posuere dui viverra hac. Fermentum magna aliquam euismod donec dui est senectus mus eros sapien, et ut etiam ac platea mi interdum orci cras suscipit, dictumst litora aptent per facilisi nibh hac quam ligula. Malesuada velit himenaeos sollicitudin magnis sociosqu id potenti elementum maecenas tempor, consequat volutpat commodo erat nam imperdiet dui luctus purus.

Suspendisse curae eleifend dignissim fermentum mi taciti, dis et facilisis nulla feugiat libero fringilla, metus risus mauris porttitor ornare. Luctus interdum placerat lacinia fringilla purus viverra mauris, magnis natoque pretium erat nibh vivamus pulvinar vel, auctor vitae per aptent semper fermentum. Tristique congue aenean a curabitur vehicula justo convallis vivamus mi faucibus lectus parturient, sodales suscipit platea egestas lacinia augue leo enim per nullam venenatis."""
        return render.parametros(titulo,descripcion)
if __name__ == "__main__":
    app.run()