class Rectangle:
    # constructor
    def _ini_(self, _base, _alssada):
        self.base = _base
        self.alssada = _alssada

    # setter

    def setBase(self, _base):
        self.base = _base

    def seAlssada(self, _alssada):
        self.alssada = _alssada
    # getters

    def getBase(self):
        return self.base

    def getAlsada(self):
        return self.alssada

    # Metodes

    def calcularPerimetre(base, alssada):
        print("El Perímetre es: " + str(2 * (alssada + base)))
       

    def calcularArea(base, alssada):
        print("l'area es: ", str(alssada * base))

    def __str__(self):
        return (f"Base: {self.base}\nAlssasda: {self.alssada}")
