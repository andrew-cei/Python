# Importar módulo
from paquete1.modulo1 import Cliente
# Creación de un cliente con nombre incorrecto
cliente_1 = Cliente('Amanda', 'Tapia', 'Amanda@cienciaseingenieria.org')
print(cliente_1)

# Corrección del nombre del cliente
cliente_1.setLastName('Tapping')
print(cliente_1)

# Creación de un segundo cliente
cliente_2 = Cliente('Andrew', 'Anderson', 'Andrew@cienciaseingenieria.org')
print(cliente_2)

# Agregar productos a cliente 2
cliente_2.setProducts(['Pantalla', 'Celular'])
print(cliente_2.getProducts())