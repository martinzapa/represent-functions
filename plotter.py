import numpy as np
import matplotlib.pyplot as plt

# ******************************************************************************
# funcion a representar
def f1(x):
    return np.sin(x)

x = np.linspace(-5, 5, 1000)

# ******************************************************************************
# parametros para la representacion grafica
xmin = -5
xmax = 5
xpaso = 0.5
x_subpaso = 2
ymin = -2
ymax = 2
ypaso = 0.5
y_subpaso = 2

# ******************************************************************************
# calculos para setear ejes
majorx = int((xmax - xmin) / xpaso) + 1
majory = int((ymax - ymin) / ypaso) + 1
minorx = x_subpaso*(int((xmax - xmin) / xpaso)) + 1
minory = y_subpaso*(int((ymax - ymin) / ypaso)) + 1
# ******************************************************************************
fig = plt.figure()
ax = fig.add_subplot(111)

# malla de la grafica
ax.grid(True, which = 'major', linestyle = '--', color = 'black', alpha = 0.7)
ax.grid(True, which = 'minor', linestyle = '--', color = 'black', alpha = 0.3)

# ejes y ticks (limites y titulos y formato)
ax.set_title('titulo', pad = 20, size = 15)
ax.set_xlabel('titulo_eje_x', labelpad = 10, size = 10)
ax.set_xlim(xmin, xmax)
ax.set_ylabel('titulo_eje_y', labelpad = 15, rotation = 90, size = 10)
ax.set_ylim(ymin, ymax)
major_xticks = np.linspace(xmin, xmax, majorx)
major_yticks = np.linspace(ymin, ymax, majory)
minor_xticks = np.linspace(xmin, xmax, minorx)
minor_yticks = np.linspace(ymin, ymax, minory)

ax.tick_params(axis = 'both', which = 'major', labelsize = 6)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 0)

ax.tick_params(axis = 'both', which = 'major', labelbottom = True,
                labeltop = False, labelleft = True, labelright = True,
                bottom = True, top = True, left = True, right = True)
ax.tick_params(axis = 'both', which = 'minor', labelbottom = False,
                labeltop = False, labelleft = False, labelright = False,
                bottom = True, top = True, left = True, right = True)

ax.tick_params(which = 'both', direction = 'out')

ax.set_xticks(major_xticks)
ax.set_xticks(minor_xticks, minor = True)

ax.set_yticks(major_yticks)
ax.set_yticks(minor_yticks, minor = True)

# plots
ax.plot(x, f1(x), 'r', label= 'etiqueta_datos_1', linewidth = 0.5)
ax.set_aspect('equal')

# leyenda y displayer
ax.legend()
#fig.savefig('imagen.png') # descomentar para guardar la imagen
plt.show()