# Ejercicio para la semana de integración 1 de la materia de Matemáticas, para el curso de programación de UTN.
## Siguiendo las pautas de trabajo propuestas, se desarrolló un programa en python que conviente el número decimal propuesto por el usuario al número binario correspondiente.


## Link del video: 
* Integrantes del grupo: Matías Facundo Herrera, Matías Vicente Lopez

# Explicación del funcionamiento del código:

* Función Menu: Se crea un menú sencillo para dar al usuario la opción de navegar entre las opciones de convertir un binario a decimal y un decimal a binario.
Se utiliza la estructura repetitiva while para forzar al usuario a escoger una opción válida. La función retorna un string.

* Función ValidarBinario: Se utiliza el parámetro x para validar un número binario ingresado por el usuario. Si este no cumple con la condición de ser un número binario, el programa
lanzará un advertencia forzando al usuario a ingresar un número binario. Esto será un bucle while que sólo finalizará cuando el usuario ingrese un dato válido.
Se utiliza un ciclo for para iterar sobre la cadena proporcionada y determinar si contiene números diferentes de 1 y 0, si no es así, el programa continúa sin entrar al bucle while y retornando el valor del parámetro x.

* Función ConvertirDecimal:

* Función ConvertirBinario: Decidimos dejar que Chat GPT lea nuestra función e interprete nuestro código, acción que ejecutó perfectamente.

* Finalmente damos la bienvenida al usuario e invocamos a la función Menu, se evalúa el retorno de esta y es utilizada una estructura condicinal para llamar la función ConvertirDecimal o ConvertirBinario según las necesidades del usuario. 