import sqlite3
conexion = sqlite3.connect('Ejemplo.db')
c = conexion.cursor()

movimientos = [
    ('24/nov/2016', 'venta', 'HPC', 50, 20.01),
    ('25/nov/2016', 'compra', 'SNY', 100, 7.18),
    ('26/nov/2016', 'compra', 'XBX', 75, 5.33),
]

c.executemany("INSERT INTO acciones VALUES (?, ?, ?, ?, ?)", movimientos)

conexion.commit()

for row in c.execute("SELECT * FROM acciones"):
    print(row)

conexion.close()