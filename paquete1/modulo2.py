def login(data):
  # Bandera para detectar existencia de usuario y contraseña
  flag = 0
  # Lectura de nombre de usuario
  name = input('Escribe tu nombre de usuario: ')
  # Revisión de usuario en la base de datos
  for user in data.keys():
    if name == user:
      flag = 1
      break
  if flag == 0:
    print('Usuario no encontrado')
    return False
  # Lectura de contraseña
  contr = input('Escribe tu contraseña: ')
  # Revisión de contraseña
  if contr == data[name]:
    flag = 2
    print('Acceso correcto')
    return True
  if flag == 1:
    print('Acceso denegado')
    return False

def registro(data):
  name = input('Escribe tu nombre de usuario: ')
  contr = input ('Escribe tu contraseña: ')
  data[name] = contr
  return True

def leer(data):
  print(f'Usuario\tContraseña')
  for user, pas in data.items():
    print(f'{user}\t{pas}')