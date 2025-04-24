""" Conversión de Números:
Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos. """


def Menu():
    opt = ''

    print("1 - Convertir un número decimal a binario.")
    print("2 - Convertir un número binario a decimal.")
    opt = input("Escoga una opción: ")

    print("opt ", opt)

    while opt != '1' and opt != '2':
        opt = input("Por favor escoga una opción válida: ")

    return opt

def ConvertirDecimal(numero): # creamos la función que convierte de decimal a binario
    if numero == 0: 
        return "0" # Si el número ingresado es 0, en binario también es 0
    binario = "" # creamos un string vacío para ir guardando el número en binario
    while numero > 0: # usamos un ciclo while que tiene como condición que el número ingresado sea mayor a 0
        residuo = numero % 2 # guardamos el residuo de número dividido 2
        binario = str(residuo) + binario # en binario vamos guardando en cada iteración el valor del residuo en forma de string
        numero //= 2 # guardamos el resultado de la división entera en número para poder reiniciar el ciclo
    return binario # Fin de la función que convierte de decimal a binario


def ConvertirBinario(number): # creamos la función que convierte un número binario a decimal
    sum = 0
    number = ''.join(reversed(number))

    for i in range(0, len(number)):
        if number[i] == '1':
            sum += int(number[i]) * (2 ** i)

    return sum


print("Bienvenido usuario!!")
print("Software convertidor binario a decimal - decimal a binario")

opt = Menu()

if opt == '1':
    print(ConvertirDecimal(int(input("Ingrese un número decimal que quiera convertir en binario: "))))
elif opt == '2':
    print(ConvertirBinario(input("Ingrese un número binario que quiera convertir en decimal: ")))

