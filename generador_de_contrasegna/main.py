import random

def generador_de_contraseña(cantidad,longitud):
    caracters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&"
    contraseñas_usuario = []
    for c in range(cantidad):
        contraseña_random = ''
        for l in range(longitud):
            contraseña_random += random.choice(caracters)
        contraseñas_usuario.append(contraseña_random)
        contraseña_random = ''
    print('\nOpciones de Contraseñas:')
    print('\n'.join(i for i in contraseñas_usuario))
if __name__ == '__main__':
    print('Genera tus contraseñas\n----------------------')
    longitud = int(input('Longitud de la contraseña?: '))
    cantidad = int(input('Cantidad de password?: '))
    generador_de_contraseña(cantidad,longitud)