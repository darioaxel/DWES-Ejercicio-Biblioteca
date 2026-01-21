# DWES-Ejercicio-Biblioteca

Una biblioteca va a tener: **publicaciones**

* publicacion:  
    * [libro, artículo]
    * ISBN
    * titulo
    * [FK] [1-N] autor/autores
    * año/fecha publicación
    * editorial
    * [FK] [0-N] unidades (0-N)
* autor:
    * id
    * nombre
    * apellidos
    * fecha_nacimiento

* unidad:
    * ESTADO (nuevo, usado, muy usado, a retirar)
