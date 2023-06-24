"""
Hay que instalar en la terminal lo siguiente: 
pip install pillow
pip install matplotlib
"""
# from PIL import Image

# # clase Curso
# class Curso:
#     def __init__(self, codigo, nombre, cupos, precio, imagen_ruta):
#         self.codigo = codigo           # Código 
#         self.nombre = nombre           # Nombre curso
#         self.cupos = cupos       # Cantidad disponible (stock)
#         self.precio = precio           # Precio 
#         self.imagen = Image.open(imagen_ruta)
    
#     def modificar(self, nuevo_nombre, nuevo_cupos, nuevo_precio, nueva_imagen_ruta):
#         self.nombre = nuevo_nombre              # Modifica la descripción
#         self.cupos = nuevo_cupos               # Modifica la cantidad
#         self.precio = nuevo_precio            # Modifica el precio
#         self.imagen = nueva_imagen_ruta
    
#     def mostrar_imagen(self):
#         plt.imshow(self.imagen)
#         plt.axis('off')
#         plt.show()

# curso = Curso(1, "Introduccion a Python", 30, 55000, "./assets/img/bg-1.png")
# print(f"{curso.codigo} | {curso.nombre} | {curso.cupos} | ${curso.precio} | {curso.imagen}")
# # para mostrar imagen
# # def mostrar_imagen(self):
# #         self.imagen.show()



from PIL import Image
import matplotlib.pyplot as plt

# clase Curso

class Curso:
    def __init__(self, codigo, nombre, cupos, precio, imagen_ruta):
        self.codigo = codigo           # Código 
        self.nombre = nombre           # Nombre curso
        self.cupos = cupos             # Cantidad disponible (stock)
        self.precio = precio           # Precio 
        self.imagen = Image.open(imagen_ruta)
    
    def modificar(self, nuevo_nombre, nuevo_cupos, nuevo_precio, nueva_imagen_ruta):
        self.nombre = nuevo_nombre              # Modifica la descripción
        self.cupos = nuevo_cupos                # Modifica la cantidad
        self.precio = nuevo_precio              # Modifica el precio
        self.imagen = Image.open(nueva_imagen_ruta)
    
    def mostrar_imagen(self):
        plt.imshow(self.imagen)
        plt.axis('off')
        plt.show()


class Inventario:
    def __init__(self):
        self.cursos = []

    # Método para crear objetos de la clase "Curso" y agregarlos al inventario. Es la "C" (create) de CRUD
    def agregar_curso(self, codigo, nombre, cupos, precio, imagen_ruta):
        nuevo_curso = Curso(codigo, nombre, cupos, precio, imagen_ruta)
        self.cursos.append(nuevo_curso)  # Agrega un nuevo producto a la lista
    
    # Método para obtener objetos de la clase "Curso" y agregarlos al inventario. Es la "R" (read) de CRUD
    def consultar_curso(self, codigo):
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso # Retorna un objeto
        return False
    
    # Método para modificar objetos de la clase "Curso" y agregarlos al inventario. Es la "U" (update) de CRUD
    def modificar_curso(self, codigo, nuevo_nombre, nuevo_cupos, nuevo_precio, nueva_imagen_ruta):
        curso = self.consultar_curso(codigo)
        if curso:
            curso.modificar(nuevo_nombre,nuevo_cupos, nuevo_precio, nueva_imagen_ruta)

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
        print("Lista de cursos en el inventario:")
        print("Código\tNombre del curso\tCupos disponibles\tPrecio\timagen")
        for curso in self.cursos:
            print(f'{curso.codigo}\t{curso.nombre}\t{curso.cupos}\t{curso.precio}\t.{curso.imagen_ruta}')
            curso.mostrar_imagen()
        print("#" * 50)

# ...

#probar clase Inventario
mi_inventario = Inventario()

mi_inventario.agregar_curso(1, "Introduccion a Python", 30, 50000, "./assets/img/bg-1.png")
mi_inventario.agregar_curso(2, "Introduccion a Javascript", 40, 30000, "./assets/img/bg-1.png")
mi_inventario.agregar_curso(3, "Introduccion a HTML", 60, 35000, "./assets/img/bg-1.png")
mi_inventario.agregar_curso(4, "Introduccion a CSS", 65, 45000, "./assets/img/bg-1.png")

curso = mi_inventario.consultar_curso(3)
if curso != False:
    print(f'Curso encontrado:\nCodigo: {curso.codigo}\nTitulo: {curso.nombre}\nCantidad: {curso.cupos}\nPrecio: ${curso.precio}')
else:
    print("Curso no encontrado.")







"""
    Probar programa principal:

curso = Curso(1, "Introduccion a Python", 30, 55000, "./assets/img/bg-1.png")
print(f"{curso.codigo} | {curso.nombre} | {curso.cupos} | ${curso.precio}")
curso.mostrar_imagen()

"""