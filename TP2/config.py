class Config:
    def __init__(self, clase, data, cruce, mutacion, seleccion, reemplazo, implementacion, corte, a, b, n, k):
        self.clase = clase
        self.data = data
        self.cruce = cruce
        self.mutacion = mutacion
        self.seleccion = seleccion
        self.reemplazo = reemplazo
        self.implementacion = implementacion
        self.corte = corte
        self.a = a
        self.b = b
        self.n = n
        self.k = k
    
    def __str__(self):
        return '%s{%s\n}' % (
            type(self).__name__,
            ', '.join('\n\t%s = %s' % item for item in vars(self).items())
        )
