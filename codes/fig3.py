# === IMPORTS ===
import matplotlib.pyplot as plt
import numpy as np

# === PARÁMETROS DEL GRÁFICO ===
categorias = ['Telemetry Analysis', 'Satellite Command', 'Anomaly Resolution']
tiempos_gui = [75, 60, 85]
tiempos_script = [50, 35, 45]
tiempos_llm = [50, 15, 25]

# Colores (ajustados a los requerimientos técnicos y fidelidad visual)
color_gui = "#2365a6"
color_script = "#808080"
color_llm = "#4d9078"

# Estilos
ancho_barra = 0.25
x = np.arange(len(categorias))

# === FIGURA ===
fig, ax = plt.subplots(figsize=(10, 8))

# Dibujo de barras
bar1 = ax.bar(x - ancho_barra, tiempos_gui, ancho_barra, label='Traditional GUI', color=color_gui)
bar2 = ax.bar(x, tiempos_script, ancho_barra, label='Script-based', color=color_script)
bar3 = ax.bar(x + ancho_barra, tiempos_llm, ancho_barra, label='Proposed LLM', color=color_llm)

# Etiquetas de datos sobre barras
def etiquetas_barra(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=12)

etiquetas_barra(bar1)
etiquetas_barra(bar2)
etiquetas_barra(bar3)

# Configuración de ejes
ax.set_ylabel('Resolution Time (seconds)', fontsize=14, labelpad=15)
ax.set_xlabel('\nOperational Task Categories', fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(categorias, fontsize=12)
ax.set_ylim(0, 90)
ax.set_yticks(np.arange(0, 91, 10))
ax.tick_params(axis='both', which='major', labelsize=12)

# Grilla y bordes
ax.yaxis.grid(True, linestyle='-', which='major', color='gray', alpha=0.7)
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Leyenda
ax.legend(frameon=False, fontsize=12, loc='upper right')

# === RENDER ===
plt.tight_layout()
plt.show()