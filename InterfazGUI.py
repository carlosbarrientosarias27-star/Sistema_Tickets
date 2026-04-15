import streamlit as st
import streamlit_antd_components as sac

# 1. Configuración de página y estilo "Dark" forzado
st.set_page_config(page_title="Tickets Soporte NLP", layout="wide")

st.markdown("""
    <style>
    /* Fondo principal y textos */
    .stApp { background-color: #1e1e1e; color: #ffffff; }
    
    /* Personalización de botones */
    div.stButton > button {
        width: 100%;
        border-radius: 4px;
        font-weight: bold;
        border: none;
    }
    
    /* Colores específicos de los botones según la imagen */
    /* Botón Cargar Ejemplo (Azul) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        background-color: #3498db !important;
        color: white !important;
    }
    /* Botón Limpiar (Rojo) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background-color: #e74c3c !important;
        color: white !important;
    }
    /* Botón Cargar JSON (Verde) */
    .st-emotion-cache-18ni7ap { 
        background-color: #4CAF50 !important; 
    }
    /* Botón Procesar Lote (Naranja) */
    button[kind="primary"] {
        background-color: #f39c12 !important;
        border-color: #f39c12 !important;
    }
    /* Botón Grande de Procesando (Verde suave) */
    div.stButton > button:disabled {
        background-color: #5bbd60 !important;
        color: white !important;
        opacity: 1 !important;
    }

    /* Caja de la consola/pipeline */
    .console-box {
        background-color: #121212;
        color: #4CAF50;
        font-family: 'Courier New', Courier, monospace;
        padding: 20px;
        border-radius: 8px;
        height: 500px;
        border: 1px solid #333;
        font-size: 14px;
        line-height: 1.5;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO ---
st.markdown("<h2 style='text-align: center; color: white;'>📑 Sistema de Análisis de Tickets de Soporte con NLP</h2>", unsafe_allow_html=True)

c_top1, c_top2 = st.columns([1, 1])
with c_top1:
    st.markdown("<span style='color: #4CAF50;'>✅ Ollama conectado</span>", unsafe_allow_html=True)
with c_top2:
    st.markdown("<p style='text-align: right; color: #888;'>🤖 Modelo: <b>qwen2.5:7b</b></p>", unsafe_allow_html=True)

st.markdown("---")

# --- CUERPO ---
col_izq, col_der = st.columns([1, 1.2])

with col_izq:
    st.markdown("### 📝 Ticket a analizar")
    st.text_area("input_ticket", placeholder="Texto del ticket...", height=250, label_visibility="collapsed")
    
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        st.button("📥 Cargar ejemplo")
    with btn_col2:
        st.button("🗑️ Limpiar")
    
    st.markdown("### 📦 Procesamiento por lotes")
    btn_col3, btn_col4 = st.columns(2)
    with btn_col3:
        st.button("📂 Cargar JSON con tickets", key="json_btn")
    with btn_col4:
        st.button("⚡ Procesar lote", type="primary")
        
    st.button("⏳ PROCESANDO LOTE...", disabled=True)
    st.progress(10)
    st.caption("📑 Procesando ticket 1/1...")

with col_der:
    # Navegación estilo pestañas como en la imagen
    tipo = sac.tabs([
        sac.TabsItem(label='Pipeline', icon='link'),
        sac.TabsItem(label='Acciones', icon='lightning'),
        sac.TabsItem(label='JSON', icon='filetype-json'),
        sac.TabsItem(label='Modelos', icon='bar-chart'),
    ], align='center', variant='standard', index=0)

    # Contenido de la consola
    st.markdown(f"""
    <div class="console-box">
    ============================================================<br>
    🔗 PROCESANDO LOTE DE 1 TICKETS<br>
    ============================================================<br>
    ><br>
    </div>
    """, unsafe_allow_html=True)