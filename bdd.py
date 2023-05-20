import sqlite3
conexion = sqlite3.connect('Ejemplo.db')
c = conexion.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS acciones (fecha text, operacion text, simbolo text, cantidad real, precio real)''')

c.execute("INSERT INTO acciones VALUES ('24/nov/2016','compra','INV',100,15.43)")
registros = [
    ('25/nov/2016', 'venta', 'AAPL', 50, 20.15),
    ('26/nov/2016', 'compra', 'GOOG', 75, 30.50),
    ('27/nov/2016', 'venta', 'MSFT', 80, 35.25),
    ('28/nov/2016', 'compra', 'AMZN', 60, 40.10),
    ('29/nov/2016', 'venta', 'FB', 45, 22.80)
]

c.executemany("INSERT INTO acciones VALUES (?, ?, ?, ?, ?, ?, ?)", registros)

conexion.commit()

conexion.close()