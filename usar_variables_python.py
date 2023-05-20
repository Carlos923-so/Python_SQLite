import sqlite3
import time

conexion = sqlite3.connect('Ejemplo.db')
c=conexion.cursor()

fecha=time.ctime()
operacion='compra'
simbolo='IBM'
cantidad=50
precio=13.23

movimientos=[(fecha,operacion,simbolo,cantidad,precio)]
c.executemany("INSERT INTO acciones VALUES (?,?,?,?,?)",movimientos)
conexion.commit()
conexion.close()