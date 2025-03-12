import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Calculador de Parcelas",
    page_icon=":house:",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    
    
 # Função de formatação monetária
    def formatar_moeda(valor):
        """Formata valores monetários no padrão brasileiro"""
        return f"R$ {valor: ,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    # Configuração das taxas de juros das máquinas (mantido do seu código original)
    MAQUINAS = {
        "Mercado Pago":{
        "Point": {2: 0.0442, 3: 0.0532, 4: 0.0622, 5: 0.0712, 6: 0.0802, 7: 0.0892, 8: 0.0982, 9: 0.1072, 10: 0.1162, 11: 0.1252, 12: 0.1342},
        "Link de Pagamento": {"Débito": 0.015, "Crédito a Vista": 0.0310, "Pix":0.0049, 2: 0.0439, 3: 0.0514, 4: 0.0589, 5: 0.0664, 6: 0.0739, 7: 0.0818, 8: 0.0893, 9: 0.0968, 10: 0.1043, 11: 0.1118, 12: 0.1193},
        },
        "Stone ISAT":{
        "Visa": {"Crédito a Vista": 0.0235, "Débito a Vista": 0.0142, "QRCode pelo App": 0.0075, 2: 0.0269, 3: 0.0269, 4: 0.0269, 5: 0.0269, 6: 0.0269, 7: 0.0300, 8: 0.0300, 9: 0.0300, 10: 0.0300, 11: 0.0300, 12: 0.0300, 13: 0.0270, 14: 0.0270, 15: 0.0270, 16: 0.0270, 17: 0.0270, 18: 0.0270},
        "Visa Crédito com Juros": {2: 0.0205, 3: 0.0205, 4: 0.0205, 5: 0.0205, 6: 0.0205, 7: 0.0205, 8: 0.0205, 9: 0.0205, 10: 0.0205, 11: 0.0205, 12: 0.0205},
        }, 
        "Stone Virtualis":{
        "Visa": {"Crédito a Vista": 0.0269, "Débito a Vista": 0.0177,  2: 0.0303, 3: 0.0303, 4: 0.0303, 5: 0.0303, 6: 0.0303, 7: 0.0327, 8: 0.0327, 9: 0.0327, 10: 0.0327, 11: 0.0327, 12: 0.0327, 13: 0.0327, 14: 0.0327, 15: 0.0327, 16: 0.0327, 17: 0.0327, 18: 0.0327},
        "Visa Crédito com Juros": {2: 0.0100, 3: 0.0100, 4: 0.0100, 5: 0.0100, 6: 0.0100, 7: 0.0100, 8: 0.0100, 9: 0.0100, 10: 0.0100, 11: 0.0100, 12: 0.0100},
        "MasterCard": {"Crédito a Vista": 0.0269, "Débito a Vista": 0.0177,  2: 0.0303, 3: 0.0303, 4: 0.0303, 5: 0.0303, 6: 0.0303, 7: 0.0327, 8: 0.0327, 9: 0.0327, 10: 0.0327, 11: 0.0327, 12: 0.0327, 13: 0.0327, 14: 0.0327, 15: 0.0327, 16: 0.0327, 17: 0.0327, 18: 0.0327},
        "AmericanExpress": {"Crédito a Vista": 0.0310,  2: 0.0356, 3: 0.0356, 4: 0.0356, 5: 0.0356, 6: 0.0356, 7: 0.0385, 8: 0.0385, 9: 0.0385, 10: 0.0385, 11: 0.0385, 12: 0.0385},
        "Cabal": {"Crédito a Vista": 0.0500, "Débito a Vista": 0.0500, 2: 0.0525, 3: 0.0525, 4: 0.0525, 5: 0.0525, 6: 0.0525, 7: 0.0550, 8: 0.0550, 9: 0.0550, 10: 0.0550, 11: 0.0550, 12: 0.0550},
        "Cabal Crédito com Juros": {2: 0.0100, 3: 0.0100, 4: 0.0100, 5: 0.0100, 6: 0.0100, 7: 0.0100, 8: 0.0100, 9: 0.0100, 10: 0.0100, 11: 0.0100, 12: 0.0100},
        "Hipercard":{"Crédito a Vista": 0.0280,  2: 0.0383, 3: 0.0383, 4: 0.0383, 5: 0.0383, 6: 0.0383, 7: 0.0430, 8: 0.0430, 9: 0.0430, 10: 0.0430, 11: 0.0430, 12: 0.0430},
        "Hipercard Crédito com Juros": {2: 0.0100, 3: 0.0100, 4: 0.0100, 5: 0.0100, 6: 0.0100, 7: 0.0100, 8: 0.0100, 9: 0.0100, 10: 0.0100, 11: 0.0100, 12: 0.0100},
        "UnionPay": {"Crédito a Vista": 0.0400, "Débito a Vista": 0.0400,  2: 0.0400, 3: 0.0400, 4: 0.0400, 5: 0.0400, 6: 0.0400, 7: 0.0400, 8: 0.0400, 9: 0.0400, 10: 0.0400, 11: 0.0400, 12: 0.0400},
        "Elo": {"Crédito a Vista": 0.0335, "Débito a Vista": 0.0186,  2: 0.0385, 3: 0.0385, 4: 0.0385, 5: 0.0385, 6: 0.0385, 7: 0.0402, 8: 0.0402, 9: 0.0402, 10: 0.0402, 11: 0.0402, 12: 0.0402,13: 0.0402, 14: 0.0402, 15: 0.0402, 16: 0.0402, 17: 0.0402, 18: 0.0402},
        "Elo Crédito com Juros": {2: 0.0100, 3: 0.0100, 4: 0.0100, 5: 0.0100, 6: 0.0100, 7: 0.0100, 8: 0.0100, 9: 0.0100, 10: 0.0100, 11: 0.0100, 12: 0.0100}
    }}
    
    
    LOGOS_MAQUINAS = {
        
        "Mercado Pago": "images/mercado-pago.svg",
        "Stone ISAT": "images/stone.png",
        "Stone Virtualis": "images/stone.png",
    }
    # Caminhos das imagens das operadoras
    LOGOS_OPERADORAS = {
        "Point": "images/mercado-pago.svg",
        "Link de Pagamento": "images/mercado-pago.svg",
        "Visa": "images/visa.png",
        "Visa Crédito com Juros": "images/visa.png",
        "MasterCard": "images/mastercard.png",
        "AmericanExpress": "images/american_express.png",
        "Cabal": "images/cabal.png",
        "Cabal Crédito com Juros": "images/cabal.png",
        "Hipercard": "images/hipercard.png",
        "Hipercard Crédito com Juros": "images/hipercard.png",
        "UnionPay": "images/unionpay.png",
        "Elo": "images/elo.svg",
        "Elo Crédito com Juros": "images/elo.svg"

    }


     # Funções de cálculo
    def calcular_price(pv, taxa_mensal, meses):
        if taxa_mensal == 0: return pv / meses
        return (pv * taxa_mensal) / (1 - (1 + taxa_mensal)**-meses)

    def calcular_sac(pv, taxa_mensal, meses):
        amortizacao = pv / meses
        return [amortizacao + (pv - amortizacao * i) * taxa_mensal for i in range(meses)]

    def calcular_sacre(pv, taxa_mensal, meses):
        saldo = pv
        amort_base = pv / meses
        return [amort_base * (1 + taxa_mensal)**(i+1) + (saldo - amort_base * i) * taxa_mensal for i in range(meses)]

    def calcular_mejs(pv, taxa_mensal, meses):
        total_juros = pv * taxa_mensal * meses
        return (pv + total_juros) / meses

   # Interface
    st.title("📈 Calculadora Financeira Integrada")
    st.markdown("---")

    modo_calculo = st.radio(
        "**Selecione o Tipo de Cálculo:**", 
        ["🏦 Financiamento", "💳 Parcelamento Simples"],
        horizontal=True,
        key="modo_calculo_radio"
    )

    with st.expander("⚙️ Configurações da Taxa", expanded=True):
        col1, col2, col3 = st.columns([2, 2, 3])

        with col1:
            # Seleção da Máquina com logo
            maquina = st.selectbox(
                "**Máquina**",
                options=list(MAQUINAS.keys()),
                key="maquina_select"
            )
            
            # Exibição da logo da máquina
            subcol1, subcol2 = st.columns([1, 2])
            with subcol1:
                if maquina in LOGOS_MAQUINAS:
                    st.image(LOGOS_MAQUINAS[maquina], width=70)
            
            with subcol2:
                # Taxa de antecipação
                taxa_antecipacao = st.number_input(
                    "**Taxa de Antec. (%)**",
                    min_value=0.0,
                    max_value=100.0,
                    value=2.0,
                    step=0.1,
                    format="%.2f"
                ) / 100

        with col2:
            # Seleção da Operadora com logo
            tipo_parcelamento = st.selectbox(
                "**Operadora**", 
                options=list(MAQUINAS[maquina].keys()),
                key="operadora_select"
            )
            
            # Exibição da logo da operadora
            subcol1, subcol2 = st.columns([1, 2])
            with subcol1:
                if tipo_parcelamento in LOGOS_OPERADORAS:
                    st.image(LOGOS_OPERADORAS[tipo_parcelamento], width=70)
            
            with subcol2:
                num_parcelas = st.selectbox(
                    "**Forma Pagamento**",
                    options=list(MAQUINAS[maquina][tipo_parcelamento].keys()),
                    format_func=lambda x: f"{x}X" if isinstance(x, int) else x,
                    key="forma_pagamento"
                )

        with col3:
            # Cálculo das taxas conforme tipo de máquina
            taxa_bruta = MAQUINAS[maquina][tipo_parcelamento][num_parcelas]
            is_parcelado = isinstance(num_parcelas, int)
            
            if maquina == "Mercado Pago":
                if is_parcelado:
                    # Taxa bruta = total, calcular mensal
                    taxa_total = taxa_bruta
                    taxa_mensal = (1 + taxa_bruta) ** (1/num_parcelas) - 1
                else:
                    # À vista: mesma taxa para ambos
                    taxa_mensal = taxa_bruta
                    taxa_total = taxa_bruta
            else:
                if is_parcelado:
                    # Taxa bruta = mensal, calcular total
                    taxa_mensal = taxa_bruta
                    taxa_total = (1 + taxa_bruta) ** num_parcelas - 1
                else:
                    # À vista: mesma taxa para ambos
                    taxa_mensal = taxa_bruta
                    taxa_total = taxa_bruta

            st.markdown(f"""
            <div style="
                background-color: {theme_config['theme.secondaryBackgroundColor']};
                padding: 1rem;
                border-radius: 10px;
                border: 2px solid {theme_config['theme.primaryColor']};
                margin-top: 1.5rem;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            ">
                <div style="margin-bottom: 0.5rem;">
                    <span style="font-size: 1.2rem; color: {theme_config['theme.primaryColor']}">💰 Taxas Aplicadas</span>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem;">
                    <div>
                        <span style="font-weight: bold; color: {theme_config['theme.textColor']}">Mensal:</span><br>
                        <span style="color: #2ecc71">{taxa_mensal:.2%}</span>
                    </div>
                    <div>
                        <span style="font-weight: bold; color: {theme_config['theme.textColor']}">Total:</span><br>
                        <span style="color: #e74c3c">{taxa_total:.2%}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    # Inicialização segura das variáveis
    valor = 0.0
    desconto = 0.0
    meses = 1
    
    if modo_calculo == "🏦 Financiamento":
        with st.expander("📊 Parâmetros do Financiamento", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                valor = st.number_input("**Valor Bruto (R$)**", 
                                      min_value=0.01, 
                                      value=10000.0, 
                                      step=100.0,
                                      key="valor_bruto")
                desconto = st.number_input("**Desconto (R$)**", 
                                         min_value=0.0, 
                                         max_value=valor if valor > 0 else 0.0, 
                                         value=0.0, 
                                         step=100.0,
                                         key="desconto")
            with col2:
                percentual = (desconto / valor * 100) if valor > 0 else 0.0
                st.metric("**Percentual de Desconto**", f"{percentual:.2f}%")
                st.metric("**Valor Líquido**", formatar_moeda(valor - desconto))
            
            metodo = st.selectbox("**Método de Amortização**",
                                ["Price", "SAC", "SACRE", "MEJS"],
                                key="metodo_amortizacao")
            meses = num_parcelas if isinstance(num_parcelas, int) else 1
    else:
        with st.expander("💸 Parâmetros do Parcelamento", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                valor = st.number_input("**Valor Total (R$)**", 
                                      min_value=0.01, 
                                      value=10000.0, 
                                      step=100.0,
                                      key="valor_total")
                desconto = st.number_input("**Desconto (R$)**", 
                                         min_value=0.0, 
                                         max_value=valor if valor > 0 else 0.0, 
                                         value=0.0, 
                                         step=100.0,
                                         key="desconto")
            with col2:
                percentual = (desconto / valor * 100) if valor > 0 else 0.0
                st.metric("**Percentual de Desconto**", f"{percentual:.2f}%")
                st.metric("**Valor Líquido**", formatar_moeda(valor - desconto))
                meses = num_parcelas if isinstance(num_parcelas, int) else 1
                st.metric("**Parcelas**", meses if isinstance(num_parcelas, int) else "À Vista")

    st.markdown("---")
    calcular_btn = st.button("🔄 Calcular", type="primary")

    if calcular_btn:
        try:
            tabela = []
            valor_base = valor - desconto 
            taxa_antecipacao_valor = valor_base * taxa_antecipacao
            valor_base_ajustado = valor_base + taxa_antecipacao_valor

            # Obtém a taxa bruta da estrutura MAQUINAS
            taxa_bruta = MAQUINAS[maquina][tipo_parcelamento][num_parcelas]

            # Cálculo da taxa mensal para Mercado Pago
            if maquina == "Mercado Pago":
                if isinstance(num_parcelas, int):
                    # Taxa bruta = taxa total para parcelado
                    taxa_total = taxa_bruta
                    taxa_mensal = (1 + taxa_total) ** (1/num_parcelas) - 1
                else:
                    # À vista: taxa única
                    taxa_mensal = taxa_bruta
                    taxa_total = taxa_bruta
            else:
                if isinstance(num_parcelas, int):
                    # Taxa bruta = taxa mensal para outras máquinas
                    taxa_mensal = taxa_bruta
                    taxa_total = (1 + taxa_mensal) ** num_parcelas - 1
                else:
                    # À vista: taxa única
                    taxa_mensal = taxa_bruta
                    taxa_total = taxa_bruta

            # Cálculo de financiamento
            total_pago = 0
            saldo = valor_base_ajustado

            if modo_calculo == "🏦 Financiamento":
                if metodo == "Price":
                    parcela = calcular_price(valor_base_ajustado, taxa_bruta, meses)
                    for i in range(1, meses + 1):
                        juros = saldo * taxa_bruta
                        amort = parcela - juros
                        saldo -= amort
                        total_pago += parcela
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Taxa Mensal": taxa_mensal,
                            "Taxa Total": taxa_total,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0),
                            "Taxa Antecipação": taxa_antecipacao_valor,
                            "Valor Base Ajustado": valor_base_ajustado,
                            "Total Pago": total_pago
                        })

                elif metodo == "SAC":
                    parcelas = calcular_sac(valor_base_ajustado, taxa_bruta, meses)
                    amort = valor_base_ajustado / meses
                    for i, parcela in enumerate(parcelas, 1):
                        juros = saldo * taxa_bruta
                        saldo -= amort
                        total_pago += parcela
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Taxa Mensal": taxa_mensal,
                            "Taxa Total": taxa_total,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0),
                            "Taxa Antecipação": taxa_antecipacao_valor,
                            "Valor Base Ajustado": valor_base_ajustado,
                            "Total Pago": total_pago
                        })

                elif metodo == "SACRE":
                    parcelas = calcular_sacre(valor_base_ajustado, taxa_bruta, meses)
                    amort_base = valor_base_ajustado / meses
                    fator = 1 + taxa_bruta
                    for i, parcela in enumerate(parcelas, 1):
                        juros = saldo * taxa_bruta
                        amort = amort_base * (fator ** i)
                        saldo -= amort
                        total_pago += parcela
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Taxa Mensal": taxa_mensal,
                            "Taxa Total": taxa_total,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0),
                            "Taxa Antecipação": taxa_antecipacao_valor,
                            "Valor Base Ajustado": valor_base_ajustado,
                            "Total Pago": total_pago
                        })

                elif metodo == "MEJS":
                    parcela = calcular_mejs(valor_base_ajustado, taxa_bruta, meses)
                    amort = valor_base_ajustado / meses
                    for i in range(1, meses + 1):
                        juros = valor_base_ajustado * taxa_bruta
                        saldo -= amort
                        total_pago += parcela
                        tabela.append({
                            "Mês": i,
                            "Parcela": parcela,
                            "Juros": juros,
                            "Taxa Mensal": taxa_mensal,
                            "Taxa Total": taxa_total,
                            "Amortização": amort,
                            "Saldo Devedor": max(saldo, 0),
                            "Taxa Antecipação": taxa_antecipacao_valor,
                            "Valor Base Ajustado": valor_base_ajustado,
                            "Total Pago": total_pago
                        })
                
                # Detalhes do cálculo
                with st.expander("🧮 Detalhes do Cálculo", expanded=False):
                    if metodo == "Price":
                        st.markdown(f"""
                        **Fórmula Price:**  
                        `P = (PV * i) / (1 - (1 + i)^-n)`  
                        
                        **Valores Aplicados:**  
                        - PV (Valor Presente) = {formatar_moeda(valor_base).replace('$', '\\$')}  
                        - i (Taxa Mensal) = {taxa_mensal:.4%}  
                        - n (Períodos) = {meses}  
                        
                        **Cálculo:**  
                        ```python
                        P = ({formatar_moeda(valor_base).replace('$', '\\$')} * {taxa_bruta:.4%}) 
                        / (1 - (1 + {taxa_bruta:.4%})^-{meses})
                        = {formatar_moeda(parcela).replace('$', '\\$')}
                        ```
                        """)
                    
                    elif metodo == "SAC":
                        st.markdown(f"""
                        **Fórmula SAC:**  
                        `Amortização = PV / n`  
                        `Juros = Saldo Devedor * i`  
                        `Parcela = Amortização + Juros`  
                        
                        **Parâmetros:**  
                        - Amortização Constante = {formatar_moeda(valor_base/meses).replace('$', '\\$')}  
             
                        """)
                    
                    elif metodo == "SACRE":
                        st.markdown(f"""
                        **Fórmula SACRE:**  
                        `Fator de Correção = 1 + i`  
                        `Amortização = (PV/n) * (1 + i)^período`  
                        
                        **Componentes:**  
                        - Fator Mensal = {1 + taxa_bruta:.5f}  
                        - Amortização Base = {formatar_moeda(valor_base/meses).replace('$', '\\$')} 
                       
                        """)
                    
                    elif metodo == "MEJS":
                        total_juros = valor_base * taxa_bruta * meses
                        st.markdown(f"""
                        **Fórmula MEJS:**  
                        `Total Juros = PV * i * n`  
                        `Parcela = (PV + Total Juros) / n`  
                        
                        **Cálculo Direto:**  
                        - Juros Totais = {formatar_moeda(total_juros).replace('$', '\\$')}  
                        - Parcela = ({formatar_moeda(valor_base).replace('$', '\\$')} + {formatar_moeda(total_juros).replace('$', '\\$')}) / {meses}  
                                          
                        """)

            else:  # Parcelamento Simples
                if isinstance(num_parcelas, int):
                    total_juros = valor * taxa_bruta * meses
                    valor_parcela = (valor + total_juros) / meses
                else:
                    total_juros = valor * taxa_bruta
                    valor_parcela = valor + total_juros
                
                for i in range(1, meses + 1):
                    tabela.append({
                        "Mês": i,
                        "Parcela": valor_parcela,
                        "Juros": total_juros / meses if isinstance(num_parcelas, int) else total_juros,
                        "Taxa Mensal": taxa_mensal,
                        "Taxa Total": taxa_total,
                        "Total Pago": valor_parcela * i
                    })
                
                
                # Detalhes do cálculo
                with st.expander("🧮 Detalhes do Cálculo", expanded=False):
                    if isinstance(num_parcelas, int):
                        st.markdown(f"""
                        **Fórmula Parcelado:**  
                        `Total Juros = Valor * Taxa * Parcelas`  
                        `Valor Parcela = (Valor + Total Juros) / Parcelas`  
                        
                        **Aplicação:**  
                        1. Total Juros = {formatar_moeda(valor).replace('$', '\\$')} * {taxa_bruta:.4%} * {meses} = {formatar_moeda(total_juros).replace('$', '\\$')}  
                        2. Valor Parcela = ({formatar_moeda(valor).replace('$', '\\$')} + {formatar_moeda(total_juros).replace('$', '\\$')}) / {meses}  
                        """)
                    else:
                        st.markdown(f"""
                        **Fórmula à Vista:**  
                        `Valor Total = Valor * (1 + Taxa)`  
                        
                        **Cálculo:**  
                        {formatar_moeda(valor).replace('$', '\\$')} * (1 + {taxa_bruta:.4%}) = {formatar_moeda(valor_parcela).replace('$', '\\$')}  
                        """)

            # Exibição dos resultados
            # Exibição dos resultados
            if tabela:
                df = pd.DataFrame(tabela)
                df = df.dropna(how='all')  # Remove apenas linhas totalmente vazias
                df['Mês'] = df['Mês'].astype(int)

                if 'Total Pago' not in df.columns:
                    df['Total Pago'] = df['Parcela'].cumsum()

                # Configurar colunas dinamicamente
                base_cols = ["Mês","Taxa Antecipação", "Taxa Mensal", "Taxa Total", "Parcela", "Juros",  "Total Pago"]
                
                if modo_calculo == "🏦 Financiamento":
                    # Inserir colunas extras nas posições específicas
                    base_cols.insert(5, "Amortização")
                    base_cols.insert(6, "Saldo Devedor")

                # Filtrar apenas colunas existentes no DataFrame
                valid_cols = [col for col in base_cols if col in df.columns]
                
                # Preencher valores NaN restantes
                df = df[valid_cols].fillna('-')
                
                # Formatação condicional
                st.markdown("### 📑 Detalhamento do Parcelamento")
                st.dataframe(
                    df.style.format({
                        'Mês': lambda x: f"{x:,.0f}",
                        'Taxa Mensal': lambda x: f"{x:.2%}" if x != '-' else '-',
                        'Taxa Total': lambda x: f"{x:.2%}" if x != '-' else '-',
                        **{col: lambda x: formatar_moeda(x) if x != '-' else '-' 
                        for col in valid_cols 
                        if col not in ['Mês','Taxa Mensal', 'Taxa Total']}
                    })
                    .applymap(lambda x: 'color: #eee60b;', subset=['Taxa Antecipação'])
                    .applymap(lambda x: 'color: #eee60b;', subset=['Taxa Mensal'])
                    .applymap(lambda x: 'color: #eee60b;', subset=['Taxa Total'])
                    .applymap(lambda x: 'color: #2ecc71;', subset=['Parcela'])
                    .applymap(lambda x: 'color: #2ecc71;', subset=['Juros'])
                    
                    .applymap(lambda x: 'color: #3498db;', subset=['Total Pago'])
                    .applymap(lambda x: 'color: #f39c12;', subset=['Amortização'] if 'Amortização' in valid_cols else [])
                    .applymap(lambda x: 'color: #f39c12;', subset=['Saldo Devedor'] if 'Saldo Devedor' in valid_cols else []),
                    use_container_width=True, hide_index=True, height=(35 * len(df) + 35)
                )
                            


                # Gráfico
                fig = px.line(
                    df, 
                    x="Mês", 
                    y="Parcela",
                    title="📈 Evolução das Parcelas",
                    markers=True,
                    color_discrete_sequence=["#2ecc71"]
                )
                fig.update_layout(
                    xaxis_title="Mês",
                    yaxis_title="Valor da Parcela",
                    xaxis=dict(tickmode='linear', dtick=1)
                )
                st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"## ❌ Erro no cálculo: {str(e)}")