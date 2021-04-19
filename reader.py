# creamos listas donde almacenar nuestros datos
x = []
y = []

# abrimos y leemos el archivo de datos
data_file = open("archivo.txt", "r")
lines = data_file.readlines()

for i in range(0, len(lines), 1):
    # dividimos cada linea en los 2 datos (estan seperados por "\t")
    position_1 = lines[i].find("\t")
    position_2 = lines[i].find("\t", position_1 + 1)

    # almacenamos el valor de los datos
    data_1 = float(lines[i][0:position_1])
    data_2 = float(lines[i][position_1 + 1:position_2])

    # añadimos a la lista correspondiente cada uno de los valores
    x.append(data_1)
    y.append(data_2)
