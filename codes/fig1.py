# === IMPORTS ===
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# === PARÁMETROS DEL GRÁFICO ===
# Ejes y límites
x_min, x_max = 2018, 2025
y_min, y_max = 0, 8000
x_ticks = list(range(2018, 2026))
y_ticks = list(range(0, 8001, 1000))
y_tick_labels = [str(y) if y != 8000 else "8000+" for y in y_ticks]

# Etiquetas y textos
y_label = "Satellite volume"
anno1_text = "Inicio despliegue\nStarlink (2019)"
anno2_text = "Aceleración\nOneWeb"
anno3_text = "Primeros\nlanzamientos Kuiper"

# Coordenadas de anotaciones (texto_xy, flecha_xy)
anno1_xytext = (2019.2, 2600)
anno1_xy = (2019.6, 600)
anno2_xytext = (2021.55, 4850)
anno2_xy = (2022.0, 3800)
# ASUNCIÓN: La flecha 3 se fuerza a apuntar a la capa gris oscura para ser fiel a la imagen generada (alucinación visual), 
# aunque lógicamente Kuiper sea la capa gris clara inferior.
anno3_xytext = (2023.6, 7500)
anno3_xy = (2024.8, 7200)

# Colores y estilos
color_starlink = "#0047AB"  # Azul cobalto
color_oneweb = "#555555"    # Gris oscuro
color_kuiper = "#888888"    # Gris claro
color_grid = "black"
color_bg = "white"

grid_linewidth = 1.2
spine_linewidth = 1.5
font_size_labels = 16
font_size_ticks = 14
font_size_anno = 11
font_size_legend = 14

# === DATOS ===
# Eje temporal
x_data = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])

# Cargas individuales por capa (ordenadas de abajo hacia arriba: Kuiper, Starlink, OneWeb)
# Los valores están ajustados para recrear la forma exacta de la curva acumulada visible en la imagen.
y_kuiper = np.array([0, 0, 0, 0, 0, 50, 200, 900])
y_starlink = np.array([0, 100, 1600, 2600, 3200, 4200, 5100, 6100])
y_oneweb = np.array([0, 0, 100, 400, 500, 650, 750, 800])

# === FIGURA ===
# Configuración base del lienzo
fig, ax = plt.subplots(figsize=(11, 6.5), facecolor=color_bg)

# Dibujo de las áreas apiladas
ax.stackplot(x_data, y_kuiper, y_starlink, y_oneweb, 
             colors=[color_kuiper, color_starlink, color_oneweb],
             linewidth=0)

# Construcción manual de la leyenda para respetar el orden visual y colores de los cuadrados
patch_starlink = mpatches.Patch(facecolor=color_starlink, edgecolor='black', label='Starlink')
patch_oneweb = mpatches.Patch(facecolor=color_oneweb, edgecolor='black', label='OneWeb')
patch_kuiper = mpatches.Patch(facecolor=color_kuiper, edgecolor='black', label='Kuiper')

ax.legend(handles=[patch_starlink, patch_oneweb, patch_kuiper],
          loc='upper left', frameon=True, edgecolor='black', 
          framealpha=1.0, fontsize=font_size_legend, borderpad=0.6,
          handlelength=1.5, handleheight=1.0)

# Configuración de ejes y límites
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.set_yticklabels(y_tick_labels)
ax.tick_params(axis='both', which='major', labelsize=font_size_ticks, length=6, width=spine_linewidth)
ax.set_ylabel(y_label, fontsize=font_size_labels)

# Configuración de grilla superpuesta (visible sobre las áreas de color)
ax.set_axisbelow(False)
ax.grid(True, color=color_grid, linestyle='-', linewidth=grid_linewidth)

# Grosor y color de los bordes del gráfico
for spine in ax.spines.values():
    spine.set_linewidth(spine_linewidth)
    spine.set_color('black')

# Inserción de anotaciones 
ax.annotate(anno1_text, xy=anno1_xy, xytext=anno1_xytext,
            arrowprops=dict(arrowstyle='-', color='black', lw=0.8),
            ha='center', va='center', fontsize=font_size_anno)

ax.annotate(anno2_text, xy=anno2_xy, xytext=anno2_xytext,
            arrowprops=dict(arrowstyle='-', color='black', lw=0.8),
            ha='center', va='center', fontsize=font_size_anno)

ax.annotate(anno3_text, xy=anno3_xy, xytext=anno3_xytext,
            arrowprops=dict(arrowstyle='-', color='black', lw=0.8),
            ha='center', va='center', fontsize=font_size_anno)

# === RENDER ===
plt.tight_layout()
plt.show()