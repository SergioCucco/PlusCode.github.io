"""
Hay que instalar en la terminal lo siguiente: 
pip install pillow
pip install matplotlib
"""
import sqlite3
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

DATABASE = "cursos_inventario.db"

def obtener_db_conexion():
    print("Conectando...")
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = obtener_db_conexion()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cursos (
        codigo INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        cupos INTEGER NOT NULL,
        precio REAL NOT NULL,
        duracion INTEGER NOT NULL,
        imagen_ruta TEXT NOT NULL
    )""")
    conn.commit()
    cursor.close()
    conn.close()

def create_database():
    conn = sqlite3.connect(DATABASE)
    conn.close()
    create_table()

create_database()

# clase Curso

class Curso:
    def __init__(self, codigo, nombre, cupos, precio, duracion, imagen_ruta):
        self.codigo = codigo           
        self.nombre = nombre           
        self.cupos = cupos             
        self.precio = precio           
        self.duracion = duracion
        self.imagen_ruta = imagen_ruta
    
    def modificar(self, nuevo_nombre, nuevo_cupos, nuevo_precio, nueva_duracion, nueva_imagen_ruta):
        self.nombre = nuevo_nombre              # Modifica la descripción
        self.cupos = nuevo_cupos                # Modifica la cantidad
        self.precio = nuevo_precio              # Modifica el precio
        self.duracion = nueva_duracion
        self.imagen_ruta = nueva_imagen_ruta
    
    def obtener_imagen_ruta(self):
        return self.imagen_ruta
    
    def mostrar_imagen(self):
        return send_file(self.imagen_ruta, mimetype='image/jpg')


class Inventario:
    def __init__(self):
        self.cursos = []
        self.conexion = obtener_db_conexion()
        self.cursor = self.conexion.cursor()

    # Método para crear objetos de la clase "Curso" y agregarlos al inventario. Es la "C" (create) de CRUD
    def agregar_curso(self, codigo, nombre, cupos, precio, duracion, imagen_ruta):
        producto_existente = self.consultar_curso(codigo)
        if producto_existente:
            return jsonify({'message': 'Ya existe curso con el código ingresado'}), 400
        sql = f"INSERT INTO cursos VALUES({codigo}, '{nombre}', {cupos}, {precio}, {duracion}, '{imagen_ruta}';)"
        self.cursor.execute(sql)
        self.conexion.commit()
        return jsonify({'message': 'Curso agregado satisfactoriamente'}), 200
        # nuevo_curso = Curso(codigo, nombre, cupos, precio, duracion, imagen_ruta)
        # self.cursos.append(nuevo_curso)  # Agrega un nuevo producto a la lista
    
    # Método para obtener objetos de la clase "Curso" y agregarlos al inventario. Es la "R" (read) de CRUD
    def consultar_curso(self, codigo):
        sql = f"SELECT * FROM cursos WHERE codigo = {codigo}:"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        if row:
            codigo, nombre, cupos, precio, duracion, imagen_ruta = row
            return Curso(codigo, nombre, cupos, precio, duracion, imagen_ruta)
        return None
        # for curso in self.cursos:
        #     if curso.codigo == codigo:
        #         return curso # Retorna un objeto
        # return False
    
    # Método para modificar objetos de la clase "Curso" y agregarlos al inventario. Es la "U" (update) de CRUD
    def modificar_curso(self, codigo, nuevo_nombre, nuevo_cupos, nuevo_precio, nueva_duracion, nueva_imagen_ruta):
        curso = self.consultar_curso(codigo)
        if curso:
            # curso.modificar(nuevo_nombre,nuevo_cupos, nuevo_precio, nueva_duracion, nueva_imagen_ruta)
            curso.modificar(nuevo_nombre, nuevo_cupos, nuevo_precio, nueva_duracion, nueva_imagen_ruta)
            sql = f'UPDATE cursos SET nombre = "{nuevo_nombre}", cupos = {nuevo_cupos}, precio = {nuevo_precio}, duracion = {nueva_duracion}, imagen_ruta = "{nueva_imagen_ruta}";'
            self.cursor.execute(sql)
            self.conexion.commit()
            return jsonify({'message': 'Curso modificado satisfactoriamente.'}), 200
        return jsonify({'message': 'Curso no encontrado.'}), 400

    # Método para eliminar objetos de la clase "Curso" y agregarlos al inventario. Es la "D" (delete) de CRUD
    def eliminar_curso(self, codigo):
        sql = f'DELETE FROM cursos WHERE codigo = {codigo}'
        self.cursor.execute(sql)
        if self.cursor.rowcount > 0:
            self.conexion.commit()
            return jsonify({'message': 'Curso eliminado satisfactoriamente.'}), 200
        return jsonify({'message': 'Curso no encontrado.'}), 404
        # eliminar = False
        # for curso in self.cursos:
        #     if curso.codigo == codigo:
        #         eliminar = True
        #         curso_eliminar = curso      
        # if eliminar == True:
        #     self.cursos.remove(curso_eliminar)
        #     print(f'Curso {codigo} eliminado.')
        # else:
        #     print(f'Curso {codigo} no encontrado.')

    def listar_cursos(self):
        self.cursor.execute('SELECT * FROM cursos')
        rows = self.cursor.fetchall()
        cursos = []
        for row in rows:
            codigo, nombre, cupos, precio, duracion, imagen_ruta = row
            curso = {
            'codigo': codigo,
            'nombre': nombre,
            'cupos': cupos,
            'precio': precio,
            'duracion': duracion,
            'imagen_ruta': imagen_ruta
            }
            cursos.append(curso)
        return jsonify(cursos), 200
        # print("#" * 50)
        # print()
        # print(f"Lista de cursos en el inventario:\n")
        # print("Cod\tNombre del curso\tCupos disponibles\tPrecio\tDuracion\tRuta imagen")
        # for curso in self.cursos:
        #     print(f'{curso.codigo}\t\t{curso.nombre} |\t{curso.cupos} |\t${curso.precio} |\t{curso.duracion} |\t{curso.imagen.filename}')
        # curso.mostrar_imagen()
        # print()
        # print("#" * 50)


class Carrito:
    def __init__(self):
        self.conexion = obtener_db_conexion()
        self.cursor = self.conexion.cursor()
        self.items = []
    
    def agregar(self, codigo, inventario):
        curso = inventario.consultar_curso(codigo)
        if curso is None:
            return jsonify({'message': 'El curso no existe.'}), 404
        
        for curso_existente in self.items:
            if curso_existente.codigo == codigo:
                return jsonify({'message': 'El curso ya está en tu carrito.'}, 400)
        
        if curso.cupos > 0:
            nuevo_curso = Curso(codigo, curso.nombre, curso.cupos, curso.precio, curso.duracion, curso.imagen_ruta)
            self.items.append(nuevo_curso)
            sql = f'UPDATE cursos SET cupos -= 1 WHERE codigo = {codigo};'
            self.cursor.execute(sql)
            self.conexion.commit()
            return jsonify({'message': 'Curso agregado al carrito.'}), 200
        
        # if curso:
        #     for curso_existente in self.items:
        #         if curso_existente.codigo == codigo:
        #             print("El curso ya está en tu carrito")
        #             return
        #     if curso.cupos > 0:
        #         self.items.append(curso)
        #         print(f"El curso {curso.nombre} se ha agregado al carrito")
        #         curso.cupos -= 1
        #     else:
        #         print(f"No hay cupos disponibles para {curso.nombre}")
        # else:
        #     print("Curso no disponible")
    
    def sacar(self, codigo, inventario):
        for curso in self.items:
            if curso.codigo == codigo:
                curso.cupos += 1
                self.items.remove(curso)
                sql = f'UPDATE cursos SET cupos += 1 WHERE codigo = {codigo};'
                self.cursor.execute(sql)
                self.conexion.commit()
                return jsonify({'message': 'Curso sacado'}), 200
        
        return jsonify({'message': 'El curso no se encuentra en el carrito.'}), 404

    
    # def vaciar_carrito(self):
    #     self.items = []
    #     print("El carrito se ha vaciado.")
    
    def mostrar_carrito(self):
        productos_carrito = []
        for curso in self.items:
            curso = {'codigo': curso.codigo, 'nombre': curso.nombre, 'cupos': curso.cupos, 'precio': curso.precio, 'duracion': curso.duracion, 'Ruta imagen': curso.imagen_ruta}
            productos_carrito.append(curso)
        return jsonify(productos_carrito), 200
        # if self.items:
        #     print(f"Cursos en el carrito".center(30, "-"))
        #     for curso in self.items:
        #         print(f"- {curso.nombre}")
        # else:
        #     print("El carrito esta vacio")
    
    def calcular_total(self):
        total = 0
        for curso in self.items:
            total += curso.precio
        return total

app = Flask(__name__)
CORS(app, origins='*')

carrito = Carrito()
inventario = Inventario()

@app.route('/cursos/<int:codigo>', methods=['GET'])
def obtener_curso(codigo):
    curso = inventario.consultar_curso(codigo)
    if curso:
        return jsonify({
            'codigo': curso.codigo,
            'nombre': curso.nombre,
            'cupos': curso.cupos,
            'precio': curso.precio,
            'duracion': curso.duracion,
            'Ruta imagen': curso.imagen_ruta
        }), 200
    return jsonify({'message': 'Curso no encontrado.'}), 404

@app.route('/cursos', methods=['GET'])
def obtener_cursos():
    return inventario.listar_cursos()

@app.route('/cursos', methods=['POST'])
def agregar_curso():
    codigo = request.json.get('codigo')
    nombre = request.json.get('nombre')
    cupos = request.json.get('cupos')
    precio = request.json.get('precio')
    duracion = request.json.get('duracion')
    imagen_ruta = request.json.get('imagen_ruta')
    return inventario.agregar_curso(codigo, nombre, cupos, precio, duracion, imagen_ruta)

@app.route('/cursos/<int:codigo>', methods=['PUT'])
def modificar_curso(codigo):
    nuevo_nombre = request.json.get('nombre')
    nuevo_cupos = request.json.get('cupos')
    nuevo_precio = request.json.get('precio')
    nueva_duracion = request.json.get('duracion')
    nueva_imagen_ruta = request.json.get('imagen_ruta')
    return inventario.modificar_curso(codigo, nuevo_nombre, nuevo_cupos, nuevo_precio, nueva_duracion, nueva_imagen_ruta)

@app.route('/cursos/<int:codigo>', methods='DELETE')
def eliminar_curso(codigo):
    return inventario.eliminar_curso(codigo)

@app.route('/')
def index():
    return 'Api +Code'

@app.route('/carrito', methods=['POST'])
def agregar_carrito():
    codigo = request.json.get('codigo')
    inventario = Inventario()
    return carrito.agregar(codigo, inventario)

@app.route('/carrito', methods=['DELETE'])
def sacar_carrito():
    codigo = request.json.get('codigo')
    inventario = Inventario()
    return carrito.sacar(codigo, inventario)

@app.route('/carrito', methods=['GET'])
def obtener_carrito():
    return carrito.mostrar_carrito()

if __name__ == '__main__':
    app.run()