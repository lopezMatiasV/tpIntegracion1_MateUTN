""" Conversión de Números:
Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos. """

def convertirDecimal(numero): # creamos la funcion que conviente de decimal a binario
    if numero == 0: 
        return "0" # Si el numero ingresado es 0, en binario tambien es 0
    binario = "" # creamos un string vacio para ir guardando el numero en binario
    while numero > 0: # usamos un ciclo while que tiene como condicion que el numero ingresado sea mayor a 0
        residuo = numero % 2 # guardamos el residuo de numero dividido 2
        binario = str(residuo) + binario # en binario vamos guardando en cada iteracion el valor del residuo en forma de string
        numero //= 2 # guardamos el resultado de la division entera en numero para poder reiniciar el ciclo
    return binario # Fin de la función que convierte de decimal a binario

print("Esta función convierte su número a su equivalente a binario!!!")
print(convertirDecimal(int(input("Ingrese el número que quiera convertir: ")))) # imprimimos el resultado de la funcion