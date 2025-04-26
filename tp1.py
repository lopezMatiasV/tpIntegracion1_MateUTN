""" Conversión de Números:
Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos. """

# Se crea la función Menu para dar opción al usuario del número que desea convertir
def Menu():
    opt = ''

    print("1 - Convertir un número decimal a binario.")
    print("2 - Convertir un número binario a decimal.")
    opt = input("Escoga una opción: ")

    while opt != '1' and opt != '2': # Se evalúa que la opción sea válida. Si no es así se continúa pidiendo una opción válida
        opt = input("Por favor escoga una opción válida: ")

    return opt

def ValidarBinario(x):
    for i in range(len(x)):

        while x[i] != '1' and x[i] != '0':
            x = input("Por favor ingrese un número binario válido: ")
    
    return x

def ConvertirDecimal(numero): # Creamos la función que convierte de decimal a binario
    if numero == 0: 
        return "0" # Si el número ingresado es 0, en binario también es 0
    binario = "" # creamos un string vacío para ir guardando el número en binario
    while numero > 0: # usamos un ciclo while que tiene como condición que el número ingresado sea mayor a 0
        residuo = numero % 2 # guardamos el residuo de número dividido 2
        binario = str(residuo) + binario # en binario vamos guardando en cada iteración el valor del residuo en forma de string
        numero //= 2 # guardamos el resultado de la división entera en número para poder reiniciar el ciclo
    return binario # Fin de la función que convierte de decimal a binario


def ConvertirBinario(number): # Creamos la función que convierte un número binario a decimal
    sum = 0
    reversed = ''

    # Usamos un ciclo for para invertir el orden del string ingresado concatenando el siguiente caratacter con el anterior

    for x in number:
        reversed = x + reversed

    for i in range(0, len(reversed)): # Se recorre el string anteriormente invertido
        if reversed[i] == '1': # Se verifica que sólo tomemos en cuenta el digito activo para realizar la ecuación
            sum += int(reversed[i]) * (2 ** i) # Se realiza la ecuación de suma de productos: base 2 se multiplica por su posición y el producto es multiplicado por un digito activo(1)

    return sum


print("Bienvenido usuario!!")
print("Software convertidor decimal a binario - binario a decimal")

opt = Menu() # Se llama a la función Menu y su valor se guarda en la variable opt

userOption = ''

# Se evalúa la variable opt según los requerimientos del usuario
if opt == '1':
    print(ConvertirDecimal(int(input("Ingrese un número decimal que quiera convertir en binario: "))))
elif opt == '2':
    userOption = input("Ingrese un número binario que quiera convertir a decimal: ")
    userOption = ValidarBinario(userOption)
    print(ConvertirBinario(userOption))


