# FizzBuzz con Unit Tests en Python

Proyecto basico de  **FizzBuzz** para la assig2 de Kanban.  
Se tiene una funcion que imprime mensajes para los multiplos de 3, 5 o ambos segun sea el resultado y un conjunto de **pruebas unitarias** usando `unittest` y `contextlib.redirect_stdout` para capturar salidas de consola.

---

## Funcionalidad

La funcion `fizzbuzz(n)`:

- Imprime `"Fizz - multiplo de 3"` si el numero es multiplo de 3.
- Imprime `"Buzz - multiplo de 5"` si es multiplo de 5.
- Imprime `"FizzBuzz - multiplo de ambos"` si es multiplo de 3 y 5.
- Imprime tambien el numero correspondiente en cada caso.
- No imprime nada para otros numeros.

---

## Archivos del Proyecto

```bash
.
├── fizzbuzz.py          
├── tests.py             
└── README.md            
```

## Como ejecutar
- Primero, Se necesita tener instalado Python en el sistema.
- Luego, puede ejecutar el programa principal para verificar su funcionamiento y dejar el resultado en la consola imprimiendo todos los multiplos del 0 a 99 con: python fizzbuzz.py.
- Despues puede ejecutar los tests correspondientes con: python tests.py, para verificar que la funcion cumple con las condiciones requeridas y con la cantidad de casos que se han definido.

## Pruebas incluidas

- test_fizz: Verifica salida para multiplos de 3.

- test_buzz: Verifica salida para multiplos de 5.

- test_fizzbuzz: Verifica salida para multiplos de ambos (como 15).

## Reflection

•	What did you learn by practicing TDD?
Al practicar TDD se comprenden un poco mejor que pensar primero en los resultados esperados mejora tanto la calidad como la claridad del código, ya que definimos a que queremos llegar sin desviarnos.
En lugar de escribir código y luego ver si funciona hacemos lo correcto o lo que debería hacer desde el inicio además de que uno se va dando cuenta un poco más a conciencia lo que realmente que es lo único que se pide, porque a veces realiza cosas extras que no se piden sin darse cuenta.

•	What would you change in your Kanban board after coding with that flow?
Posiblemente la columna de Back log, pero fue más en testing ya que estuve realizando y pensando las pruebas para que funcionaran y para que me servirían, tal vez incluso agregaría otra columna para expandir un poco las pruebas o en todo caso analizar los limites WIP.

•	Which XP practices were reflected (besides TDD)?
-	Diseño directo para lo necesario de los resultados
-	Iteración de desarrollo por cada parte de la función
-	Documentación un poco mas directa 
-	Refactorizar al escribir primero pruebas

