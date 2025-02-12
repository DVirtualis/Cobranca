import streamlit as st
import pandas as pd
import plotly.express as px
import pyodbc
import toml
from datetime import datetime, timedelta

# Configuração inicial do painel
#st.set_page_config(
 #   page_title="Painel Financeiro Completo",
  #  page_icon="📊",
   # layout="wide",
    #initial_sidebar_state="expanded")

def page_calculo_parcelas():
     # Paleta de cores atualizada
    COLORS = ['#13428d', '#7C3AED', '#3B82F6', '#10B981', '#EF4444', '#F59E0B']
    COLORS_DARK = ['#1b4f72', '#d35400', '#145a32', '#7b241c', '#5b2c6f']

    # Configuração do tema no session_state
    ms = st.session_state
    if "themes" not in ms:
        ms.themes = {
            "current_theme": "light",
            "light": {
                "theme.base": "light",
                "theme.backgroundColor": "#FFFFFF",  # Cor de fundo
                "theme.primaryColor": "#0095fb",     # Cor primária (botões, links)
                "theme.secondaryBackgroundColor": "#F3F4F6",  # Cor de fundo secundária
                "theme.textColor": "#111827",        # Cor do texto
                "button_face": "Modo Escuro 🌙",     # Texto do botão
                "colors": COLORS,                    # Paleta de cores
            },
            "dark": {
                "theme.base": "dark",
                "theme.backgroundColor": "#1F2937",  # Cor de fundo
                "theme.primaryColor": "#0095fb",     # Cor primária (botões, links)
                "theme.secondaryBackgroundColor": "#4B5563",  # Cor de fundo secundária
                "theme.textColor": "#efefef",        # Cor do texto
                "button_face": "Modo Claro 🌞",      # Texto do botão
                "colors": COLORS_DARK,               # Paleta de cores
            }
        }

    # Função para alternar o tema
    def change_theme():
        current_theme = ms.themes["current_theme"]
        ms.themes["current_theme"] = "dark" if current_theme == "light" else "light"
        ms.themes["refreshed"] = True  # Atualiza o estado

    # Configuração do tema atual
    current_theme = ms.themes["current_theme"]
    theme_config = ms.themes[current_theme]

     # Botão de alternar tema
    if st.button(theme_config["button_face"], on_click=change_theme):
        pass


    # Aplicar as cores do tema atual
    colors = theme_config["colors"]

    # Injetar CSS personalizado com base no tema atual
    st.markdown(
        f"""
        <style>
        /* ===== [CONFIGURAÇÃO GLOBAL] ===== */
        html, body, .stApp {{
            background-color: {theme_config["theme.backgroundColor"]};
            color: {theme_config["theme.textColor"]};
        }}

        /* ===== [COMPONENTES DO STREAMLIT] ===== */
        /* Ajuste para Selectbox */
        .stSelectbox > div > div {{
            background-color: {theme_config["theme.secondaryBackgroundColor"]} !important;
            color: {theme_config["theme.textColor"]} !important;
            border-radius: 5px; /* Bordas arredondadas */
            border: 2px solid {theme_config["theme.primaryColor"]} !important; /* Cor oposta do tema */
        }}

        .stSelectbox > div > div:hover {{
            background-color: {theme_config["theme.primaryColor"]} !important;
            color: #FFFFFF !important;
              border: 2px solid {theme_config["theme.textColor"]} !important; /* Cor oposta do tema */
        border-radius: 5px; /* Bordas arredondadas */
        transition: border-color 0.3s ease-in-out; /* Suaviza a transição */

        }}

        /* Placeholder ajustado */
        .stSelectbox > div > div::placeholder {{
            color: {theme_config["theme.textColor"]} !important;
            opacity: 0.7;
        }}

        
        /* ===== [CABEÇALHOS E TÍTULOS] ===== */
        h1, h2, h3, h4, h5, h6,
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
        .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {{
            color: {theme_config["theme.textColor"]} !important;
        }}

    /* ===== [COMPONENTES PRINCIPAIS] ===== */
        .stDataFrame, .stMetric, .stJson, .stAlert,
        .stExpander .stMarkdown, .stTooltip, .stMetricValue {{
            color: {theme_config["theme.textColor"]} !important;
        }}
        
        
        /* ===== [SIDEBAR] ===== */
        .stSidebar {{
            background-color: {theme_config["theme.secondaryBackgroundColor"]} !important;
            border-radius: 15px;
            padding: 10px;
        }}
         .nav-link.active {{
        background-color: {theme_config["theme.primaryColor"]} !important;
        color: #FFFFFF !important; /* Texto branco para contraste */
        font-weight: bold !important; /* Texto em negrito para destaque */
        border-radius: 8px; /* Bordas arredondadas */
        padding: 10px; /* Espaçamento interno */
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra para destaque */
    }}

    /* Ícones dentro do item ativo */
    .nav-link.active .icon {{
        color: #FFFFFF !important; /* Altera a cor do ícone no item ativo */
    }}

    /* Estilo para itens inativos */
    .nav-link {{
        color: {theme_config["theme.textColor"]} !important; /* Cor do texto do tema */
        transition: background-color 0.3s, color 0.3s; /* Transição suave ao passar o mouse */
    }}

    .nav-link:hover {{
        background-color: {theme_config["theme.primaryColor"]}33; /* Cor primária translúcida */
        color: {theme_config["theme.primaryColor"]} !important; /* Texto na cor primária */
    }}

        /* Ajusta texto e fundo nos botões */
        .stButton>button {{
            background-color: {theme_config["theme.primaryColor"]} !important;
            color: #FFFFFF !important;
        }}

        /* ===== [GENÉRICO] ===== */
        /* Ajusta elementos dinâmicos */
        .st-emotion-cache-1cj4yv0,
        .st-emotion-cache-efbu8t {{
            background-color: {theme_config["theme.secondaryBackgroundColor"]} !important;
        
        }}
        
        /* ===== [COMPONENTES ESPECÍFICOS] ===== */
        .stMultiSelect span[data-baseweb="tag"] {{
            background-color: {theme_config["theme.primaryColor"]} !important;
            color: white !important;
        }}

        .stButton>button p {{
            color: white !important;
        }}

        div[data-testid="stMetricValue"] {{
            color: {theme_config["theme.textColor"]} !important;
        }}

        [class*="stMetric"]
        {{
            color: {theme_config["theme.textColor"]} !important;
        }}
        
        [class*="st-emotion-cache"] {{
            color: {theme_config["theme.primaryColor"]} !important;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Calculadora de Parcelas - Métodos de Amortização")

    # Funções de cálculo
    def calcular_price(pv, taxa_mensal, meses):
        if taxa_mensal == 0:
            return pv / meses
        return (pv * taxa_mensal) / (1 - (1 + taxa_mensal)**-meses)

    def calcular_sac(pv, taxa_mensal, meses):
        amortizacao = pv / meses
        saldo_devedor = pv
        tabela = []
        for _ in range(meses):
            juros = saldo_devedor * taxa_mensal
            parcela = amortizacao + juros
            tabela.append(parcela)
            saldo_devedor -= amortizacao
        return tabela
    def calcular_sacre(pv, taxa_mensal, meses):
        saldo_devedor = pv
        amortizacao_base = pv / meses
        fator = 1 + taxa_mensal
        tabela = []
        for i in range(1, meses + 1):
            amortizacao = amortizacao_base * (fator**i)
            juros = saldo_devedor * taxa_mensal
            parcela = amortizacao + juros
            tabela.append(parcela)
            saldo_devedor -= amortizacao
        return tabela
    
    
    def calcular_mejs(pv, taxa_mensal, meses):
        total_juros = pv * taxa_mensal * meses
        return (pv + total_juros) / meses

    # Interface
    metodo = st.selectbox("Selecione o Método:", ["Price", "SAC","SACRE", "MEJS"])

    col1, col2 = st.columns(2)
    with col1:
        valor = st.number_input(f"Valor {'Presente' if metodo == 'Price' else 'Financiado'} (R$)", 
                            min_value=0.0, value=10000.0, step=100.0)
    with col2:
        taxa = st.number_input("Taxa de Juros Mensal (%)", 
                            min_value=0.0, value=2.0, step=0.1) / 100

    meses = st.slider("Número de Meses", min_value=1, max_value=360, value=12)
    mostrar_todas = st.checkbox("Mostrar tabela completa de amortização")

    # Cálculos
    if st.button("Calcular"):
        try:
            if metodo == "Price":
                parcela = calcular_price(valor, taxa, meses)
                st.success(f"Valor da Parcela (Price): R$ {parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
                
                if mostrar_todas:
                    saldo = valor
                    tabela = []
                    for i in range(1, meses+1):
                        juros = saldo * taxa
                        amort = parcela - juros
                        saldo -= amort
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0)
                        })
                    df = pd.DataFrame(tabela)
                    st.dataframe(df.style.format({
                        "Parcela": "{:,.2f}",
                        "Juros": "{:,.2f}", 
                        "Amortização": "{:,.2f}",
                        "Saldo Devedor": "{:,.2f}"
                    }))

            elif metodo == "SAC":
                parcelas = calcular_sac(valor, taxa, meses)
                st.success(f"Primeira Parcela (SAC): R$ {parcelas[0]:,.2f}")
                
                if mostrar_todas:
                    saldo = valor
                    tabela = []
                    for i, parcela in enumerate(parcelas, 1):
                        juros = saldo * taxa
                        amort = valor / meses
                        saldo -= amort
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0)
                        })
                    df = pd.DataFrame(tabela)
                    st.dataframe(df.style.format({
                        "Parcela": "{:,.2f}",
                        "Juros": "{:,.2f}",
                        "Amortização": "{:,.2f}",
                        "Saldo Devedor": "{:,.2f}"
                    }))

            elif metodo == "SACRE":
                parcelas = calcular_sacre(valor, taxa, meses)
                st.success(f"Primeira Parcela (SACRE): R$ {parcelas[0]:,.2f}")
                
                if mostrar_todas:
                    saldo = valor
                    amortizacao_base = valor / meses
                    fator = 1 + taxa
                    tabela = []
                    for i, parcela in enumerate(parcelas, 1):
                        juros = saldo * taxa
                        amort = amortizacao_base * (fator**i)
                        saldo -= amort
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0)
                        })
                    df = pd.DataFrame(tabela)
                    st.dataframe(df.style.format({
                        "Parcela": "{:,.2f}",
                        "Juros": "{:,.2f}",
                        "Amortização": "{:,.2f}",
                        "Saldo Devedor": "{:,.2f}"
                    }))

            elif metodo == "MEJS":
                parcela = calcular_mejs(valor, taxa, meses)
                st.success(f"Valor da Parcela (MEJS): R$ {parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
                
                if mostrar_todas:
                    saldo = valor
                    amort = valor / meses
                    tabela = []
                    for i in range(1, meses+1):
                        juros = valor * taxa  # Juros fixos sobre o valor original
                        saldo -= amort
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0)
                        })
                    df = pd.DataFrame(tabela)
                    st.dataframe(df.style.format({
                        "Parcela": "{:,.2f}",
                        "Juros": "{:,.2f}", 
                        "Amortização": "{:,.2f}",
                        "Saldo Devedor": "{:,.2f}"
                    }))

        except ZeroDivisionError:
            st.error("O número de meses deve ser maior que zero")
        except Exception as e:
            st.error(f"Erro no cálculo: {str(e)}")

    # Explicação dos métodos
    st.markdown("""
    ### Explicação dos Métodos:
    - **Price (Tabela Price):** Parcelas constantes com juros compostos.  
    - **SAC (Sistema de Amortização Constante):** Parcelas decrescentes com amortização constante.  
    - **SACRE (Sistema de Amortização Crescente):** Amortização crescente com parcelas variáveis.  
    - **MEJS:** Método de Equivalência a Juros Simples com maior amortização inicial.  
    """)