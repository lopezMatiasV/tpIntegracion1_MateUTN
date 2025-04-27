# Ejercicio para la semana de integración 1 de la materia de Matemáticas, para el curso de programación de UTN.
## Siguiendo las pautas de trabajo propuestas, se desarrolló un programa en python que conviente el número decimal propuesto por el usuario al número binario correspondiente. Dicha aplicación también hace lo opuesto, convierte un número binario a decimal. Se utilizó lo visto hasta ahora en la materia de programación, como bucles, condicionales y funciones. También se crearon validaciones para que siempre el usuario ingrese opciones validas y no genere un error en dicho programa. 


## Link del video: 
* https://youtu.be/A_FG3ShE9jw
* Integrantes del grupo: Matías Facundo Herrera, Matías Vicente Lopez

# Explicación del funcionamiento del código:

* Función Menu: Se crea un menú sencillo para dar al usuario la opción de navegar entre las opciones de convertir un binario a decimal y un decimal a binario.
Se utiliza la estructura repetitiva while para forzar al usuario a escoger una opción válida. La función retorna un string.

* Función ValidarBinario: Se utiliza el parámetro x para validar un número binario ingresado por el usuario. Si este no cumple con la condición de ser un número binario, el programa
lanzará un advertencia forzando al usuario a ingresar un número binario. Esto será un bucle while que sólo finalizará cuando el usuario ingrese un dato válido.
Se utiliza un ciclo for para iterar sobre la cadena proporcionada y determinar si contiene números diferentes de 1 y 0, si no es así, el programa continúa sin entrar al bucle while y retornando el valor del parámetro x.

* Función ConvertirDecimal: Utilizamos la variable numero como parámetro de entrada. Se utiliza un condicional por si el número ingresado por el usuario es 0. Se utiliza una estructura cíclica while para dividir la variable numero entre dos sucesivamente hasta que su cociente sea 0. El residuo es guardado y concatenado sucesivamente y así obtenemos
el número binario equivalente.

* Función ConvertirBinario: Decidimos dejar que Chat GPT lea nuestra función e interprete nuestro código, acción que ejecutó perfectamente. Esto nos sirve para percatarnos
lo útil que es usar IA en este tipo de proyectos.

![image1](./files/Screenshot%202025-04-26%20005831.png)
![image2](./files/Screenshot%202025-04-26%20005845.png)
![image3](./files/Screenshot%202025-04-26%20005856.png)


* Finalmente damos la bienvenida al usuario e invocamos a la función Menu, se evalúa el retorno de esta y es utilizada una estructura condicinal para llamar la función ConvertirDecimal o ConvertirBinario según las necesidades del usuario. 