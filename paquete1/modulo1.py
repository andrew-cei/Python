class Cliente:
    # Constructor de la clase
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.products = []
    # Método para imprimir el objeto
    def __str__(self) -> str:
        return 'Cliente: ' + self.first_name + ' ' + self.last_name + '\nCorreo: ' + self.email
    # Métodos de obtención
    def getName(self):
        return self.first_name + ' ' + self.last_name
    
    def getEmail(self):
        return self.email
    
    def getProducts(self):
        return self.products
    # Métodos de inicialización
    def setFirstName(self, first_name):
        self.first_name = first_name
    
    def setLastName(self, last_name):
        self.last_name = last_name

    def setEmail(self, email):
        self.email = email
    
    def setProducts(self, products):
        self.products = products
