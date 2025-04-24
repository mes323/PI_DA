# 📡 Proyecto de Análisis de Telecomunicaciones en Argentina

## 🧾 Descripción del Proyecto

Este proyecto tiene como objetivo analizar el comportamiento del sector de telecomunicaciones en Argentina, con foco en el **acceso a Internet por provincia**. A través de la integración de múltiples fuentes de datos, se busca:

- Identificar la penetración del servicio en cada provincia.
- Medir la evolución del acceso a lo largo del tiempo.
- Evaluar el crecimiento potencial de la conectividad.
- Brindar insights para una mejor toma de decisiones en la empresa.

---

## 📊 Dataset Utilizado

Se utilizaron los siguientes datasets oficiales:

- `Internet.xlsx` → Acceso a Internet por provincia.
- `telefonia_fija.xlsx` → Accesos a líneas fijas.
- `Telefonia_movil.xlsx` → Accesos a telefonía móvil (3G/4G).
- `Television.xlsx` → Servicios de TV.
- `servicios_postales.xlsx` → Servicios postales por región.
- `mapa_conectividad.xlsx` → Información poblacional y cobertura.

> Todos los datasets fueron limpiados, unificados por provincia y enriquecidos en una tabla final.

---

## 🛠️ Estructura del Proyecto

PI - DA/ 
├── /data/ (ademas de los datasets de fuente)
│ └── dataset_kpis.csv 
├── /scripts/ 
│ └──EDA_Telecomunicaciones.py 
├── /app/ 
│ └── app_streamlit.py 
├── README.md 
├── requirements.txt


---

## 🧮 KPIs Calculados

1. **Penetración de Internet (%)**
   - Fórmula: `(Hogares con Internet / Total de Hogares) * 100`

2. **Proyección de Accesos a Internet (2%)**
   - Fórmula: `Accesos actuales * 1.02`

3. **KPI de Crecimiento Esperado**
   - Fórmula: `((Proyección - Actual) / Actual) * 100`

---

## 🧠 Conclusiones Relevantes

- Las provincias con mayor penetración superan el 90% de cobertura.
- Se detectan zonas con baja conectividad en el norte argentino.
- El crecimiento potencial está concentrado en provincias con menor densidad.

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/mes323/PI_DA
cd PI - DA

2. Instalar dependencias
pip install -r requirements.txt

3. Ejecutar la app Streamlit
streamlit run app/app_streamlit.py

DIGRAMA DE FLUJO DEL PROYECTO

               +--------------------+
               |  Datasets Original |
               |  (.xlsx archivos)  |
               +---------+----------+
                         |
                         v
           +----------------------------+
           | Limpieza y Enriquecimiento |
           | (EDA_Telecomunicaciones)|
           +--------------+-------------+
                          |
                          v
         +----------------------------------+
         | dataset_kpis.csv       |
         +----------------+-----------------+
                          |
                          v
           +------------------------------+
           |   App Interactiva (Streamlit)|
           +------------------------------+
                          |
                          v
            +----------------------------+
            |    Visualización y KPIs   |
            +----------------------------+

🙌 Autor
Maximiliano Emmanuel Sosa
📧 mes_323@hotmail.com
🔗 LinkedIn https://www.linkedin.com/in/maxsosa23/
🔗 GitHub https://github.com/mes323
