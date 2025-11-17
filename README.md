# 📊 Práctica 03 – Calidad de Software  
## Análisis y pruebas sobre datos del SRI (Python)

Este proyecto implementa un analizador de datos basado en un archivo CSV del SRI (ventas, exportaciones e importaciones). Se incluyen:

- Lectura robusta de datos.
- Cálculo de estadísticas por provincia.
- Consultas interactivas desde consola.
- Pruebas unitarias con `unittest`.
- Revisión de calidad mediante `coverage`.

---

## 📁 Estructura del proyecto

Practica03-calidad/
│
├── app.py
├── README.md
├── datos/
│ └── sri_ventas_2024.csv
│
├── src/
│ └── procesador.py
│
└── test/
└── test_procesador.py

## 🧠 Funcionalidades principales

### ✔ 1. Ventas totales por provincia  
El sistema suma la columna **TOTAL_VENTAS** agrupada por provincia.

### ✔ 2. Ventas para una provincia específica  
Permite ingresar el nombre de una provincia y ver sus ventas.

### ✔ 3. Exportaciones totales por mes  
Usa las columnas **EXPORTACIONES**, **MES** o **PERIODO**.

### ✔ 4. Porcentaje de ventas tarifa 0%  
Calcula:

\[
(VENTAS\_NETAS\_TARIFA\_0 / TOTAL\_VENTAS) * 100
\]

### ✔ 5. Provincia con mayor importación  
Devuelve la provincia y su total de **IMPORTACIONES**.

---

## ▶️ Ejecución del programa

Ejecutar desde la raíz del proyecto:

```bash
python app.py
