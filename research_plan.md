**PARTE 1: ESTRUCTURA JSON**

```json
{
  "titulo": "Uso de Modelos de Lenguaje Grande (LLM) para Operaciones de Misión en Constelaciones LEO: Control Intuitivo y Reducción de Errores Humanos",
  "folder_name": "llm_operaciones_mision_constelaciones_leo",
  "abstract_preliminar": "El creciente número y complejidad de mega-constelaciones en órbita baja terrestre (LEO) exige operadores de misión más eficientes y resilientes. Este artículo explora el uso de Modelos de Lenguaje Grande (LLM) como interfaz de control intuitivo y agente de apoyo en operaciones de misión, facilitando la generación de comandos, diagnóstico de anomalías y toma de decisiones en lenguaje natural. Se propone una arquitectura agente LLM-aumentada que integra telemetría en tiempo real con razonamiento en lenguaje, evaluada en entornos de simulación de alta fidelidad. Los resultados demuestran mejoras significativas en tiempo de respuesta, reducción de errores humanos y usabilidad para operadores. Se discuten implicaciones para la autonomía en operaciones de constelaciones, desafíos de confiabilidad y caminos hacia implementación en vuelo, contribuyendo al avance de sistemas de operación de misión más intuitivos y seguros.",
  "secciones": [
    {
      "nro": 1,
      "titulo_seccion": "Introducción",
      "objetivos": ["Contextualizar la complejidad operativa de mega-constelaciones LEO", "Presentar el potencial de LLM para control intuitivo en operaciones de misión", "Definir objetivos e hipótesis de la investigación"],
      "subsecciones": ["1.1 Motivación y Problema de Investigación", "1.2 Contribuciones del Trabajo", "1.3 Estructura del Artículo"],
      "insumos": ["Figura 1: Crecimiento de constelaciones LEO", "Tabla 1: Comparativa de interfaces de control"],
      "llaves_bibtex": ["rodriguez2024llm", "schefels2024evaluating", "carrasco2025llm"]
    },
    {
      "nro": 2,
      "titulo_seccion": "Estado del Arte",
      "objetivos": ["Revisar aplicaciones de LLM en operaciones espaciales", "Analizar enfoques existentes de agentes autónomos", "Identificar gaps en control intuitivo y reducción de errores"],
      "subsecciones": ["2.1 LLM en Operaciones Espaciales", "2.2 Agentes Autónomos en Control de Satélites", "2.3 Interfaces Hombre-Máquina en Misiones"],
      "insumos": ["Tabla 2: Comparativa de enfoques LLM"],
      "llaves_bibtex": ["rodriguez2024llm", "schefels2024evaluating", "maranto2024llmsat"]
    },
    {
      "nro": 3,
      "titulo_seccion": "Arquitectura Propuesta",
      "objetivos": ["Diseñar framework LLM-aumentado para operaciones de misión", "Integrar telemetría en prompts y razonamiento", "Definir flujo de control intuitivo"],
      "subsecciones": ["3.1 Arquitectura General del Sistema", "3.2 Procesamiento de Telemetría y Prompt Engineering", "3.3 Módulo de Generación de Comandos"],
      "insumos": ["Figura 2: Diagrama de arquitectura LLM", "Eq. 1: Estructura de prompt"],
      "llaves_bibtex": ["carrasco2025llm", "schefels2024evaluating"]
    },
    {
      "nro": 4,
      "titulo_seccion": "Metodología y Implementación",
      "objetivos": ["Detallar técnicas de fine-tuning y prompting", "Describir entorno de simulación", "Definir métricas de evaluación"],
      "subsecciones": ["4.1 Fine-tuning y Prompt Engineering", "4.2 Entorno de Simulación", "4.3 Métricas de Rendimiento"],
      "insumos": [],
      "llaves_bibtex": ["maranto2024llmsat", "rodriguez2024llm"]
    },
    {
      "nro": 5,
      "titulo_seccion": "Resultados y Análisis",
      "objetivos": ["Presentar resultados experimentales", "Comparar con métodos tradicionales", "Analizar reducción de errores humanos"],
      "subsecciones": ["5.1 Resultados Cuantitativos", "5.2 Análisis Cualitativo de Usabilidad", "5.3 Análisis de Sensibilidad"],
      "insumos": ["Figura 3: Comparativa de tiempo de respuesta", "Tabla 3: Métricas de error"],
      "llaves_bibtex": ["carrasco2025llm", "schefels2024evaluating"]
    },
    {
      "nro": 6,
      "titulo_seccion": "Discusión",
      "objetivos": ["Interpretar hallazgos en contexto operativo", "Analizar limitaciones y riesgos", "Evaluar impacto en operaciones de constelaciones"],
      "subsecciones": ["6.1 Implicaciones Operativas", "6.2 Limitaciones Técnicas y de Confiabilidad", "6.3 Consideraciones de Seguridad"],
      "insumos": ["Tabla 4: Comparativa de enfoques"],
      "llaves_bibtex": ["rodriguez2024llm", "maranto2024llmsat"]
    },
    {
      "nro": 7,
      "titulo_seccion": "Conclusiones y Trabajos Futuros",
      "objetivos": ["Sintetizar aportes principales", "Destacar contribuciones a la reducción de errores", "Proponer líneas de investigación futuras"],
      "subsecciones": ["7.1 Conclusiones", "7.2 Trabajos Futuros"],
      "insumos": [],
      "llaves_bibtex": ["carrasco2025llm", "schefels2024evaluating"]
    }
  ]
}
```

**PARTE 2: BLOQUES BIBLIOGRÁFICOS SECCIONALES**

```bibtex
@article{rodriguez2024llm,
  author    = {Rodriguez-Fernandez, V. and others},
  title     = {Language Models are Spacecraft Operators},
  journal   = {arXiv preprint arXiv:2404.00413},
  year      = {2024},
  doi       = {10.48550/arXiv.2404.00413},
  url       = {https://arxiv.org/pdf/2404.00413},
  note      = {[Online]. Available: https://arxiv.org/abs/2404.00413}
}

@article{schefels2024evaluating,
  author    = {Schefels, C. and Hartmann, C. and Helmsauer, K. and Schlag, L.},
  title     = {Evaluating Large Language Models for Space Operations},
  journal   = {German Aerospace Center (DLR), GSOC},
  year      = {2024},
  url       = {https://elib.dlr.de/210113/1/evaluating_large_language_models_for_space_operations.pdf},
  note      = {[Online]. Available: https://elib.dlr.de/210113/1/evaluating_large_language_models_for_space_operations.pdf}
}

@article{carrasco2025llm,
  author    = {Carrasco, A. and Rodriguez-Fernandez, V. and Linares, R.},
  title     = {Large Language Models as Autonomous Spacecraft Operators in Kerbal Space Program},
  journal   = {Advances in Space Research},
  year      = {2025},
  doi       = {10.1016/j.asr.2025.XX.XXX},
  url       = {https://arxiv.org/pdf/2505.19896},
  note      = {[Online]. Available: https://arxiv.org/abs/2505.19896}
}
```

```bibtex
@article{maranto2024llmsat,
  author    = {Maranto, D. and others},
  title     = {LLMSat: A Large Language Model-Based Goal-Oriented Agent for Autonomous Space Exploration},
  journal   = {arXiv preprint arXiv:2405.01392},
  year      = {2024},
  doi       = {10.48550/arXiv.2405.01392},
  url       = {https://arxiv.org/pdf/2405.01392},
  note      = {[Online]. Available: https://arxiv.org/abs/2405.01392}
}
```

**PARTE 3: MAPA DE USO DE REFERENCIAS (POR SECCIÓN)**

```json
{
  "seccion_nro": 1,
  "titulo_seccion": "Introducción",
  "mapa_uso": {
    "rodriguez2024llm": {
      "razon_seleccion": "Estudio pionero que demuestra LLMs como operadores de naves espaciales.",
      "guia_redaccion": "Usar en 1.1 para motivar el potencial de LLMs en control intuitivo y citar resultados en simulaciones.",
      "subseccion_destino": "1.1"
    },
    "schefels2024evaluating": {
      "razon_seleccion": "Evaluación práctica de LLMs en operaciones reales del GSOC.",
      "guia_redaccion": "Integrar en 1.2 para destacar reducción de carga cognitiva y errores humanos.",
      "subseccion_destino": "1.2"
    },
    "carrasco2025llm": {
      "razon_seleccion": "Aplicación reciente de LLMs en control autónomo de satélites.",
      "guia_redaccion": "Mencionar en 1.1 como evidencia de viabilidad técnica.",
      "subseccion_destino": "1.1"
    }
  }
}
```

```json
{
  "seccion_nro": 2,
  "titulo_seccion": "Estado del Arte",
  "mapa_uso": {
    "rodriguez2024llm": {
      "razon_seleccion": "Marco conceptual de LLMs como operadores.",
      "guia_redaccion": "Citar en 2.2 para contrastar con enfoques RL tradicionales.",
      "subseccion_destino": "2.2"
    },
    "schefels2024evaluating": {
      "razon_seleccion": "Estudio de caso en centro de operaciones real.",
      "guia_redaccion": "Usar en 2.1 para ejemplos de recuperación de información y diagnóstico.",
      "subseccion_destino": "2.1"
    },
    "maranto2024llmsat": {
      "razon_seleccion": "Agente goal-oriented basado en LLM para exploración espacial.",
      "guia_redaccion": "Contrastar en 2.3 con interfaces tradicionales.",
      "subseccion_destino": "2.3"
    }
  }
}
```

```json
{
  "seccion_nro": 3,
  "titulo_seccion": "Arquitectura Propuesta",
  "mapa_uso": {
    "carrasco2025llm": {
      "razon_seleccion": "Arquitectura LLM para control en tiempo real.",
      "guia_redaccion": "Base para 3.1 y 3.3, citando flujo de telemetría a comandos.",
      "subseccion_destino": "3.1"
    },
    "schefels2024evaluating": {
      "razon_seleccion": "Lecciones de implementación en entornos operativos.",
      "guia_redaccion": "Integrar en 3.2 para prompt engineering y manejo de datos sensibles.",
      "subseccion_destino": "3.2"
    }
  }
}
```

```json
{
  "seccion_nro": 4,
  "titulo_seccion": "Metodología y Implementación",
  "mapa_uso": {
    "maranto2024llmsat": {
      "razon_seleccion": "Diseño de agente goal-oriented con LLM.",
      "guia_redaccion": "Usar en 4.1 para detalles de fine-tuning y razonamiento.",
      "subseccion_destino": "4.1"
    },
    "rodriguez2024llm": {
      "razon_seleccion": "Implementación en simulador KSP.",
      "guia_redaccion": "Referenciar en 4.2 para entorno de simulación.",
      "subseccion_destino": "4.2"
    }
  }
}
```

```json
{
  "seccion_nro": 5,
  "titulo_seccion": "Resultados y Análisis",
  "mapa_uso": {
    "carrasco2025llm": {
      "razon_seleccion": "Resultados en desafíos de control de satélites.",
      "guia_redaccion": "Comparar métricas de rendimiento en 5.1.",
      "subseccion_destino": "5.1"
    },
    "schefels2024evaluating": {
      "razon_seleccion": "Evaluación de usabilidad en operaciones reales.",
      "guia_redaccion": "Citar en 5.2 para análisis de reducción de errores.",
      "subseccion_destino": "5.2"
    }
  }
}
```

```json
{
  "seccion_nro": 6,
  "titulo_seccion": "Discusión",
  "mapa_uso": {
    "rodriguez2024llm": {
      "razon_seleccion": "Limitaciones observadas en control autónomo.",
      "guia_redaccion": "Discutir desafíos en 6.2.",
      "subseccion_destino": "6.2"
    },
    "maranto2024llmsat": {
      "razon_seleccion": "Enfoque en autonomía goal-oriented.",
      "guia_redaccion": "Usar en 6.1 para implicaciones operativas.",
      "subseccion_destino": "6.1"
    }
  }
}
```

```json
{
  "seccion_nro": 7,
  "titulo_seccion": "Conclusiones y Trabajos Futuros",
  "mapa_uso": {
    "carrasco2025llm": {
      "razon_seleccion": "Resultados en simulaciones de operaciones.",
      "guia_redaccion": "Sintetizar contribuciones en 7.1.",
      "subseccion_destino": "7.1"
    },
    "schefels2024evaluating": {
      "razon_seleccion": "Lecciones prácticas de despliegue.",
      "guia_redaccion": "Proponer extensiones en 7.2 basadas en entornos reales.",
      "subseccion_destino": "7.2"
    }
  }
}
```

Listo. ¿Quieres que comencemos directamente con el **SPRINT DE ESCRITURA: SECCIÓN 1**?