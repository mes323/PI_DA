import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración inicial
st.set_page_config(page_title="Dashboard Telecomunicaciones", layout="wide")
st.title("📡 Dashboard de Telecomunicaciones en Argentina")

# Cargar dataset limpio
@st.cache_data
def load_data():
    # ✅ Importante: archivo CSV debe estar en la raíz del proyecto
    df = pd.read_csv("dataset_kpis.csv")

    # Normalizar columna Provincia
    if 'Provincia' in df.columns:
        df['Provincia'] = df['Provincia'].astype(str).str.upper().str.strip()

    # Calcular métricas necesarias si no existen
    if 'Penetracion_Internet' not in df.columns:
        if 'Población' in df.columns and df['Población'].notna().any():
            df['Penetracion_Internet'] = (df['Accesos'] / df['Población']) * 100
        else:
            df['Penetracion_Internet'] = 0  # Fallback si población está vacía

    # Usar Accesos como proxy de hogares conectados
    df['Hogares Con Internet'] = df['Accesos']

    # Cálculo de KPIs
    df['Proyeccion_Nuevo_Acceso'] = df['Hogares Con Internet'] * 1.02
    df['KPI_Incremento_Internet'] = (
        (df['Proyeccion_Nuevo_Acceso'] - df['Hogares Con Internet']) /
        df['Hogares Con Internet']
    ) * 100

    return df

# Cargar datos
df = load_data()

# Sidebar de filtros
st.sidebar.header("Filtros")
provincias = df['Provincia'].dropna().unique()
prov_select = st.sidebar.multiselect("Seleccionar Provincia(s)", sorted(provincias), default=sorted(provincias))

# Filtrado de datos
df_filtrado = df[df['Provincia'].isin(prov_select)]

# KPIs
st.subheader("🔢 Indicadores Clave (KPI)")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Penetración Promedio (%)", f"{df_filtrado['Penetracion_Internet'].mean():.2f}")
with col2:
    st.metric("Accesos Totales", f"{df_filtrado['Hogares Con Internet'].sum():,.0f}")
with col3:
    st.metric("Proyección Accesos (2%)", f"{df_filtrado['Proyeccion_Nuevo_Acceso'].sum():,.0f}")

# Gráfico de barras - Penetración por Provincia
st.subheader("📊 Penetración de Internet por Provincia")
fig_bar = px.bar(
    df_filtrado.sort_values("Penetracion_Internet", ascending=False),
    x="Penetracion_Internet", y="Provincia",
    orientation="h", color="Penetracion_Internet",
    labels={"Penetracion_Internet": "Penetración (%)"},
    height=600
)
st.plotly_chart(fig_bar, use_container_width=True)

# Gráfico de KPI incremento
st.subheader("📈 Proyección de Incremento en Accesos por Provincia")
fig_kpi = px.bar(
    df_filtrado.sort_values("KPI_Incremento_Internet", ascending=False),
    x="Provincia", y="KPI_Incremento_Internet",
    color="KPI_Incremento_Internet",
    labels={"KPI_Incremento_Internet": "KPI Incremento (%)"}
)
st.plotly_chart(fig_kpi, use_container_width=True)

# Tabla de datos opcional
with st.expander("📋 Ver datos filtrados"):
    st.dataframe(df_filtrado)
