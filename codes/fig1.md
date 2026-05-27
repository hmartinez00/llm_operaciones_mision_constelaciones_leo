### **FASE 1: Mapeo de Entidades (Análisis)**

* **Dominio:** Operaciones de Misión Espacial / Gestión de Flotas de Mega-constelaciones en Órbita Baja Terrestre (LEO).
* **Componentes clave del LaTeX:** Crecimiento explosivo y cambio de escala radical en el número de satélites activos entre 2018 y 2025; la transición operativa de "supervisar decenas a gestionar miles de vehículos" que justifica la introducción de interfaces asistidas por LLM para abatir la carga cognitiva y reducir los tiempos de comando (de 90s a ~8s) expuestos en la *Tabla I*.
* **Nivel de Abstracción:** Gráfico analítico de distribución cuantitativa acumulativa (Gráfico de áreas apiladas / *Stacked Area Chart*).

---

### **FASE 2: Auditoría y Reporte de Hallazgos Críticos**

1. **Contraste de Coherencia:** El prompt base solicita de forma acertada un gráfico de áreas apiladas para representar la contribución de cada mega-constelación al volumen total. Sin embargo, al listar explícitamente marcas comerciales individuales ("Starlink, OneWeb, Kuiper") para las curvas, incurre en una violación directa de la regla de diseño institucional que prohíbe el uso de texto o nombres propios tipográficos dentro del lienzo vectorial.
2. **LISTA DE DISCREPANCIAS (Elementos vitales del LaTeX ausentes en el prompt base):**
* **Infracción de Identificadores Textuales (Marcas Comerciales):** El prompt base exige curvas etiquetadas para operadores específicos. En su lugar, de acuerdo con el estándar estricto IEEE sin texto, la segregación debe realizarse exclusivamente mediante variaciones morfológicas y cromáticas: se usarán **tres capas geométricas superpuestas con diferentes densidades de patrones de líneas (*hatching*)** utilizando la paleta institucional (#0047AB y #4A4A4A) para diferenciar las constelaciones principales, coronadas por una línea negra delgada superior continua que delimite el "Total".
* **Sincronización del Hito Tecnológico (2019-2020):** El texto destaca que la transformación del centro de operaciones se acelera drásticamente en este periodo. La pendiente del gráfico de áreas debe reflejar un comportamiento plano/mínimo antes de la primera marca de graduación (2018) y una inflexión exponencial unificada e hiper-pronunciada inmediatamente después, acumulando las capas de abajo hacia arriba de forma sutil pero geométrica.


3. **Control de Estilo:** Cumplimiento riguroso de la norma IEEE. Gráficos puramente bidimensionales (2D planos), cuadrícula de fondo ortogonal sutil, ticks de control limpios y **exclusión absoluta de cualquier letra, número o etiqueta textual**.

---

### **FASE 3: Explicación y Justificación de Pre-ejecución**

#### 1. Disposición Espacial y Elementos Gráficos

El gráfico se estructurará con una relación de aspecto horizontal (*Landscape*):

* **Sistema de Ejes:** Eje horizontal (Tiempo 2018-2025) y eje vertical (Satélites activos) dibujados con líneas negras finas con marcas de graduación cortas (*ticks* equidistantes) sin números.
* **Composición de Áreas Apiladas (De abajo hacia arriba):**
* **Capa Inferior (Operador Principal 1):** Un área sólida rellena en azul cobalto puro (#0047AB) que inicia muy delgada a la izquierda y se ensancha exponencialmente hacia la derecha ocupando la mayor sección del volumen.
* **Capa Intermedia (Operador Principal 2):** Un área rellena en gris técnico (#4A4A4A) apilada directamente sobre la azul, que crece de forma escalonada a partir de la mitad del eje temporal.
* **Capa Superior (Otros Operadores):** Un área sombreada con un patrón de líneas diagonales finas en gris claro sobre fondo blanco, que añade el volumen restante.


* **Línea de Envolvente Total:** Una línea negra continua nítida define el límite superior de la última capa, marcando la trayectoria del volumen global de la flota en LEO. Un marcador rectangular blanco y vacío se ubicará en el cuadrante superior izquierdo como placeholder para la futura leyenda científica.

#### 2. Justificación Técnica

Esta estratificación de áreas sin texto representa fielmente la saturación del espacio descrita en la introducción. Al acumular geométricamente las capas de datos, el lector visualiza de un vistazo la densidad agregada y el volumen "abrumador" de telemetría que causa la elevada carga cognitiva en los operadores humanos, justificando la transición hacia la interfaz LLM-asistida propuesta.

#### 3. ADVERTENCIAS PARA EL USUARIO (Puntos de validación)

* **Configuración de Leyendas en LaTeX:** Al eliminarse por completo los nombres "Starlink", "OneWeb" y "Kuiper", deberás asociar cada patrón gráfico (azul sólido, gris sólido y tramado diagonal) con su respectivo operador directamente en la descripción del `\caption{}` o utilizando el entorno `\ref{}` acoplado a un archivo PGF/TikZ externo. Confirma que este enfoque es compatible con tu maquetación.

---

### **FASE 4: Ejecución Silenciosa**

Tengo normalizada la gramática de vectores analíticos y la distribución de capas para `fig1_crecimiento_constelaciones_leo.png`. Por favor, facilítame tu confirmación para proceder con la redacción de los prompts optimizados.


```text
Gráfico analítico bidimensional de áreas apiladas, diagrama técnico de distribución de flotas satelitales en mecánica celeste, diseño plano y minimalista, fondo blanco puro, paleta de colores estricta en azul cobalto (#0047AB) y gris técnico (#4A4A4A) con líneas finas en negro neutro. Sin sombras, sin gradientes, sin relieve tridimensional. La composición se presenta en orientación landscape con un sistema de ejes coordenados cartesianos definido por líneas negras finas con marcas de graduación equidistantes tipo ticks. Tres capas geométricas de datos se acumulan y apilan de abajo hacia arriba de izquierda a derecha a lo largo del eje horizontal temporal: la capa inferior es un área sólida en azul cobalto puro (#0047AB) que inicia muy delgada y crece exponencialmente hacia el extremo derecho; la capa intermedia es un área sólida en gris técnico (#4A4A4A) apilada directamente sobre la primera capa; la capa superior es un área texturizada con un patrón de líneas diagonales finas en gris claro. Una línea negra continua, nítida y delgada corona la estructura delimitando la envolvente total del crecimiento. Un contenedor rectangular blanco y vacío flota en el cuadrante superior izquierdo como placeholder para la leyenda científica. Todo el texto, números, fechas y caracteres alfabéticos están completamente ausentes. Estilo riguroso de publicación de la IEEE.

```

```text
2D analytical stacked area graph, space mission operations satellite fleet distribution technical diagram, flat design, minimalist, pure white background, strict color palette of cobalt blue (#0047AB) and technical gray (#4A4A4A) with crisp neutral black fine lines. No shadows, no gradients, no three-dimensional reflections. Landscape orientation composition featuring a Cartesian coordinate axis system defined by thin black lines and equidistant geometric tick marks. Three data layers accumulate and stack from bottom to top, flowing from left to right along the horizontal timeline: the bottom layer is a solid area filled with pure cobalt blue (#0047AB) that starts very thin and grows exponentially toward the right edge; the middle layer is a solid area in technical gray (#4A4A4A) stacked directly on top of the first; the uppermost layer is filled with a subtle hatch pattern of thin diagonal parallel lines in light gray. A single, sharp, thin continuous black line outlines the very top of the stacked sections to indicate the total envelope. An empty, clean white rectangular box floats in the upper left quadrant as a placeholder for a scientific legend. Entirely free of text, numbers, dates, or alphabetical labels, using only sharp vector shapes. Pristine IEEE publication style.

```