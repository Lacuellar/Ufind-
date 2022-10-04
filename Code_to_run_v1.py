'''
Código de prueba para función de pedir y buscar información.

'''
Decision1 = int(input('Elige 1.Afuera de la universidad o 2.Adentro de la universidad. Respuesta: '))
if Decision1==1:
    print('Has elegido 1.Afuera de la universidad')
    comida = input('Ingrese el nombre de la comida a buscar. Respuesta: ')
    Monedero = int(input('Ingrese cuanto dinero esta dispuesto a gastar. Respuesta: '))
    print('Se realizará la busqueda')
elif Decision1==2:
    print('Has elegido 2.Adentro de la universidad.')
    Decision2 = int(input('Elige 1.du nord express o 2.dunord terraza. Respuesta: '))
    if Decision2==1:
        print('Has elegido 1.du nord express')
        comida = input('Ingrese el nombre de la comida a buscar. Respuesta: ')
        Monedero = int(input('Ingrese cuanto dinero esta dispuesto a gastar. Respuesta: '))
        print('Se realizará la busqueda')
    elif Decision2==2:
        print('Has elegido 2.dunord terraza ')
        comida = input('Ingrese el nombre de la comida a buscar. Respuesta: ')
        Monedero = int(input('Ingrese cuanto dinero esta dispuesto a gastar. Respuesta: '))
        print('Se realizará la busqueda')
        
## Idea general de como trabajara nuestro proyecto.
## Aun esta en una idea simple.
