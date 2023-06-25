"""
Hay que instalar en la terminal lo siguiente: 
pip install pillow
pip install matplotlib
"""

from PIL import Image
import matplotlib.pyplot as plt

# clase Curso

class Curso:
    def __init__(self, codigo, nombre, cupos, precio, duracion, imagen_ruta):
        self.codigo = codigo           
        self.nombre = nombre           
        self.cupos = cupos             
        self.precio = precio           
        self.duracion = duracion
        self.imagen = Image.open(imagen_ruta)
    
    def modificar(self, nuevo_nombre, nuevo_cupos, nuevo_precio, nueva_duracion, nueva_imagen_ruta):
        self.nombre = nuevo_nombre              # Modifica la descripción
        self.cupos = nuevo_cupos                # Modifica la cantidad
        self.precio = nuevo_precio              # Modifica el precio
        self.duracion = nueva_duracion
        self.imagen = Image.open(nueva_imagen_ruta)
    
    def mostrar_imagen(self):
        plt.imshow(self.imagen)
        plt.axis('off')
        plt.show()


class Inventario:
    def __init__(self):
        self.cursos = []

    # Método para crear objetos de la clase "Curso" y agregarlos al inventario. Es la "C" (create) de CRUD
    def agregar_curso(self, codigo, nombre, cupos, precio, duracion, imagen_ruta):
        nuevo_curso = Curso(codigo, nombre, cupos, precio, duracion, imagen_ruta)
        self.cursos.append(nuevo_curso)  # Agrega un nuevo producto a la lista
    
    # Método para obtener objetos de la clase "Curso" y agregarlos al inventario. Es la "R" (read) de CRUD
    def consultar_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso # Retorna un objeto
        return False
    
    # Método para modificar objetos de la clase "Curso" y agregarlos al inventario. Es la "U" (update) de CRUD
    def modificar_curso(self, codigo, nuevo_nombre, nuevo_cupos, nuevo_precio, nueva_duracion, nueva_imagen_ruta):
        curso = self.consultar_curso(codigo)
        if curso:
            curso.modificar(nuevo_nombre,nuevo_cupos, nuevo_precio, nueva_duracion, nueva_imagen_ruta)

    # Método para eliminar objetos de la clase "Curso" y agregarlos al inventario. Es la "D" (delete) de CRUD
    def eliminar_curso(self, codigo):
        eliminar = False
        for curso in self.cursos:
            if curso.codigo == codigo:
                eliminar = True
                curso_eliminar = curso      
        if eliminar == True:
            self.cursos.remove(curso_eliminar)
            print(f'Curso {codigo} eliminado.')
        else:
            print(f'Curso {codigo} no encontrado.')

    def listar_cursos(self):
        print("#" * 50)
        print()
        print(f"Lista de cursos en el inventario:\n")
        print("Cod\tNombre del curso\tCupos disponibles\tPrecio\tDuracion\tRuta imagen")
        for curso in self.cursos:
            print(f'{curso.codigo}\t\t{curso.nombre} |\t{curso.cupos} |\t${curso.precio} |\t{curso.duracion} |\t{curso.imagen.filename}')
        curso.mostrar_imagen()
        print()
        print("#" * 50)


class Carrito:
    def __init__(self):
        self.items = []
    
    def agregar(self, codigo, inventario):
        curso = inventario.consultar_curso(codigo)
        if curso:
            for curso_existente in self.items:
                if curso_existente.codigo == codigo:
                    print("El curso ya está en tu carrito")
                    return
            if curso.cupos > 0:
                self.items.append(curso)
                print(f"El curso {curso.nombre} se ha agregado al carrito")
                curso.cupos -= 1
            else:
                print(f"No hay cupos disponibles para {curso.nombre}")
        else:
            print("Curso no disponible")
    
    def eliminar(self, codigo):
        for curso in self.items:
            if curso.codigo == codigo:
                self.items.remove(curso)
                print(f"Se ha eliminado del carrito el curso {curso.nombre}")
                curso.cupos += 1
                return
        print("El curso no está en el carrito")
    
    def vaciar_carrito(self):
        self.items = []
        print("El carrito se ha vaciado.")
    
    def mostrar_carrito(self):
        if self.items:
            print(f"Cursos en el carrito".center(30, "-"))
            for curso in self.items:
                print(f"- {curso.nombre}")
        else:
            print("El carrito esta vacio")
    
    def calcular_total(self):
        total = 0
        for curso in self.items:
            total += curso.precio
        return total


    # probar programa principal
mi_inventario = Inventario()

mi_inventario.agregar_curso(1, "Introduccion a Python", 30, 50000, "5 meses", "./assets/img/bg-1.png")
mi_inventario.agregar_curso(2, "Introduccion a Javascript", 40, 30000, "8 meses", "./assets/img/bg-1.png")
mi_inventario.agregar_curso(3, "Introduccion a HTML", 60, 35000, "2 meses", "./assets/img/bg-1.png")
mi_inventario.agregar_curso(4, "Introduccion a CSS", 65, 45000, "2 meses", "./assets/img/bg-1.png")

curso = mi_inventario.consultar_curso(1) # Consultar un curso en el inventario:
if curso:
    print(f"Curso encontrado: {curso.nombre}")
else:
    print("Curso no encontrado")

mi_inventario.modificar_curso(1, "Python de 0 a 100", 30, 65000, "6 meses", "./assets/img/bg-1.png") # Modifica curso en el inventario
curso = mi_inventario.consultar_curso(1) # Consultar un curso en el inventario:
if curso:
    print(f"Curso encontrado: {curso.nombre}")
else:
    print("Curso no encontrado")

mi_inventario.listar_cursos()

#intacio objeto de la clase Carrito:
carrito = Carrito()
carrito.agregar(2, mi_inventario )
carrito.agregar(4, mi_inventario )

carrito.mostrar_carrito()
carrito.eliminar(2)
carrito.agregar(1, mi_inventario )
carrito.mostrar_carrito()
total = carrito.calcular_total()
print(f"Total del carrito: ${total}")

"""
    *** Probar clase Curso ***

curso = Curso(1, "Introduccion a Python", 30, 55000, "./assets/img/bg-1.png")
print(f"{curso.codigo} | {curso.nombre} | {curso.cupos} | ${curso.precio}")
curso.mostrar_imagen()

*** probar clase Inventario***
    *** Probar agregar curso ***
mi_inventario = Inventario()

mi_inventario.agregar_curso(1, "Introduccion a Python", 30, 50000, "5 meses", "./assets/img/bg-1.png")
mi_inventario.agregar_curso(2, "Introduccion a Javascript", 40, 30000, "8 meses", "./assets/img/bg-1.png")
mi_inventario.agregar_curso(3, "Introduccion a HTML", 60, 35000, "2 meses", "./assets/img/bg-1.png")
mi_inventario.agregar_curso(4, "Introduccion a CSS", 65, 45000, "2 meses", "./assets/img/bg-1.png")


    *** Probar consultar_curso ***

curso = mi_inventario.consultar_curso(1)
if curso != False:
    print(f'Curso encontrado:\nCodigo: {curso.codigo}\nTitulo: {curso.nombre}\nCantidad: {curso.cupos}\nPrecio: ${curso.precio}\n{curso.duracion}')
else:
    print("Curso no encontrado.")
    

    *** Probar modificar_curso ***

curso1 = mi_inventario.modificar_curso(1, "Python nivel -1", 35, 66000, "4 meses", "./assets/img/bg-1.png")


    *** Probar listar_cursos ***

mi_inventario.listar_cursos()


    *** Probar eliminar_curso ***

mi_inventario.eliminar_curso(6)
"""