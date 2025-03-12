import streamlit as st
from streamlit_option_menu import option_menu
# Configuração do título e favicon da aplicação
st.set_page_config(
    page_title="Cobranças Virtualis",
    page_icon=":house:",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Verificação de autenticação
if not st.experimental_user.is_logged_in:
    st.title("🔒 Acesso Restrito - Virtualis")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/2965/2965278.png", width=200)
        if st.button("🔐 Entrar com Google"):
            st.login()
        st.markdown("---")
        st.caption("Você precisa estar autenticado para acessar esta aplicação")
    st.stop()
    
    
from parcelamento import page_parcelamento_cartao
from cobranca import page_cobranca
from calculo_parcelas import page_calculo_parcelas


# Configuração inicial do painel
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

    /* Estilização do item selecionado no sidebar */
        .nav-link.active  {{
        background-color: {theme_config["theme.primaryColor"]} !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border-radius: 8px;
        padding: 5px 10px;
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


# Definir as páginas como funções para chamadas diretas
def p_parcelamento_cartao():
    st.title("Calculadora de Parcelas de Cartão 💳💲")
    st.write("Calcule aqui o parcelamento de valores...")
    page_parcelamento_cartao()  # Chama a função de Contas a Pagar


    
def p_cobranca():
    st.title("Cobrança 🤑")
    st.write("Aqui estão os dados de cobrança...")
    page_cobranca()  # Chama a função de Cobrança    
    
def p_calculo_parcelas():
    st.title("Calculo de Parcelas 🖩🧮")
    st.write("Aqui está o calculo de parcelas")
    page_calculo_parcelas()  # Chama a função de Calcul
# Criando o menu lateral para navegação com o Streamlit-Option-Menu
with st.sidebar:
    pagina_selecionada = option_menu(
        menu_title="Menu",
        options=["Parcelamento", "Cobrança", "Cálculo Parcelas"],
        icons=["currency-exchange", "cash", "bar-chart", "bar-chart", "bar-chart", "bar-chart"],  # Alterado o ícone de Comparativo
        menu_icon="cast",
        default_index=0,
    )

# Lógica para mostrar a página selecionada, agora com chamadas diretas para as funções
if pagina_selecionada == "Parcelamento":
    p_parcelamento_cartao()  # Chama a função para Contas a Pagar

elif pagina_selecionada == "Cobrança":
    p_cobranca()  # Chama a função para Cobrança
elif pagina_selecionada == "Cálculo Parcelas":
    p_calculo_parcelas()  # Chama a função para Cálculo de Parcelas
    