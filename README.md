# 📊 Proyecto de Econometría Aplicada

## 🎯 1. Objetivo

Este proyecto analiza la relación entre el índice bursátil S&P 500 y el tipo de cambio USD/MXN, utilizando modelos econométricos de series de tiempo:

- VAR (Vector Autoregressive)
- VECM (Vector Error Correction Model)
- GARCH
- EGARCH

---

## 📁 2. Datos

Los datos fueron obtenidos de Yahoo Finance y corresponden a:

- 📈 S&P 500 (^GSPC)
- 💱 Tipo de cambio USD/MXN (MXN=X)

📅 Periodo: 2015 - actualidad  
📊 Frecuencia: diaria  
📌 Transformación: rendimientos logarítmicos

---

## 🧠 3. Metodología

### 📌 VAR
Modelo multivariado que analiza la relación dinámica entre las variables.

### 📌 Cointegración (Johansen)
Se evalúa si existe una relación de equilibrio de largo plazo entre las variables.

### 📌 VECM
Modelo que corrige desviaciones del equilibrio de largo plazo.

### 📌 GARCH
Modela la volatilidad condicional del mercado.

### 📌 EGARCH
Permite capturar asimetrías en los shocks financieros.

---

## 📊 4. Resultados

### 📈 VAR
- Existe interacción significativa entre las variables.
- Se observa dependencia temporal entre SP500 y USD/MXN.

### 🔗 Cointegración (Johansen)
- Se encontró evidencia de cointegración.
- Las variables tienen relación de largo plazo.

### ⚖️ VECM
- El sistema corrige desviaciones del equilibrio.
- Los coeficientes de ajuste son significativos.

### 📉 GARCH
- La volatilidad es persistente (clustering).
- Alta sensibilidad a shocks del mercado.

### ⚡ EGARCH
- Existe asimetría en los shocks.
- Las malas noticias afectan más que las buenas.

---

## 📊 5. Gráficas (incluidas en el proyecto)

El análisis incluye:

- Evolución de rendimientos del S&P 500
- Evolución del tipo de cambio USD/MXN
- Volatilidad condicional (GARCH)
- Shock asimétrico (EGARCH)

📌 Estas gráficas se generan automáticamente al ejecutar el código en `main.py`.

---

## 🧰 6. Herramientas utilizadas

- Python 🐍
- Pandas
- NumPy
- Statsmodels
- ARCH package
- Yahoo Finance API
- Visual Studio Code

---

## 🚀 7. Conclusiones

- Existe relación entre el mercado bursátil y el tipo de cambio.
- Se confirma cointegración entre las variables.
- Los mercados presentan volatilidad persistente.
- Los shocks negativos tienen mayor impacto que los positivos.
- Los modelos utilizados permiten capturar dinámicas de corto y largo plazo.

---

## 📌 8. Cómo ejecutar el proyecto

```bash
python main.py