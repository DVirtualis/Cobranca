import streamlit as st
import pandas as pd


def page_parcelamento_cartao():
    # Paleta de cores atualizada
    COLORS = ['##0095fb', '#7C3AED', '#3B82F6', '#10B981', '#EF4444', '#F59E0B']
    COLORS_DARK = ['#1b4f72', '#d35400', '#145a32', '#7b241c', '#5b2c6f']

    # Configuração do tema no session_state
    ms = st.session_state
    if "themes" not in ms:
        ms.themes = {
            "current_theme": "light",
            "light": {
                "theme.base": "light",
                "theme.backgroundColor": "#F3F4F6",  # Cor de fundo
                "theme.primaryColor": "#383bf8",     # Cor primária (botões, links)
                "theme.secondaryBackgroundColor": "#F3F4F6",  # Cor de fundo secundária
                "theme.textColor": "#111827",        # Cor do texto
                "button_face": "Modo Escuro 🌙",     # Texto do botão
                "colors": COLORS,                    # Paleta de cores
            },
            "dark": {
                "theme.base": "dark",
                "theme.backgroundColor": "#1F2937",  # Cor de fundo
                "theme.primaryColor": "#70c4fc",     # Cor primária (botões, links)
                "theme.secondaryBackgroundColor": "#1f2937",  # Cor de fundo secundária
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
            border-radius:5px;
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
        .stExpander .stMarkdown, .stTooltip{{
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

        .stElementToolbarButton  {{
                color: white !important;
            }}
        
        
        div[data-testid="stMetricValue"] {{
            color: {theme_config["theme.textColor"]} !important;
        }}

        #[class*="stMetric"]
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
    # Configuração das taxas de juros
    TAXAS = {
        "Point": {
            
            2: 0.0442,
            3: 0.0532,
            4: 0.0622,
            5: 0.0712,
            6: 0.0802,
            7: 0.0892,
            8: 0.0982,
            9: 0.1072,
            10: 0.1162,
            11: 0.1252,
            12: 0.1342
        },
        "Link de Pagamento": {
            "Débito": 0.015,
            "Crédito a Vista": 0.0310,
            "Pix":0.0049,
            2: 0.0439,
            3: 0.0514,
            4: 0.0589,
            5: 0.0664,
            6: 0.0739,
            7: 0.0818,
            8: 0.0893,
            9: 0.0968,
            10: 0.1043,
            11: 0.1118,
            12: 0.1193
        }, 
        "Visa": {
            "Crédito a Vista": 0.0235,
            "Débito a Vista": 0.0142,
            "QRCode pelo App": 0.0075,
            2: 0.0269, 
            3: 0.0269,
            4: 0.0269,
            5: 0.0269,
            6: 0.0269,
            7: 0.0300,
            8: 0.0300,
            9: 0.0300,
            10: 0.0300,
            11: 0.0300,
            12: 0.0300,
            13: 0.0270,
            14: 0.0270,
            15: 0.0270,
            16: 0.0270,
            17: 0.0270,
            18: 0.0270
        },
        "Visa Crédito com Juros": {
            2: 0.0205, 
            3: 0.0205,
            4: 0.0205,
            5: 0.0205,
            6: 0.0205,
            7: 0.0205,
            8: 0.0205,
            9: 0.0205,
            10: 0.0205,
            11: 0.0205,
            12: 0.0205,  
        }
    }

    def formatar_moeda(valor):
        """Formata valores monetários no padrão brasileiro"""
        return f"R$ {valor: ,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    def mostrar_calculo(valor_total, taxa, num_parcelas, tipo_parcelamento):
        """Exibe os cálculos detalhados"""
        
        if tipo_parcelamento in ["Visa", "Visa Crédito com Juros"] and isinstance(num_parcelas, int):
            taxa_base = TAXAS[tipo_parcelamento][num_parcelas]
            taxa_total = taxa_base * num_parcelas
            total_com_juros = valor_total * (1 + taxa_total)
        else:
            total_com_juros = valor_total * (1 + taxa)
        
        valor_parcela = total_com_juros / num_parcelas if isinstance(num_parcelas, int) else total_com_juros
        juros_total = total_com_juros - valor_total
        
        st.subheader("Resultado do Cálculo")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Valor Total", formatar_moeda(valor_total))
        with col2:
            if tipo_parcelamento in ["Visa", "Visa Crédito com Juros"] and isinstance(num_parcelas, int):
                taxa_base = TAXAS[tipo_parcelamento][num_parcelas]
                st.metric(
                    "Taxa Aplicada", 
                    f"{taxa_base:.2%} × {num_parcelas}",
                    help="Taxa por parcela multiplicada pelo número de parcelas"
                )
            else:
                st.metric("Taxa Aplicada", f"{taxa:.2%}")
        with col3:
            st.metric("Total Parcelado", formatar_moeda(total_com_juros))
        
        # Mostrar detalhes do cálculo
        with st.expander("Ver detalhes do cálculo"):
            if tipo_parcelamento in ["Visa", "Visa Crédito com Juros"] and isinstance(num_parcelas, int):
                st.markdown(f"""
                **Fórmula utilizada (Parcelado):**  
                - Taxa Total = Taxa por Parcela × Número de Parcelas  
                - Valor Total com Juros = Valor Total × (1 + Taxa Total)  
                - Valor da Parcela = Valor Total com Juros ÷ Número de Parcelas  
                
                **Aplicando os valores:**  
                1\. Taxa Total = {taxa_base:.2%} × {num_parcelas} = {taxa_total:.2%}  
                2\. {formatar_moeda(valor_total).replace('$', '\\$')} × (1 + {taxa_total:.2%}) = {formatar_moeda(total_com_juros).replace('$', '\\$')}  
                3\. {formatar_moeda(total_com_juros).replace('$', '\\$')} ÷ {num_parcelas} = {formatar_moeda(valor_parcela).replace('$', '\\$')}  
                """)
            else:
                st.markdown(f"""
                **Fórmula utilizada:**  
                - Valor Total com Juros = Valor Total × (1 + Taxa)  
                - Valor da Parcela = Valor Total com Juros ÷ Número de Parcelas  
                
                **Aplicando os valores:**  
                1\. {formatar_moeda(valor_total).replace('$', '\\$')} × (1 + {taxa:.2%}) = {formatar_moeda(total_com_juros).replace('$', '\\$')}  
                2\. {formatar_moeda(total_com_juros).replace('$', '\\$')} ÷ {num_parcelas} = {formatar_moeda(valor_parcela).replace('$', '\\$')}  
                """)

    def page_calculadora_parcelamento():
        st.title("Calculadora de Parcelamento")
        
        # Entrada de dados
        valor_total = st.number_input(
            "Valor Total (R$)", 
            min_value=0.01, 
            step=100.0,
            format="%.2f"
        )
        
        tipo_parcelamento = st.selectbox(
            "Tipo de Parcelamento",
            options=list(TAXAS.keys())
        )
        
        num_parcelas = st.selectbox(
        "Número de Parcelas",
        options=list(TAXAS[tipo_parcelamento].keys()),
        format_func=lambda x: f"{x}X" if isinstance(x, int) else x
    )
        
        # Obter taxa selecionada com regras especiais para Visa
        if tipo_parcelamento in ["Visa", "Visa Crédito com Juros"] and isinstance(num_parcelas, int):
            taxa_base = TAXAS[tipo_parcelamento][num_parcelas]
            taxa = taxa_base * num_parcelas
        else:
            taxa = TAXAS[tipo_parcelamento][num_parcelas]
        
    
        
        # Calcular e mostrar resultados
        if valor_total > 0:
            mostrar_calculo(valor_total, taxa, num_parcelas, tipo_parcelamento)
            
            # Mostrar tabela comparativa de taxas
            st.subheader("Tabela Completa de Taxas")
            
            # Configurar pandas para mostrar todo o conteúdo
            pd.set_option('display.max_colwidth', None)
            
            df_taxas = pd.DataFrame.from_dict(TAXAS[tipo_parcelamento], orient='index', columns=['Taxa'])
            df_taxas.index.name = 'Parcelas'
            
            # Aplicar formatação especial para Visa
            if tipo_parcelamento in ["Visa", "Visa Crédito com Juros"]:
                df_taxas['Taxa'] = df_taxas.apply(
                    lambda x: f"{x['Taxa']:.2%} por parcela" if isinstance(x.name, int) else f"{x['Taxa']:.2%}",
                    axis=1
                )
            else:
                df_taxas['Taxa'] = df_taxas['Taxa'].apply(lambda x: f"{x:.2%}")

            # Configurar a exibição da tabela
            with st.container():
                st.markdown("""
                <style>
                    .full-width-table {
                        width: 100%;
                        white-space: nowrap;
                    }
                    .dataframe td {
                        min-width: 120px;
                        padding: 10px !important;
                    }
                </style>
                """, unsafe_allow_html=True)
                
                st.dataframe(
                    df_taxas,
                    use_container_width=True,
                    height=(len(df_taxas) * 35 + 40) ) # Altura dinâmica baseada no número de linhas

    if __name__ == "__main__":
        page_calculadora_parcelamento()