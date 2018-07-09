# RentBikes

Problema
--------

Una compañía que alquila bicicletas lo hace bajo las siguientes opciones:
1. Alquilar por una hora cuesta $5.
2. Alquilar por un día cuesta $20.
3. Alquilar por una semana cuesta $60.
4. Los alquileres familiares de entre 3 y 5 bicicletas (de cualquier tipo de 
alquiler) tienen un descuento del 30% sobre el precio final.

Solución
--------

Se decidió crear un programa que corre por shell el cual cuenta con 4 
opciones
* Alquilar bicis
* Ver bicicletas alquiladas
* Ver precios
* Salir

Se creó un objeto que va guardando los alquileres que se van efectuando (Rent).
Para poder alquilar una bicicleta y poder ver el precio es necesario saber 
dos variables
* Cantidad de bicicletas a alquilar.
* Cantidad de horas que se van a alquilar.
con estas dos variables ya podemos calcular el precio a cobrar y la fecha en 
la cual serán devueltas.
También se puede definir si se trata de un alquiler familiar, para lo cual
se necesita alquilar entre 3 y 5 bicicletas, por lo que si intentamos
alquilar con el descuento familiar 1, 2 o más de 5 bicicletas entonces no
aplicamos el descuento del 30%.
